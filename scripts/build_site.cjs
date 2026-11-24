#!/usr/bin/env node
'use strict';
// Offline, dependency-free build. Only project-owned JS is evaluated in the VM.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const crypto = require('node:crypto');
const root = path.resolve(__dirname,'..');
const dist = path.join(root,'dist');
const sources = ['archive.js','content.js','videos.js','video-gallery.js','i18n.js','routes.js','privacy.js','site-render.js','seo.js','analytics-config.js','analytics-core.js'];
function load() {
  const context = {window:{},URL};
  vm.createContext(context);
  for (const file of sources) vm.runInContext(fs.readFileSync(path.join(dist,'assets',file),'utf8'),context,{filename:file,timeout:5000});
  return context.window;
}
function build({today} = {}) {
  const site = load();
  const template = fs.readFileSync(path.join(root,'templates/site.html'),'utf8');
  const digest = file=>crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
  const escape = value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const gallery = site.buildVideoGallery(site.youtubeCatalog);
  const routeTable = site.siteRoutes;
  const buildDate = today || new Intl.DateTimeFormat('sv-SE',{timeZone:'America/Sao_Paulo',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
  if (!/^20\d{2}-\d{2}-\d{2}$/.test(buildDate) || !Number.isFinite(Date.parse(buildDate))) throw new Error('Invalid build date');
  const scriptTags = [...sources,'site.js','analytics.js'].map(file=>`  <script defer src="/assets/${file}?v=${digest(path.join(dist,'assets',file)).slice(0,12)}"></script>`).join('\n');
  const pages = [];
  const receiptPath = path.join(root,'docs/seo/static-build.json');
  const previous = fs.existsSync(receiptPath) ? JSON.parse(fs.readFileSync(receiptPath,'utf8')) : null;
  for (const lang of routeTable.languages) {
    const copy = site.copy[lang];
    for (const section of routeTable.sections) {
      for (const year of section === 'gallery' ? ['',...gallery.years] : ['']) {
        const state = {lang,year:year || 'all',country:'',memberQuery:'',galleryQuery:'',galleryChannel:'',galleryLimit:24};
        const renderer = site.createSiteRenderer(state,{static:true,today:buildDate});
        const url = routeTable.path(section,lang,year);
        const file = url.slice(1)+'index.html';
        const meta = site.siteSEO(section,lang,year);
        const jsonLD = JSON.stringify(meta.organization).replace(/</g,'\\u003c');
        const seo = [
          `<link rel="canonical" href="${meta.canonical}">`,
          ...meta.alternates.map(item=>`<link rel="alternate" hreflang="${item.lang}" href="${item.url}">`),
          `<meta property="og:type" content="website">`,
          `<meta property="og:site_name" content="LAFMAT">`,
          `<meta property="og:title" content="${escape(meta.title)}">`,
          `<meta property="og:description" content="${escape(meta.description)}">`,
          `<meta property="og:url" content="${meta.canonical}">`,
          `<meta property="og:image" content="${meta.image}">`,
          `<meta property="og:image:width" content="1200">`,
          `<meta property="og:image:height" content="630">`,
          `<meta property="og:image:alt" content="LAFMAT · ${escape(site.copy.en.footer)}">`,
          `<meta property="og:locale" content="${meta.locale}">`,
          `<meta name="twitter:card" content="summary_large_image">`,
          `<meta name="twitter:title" content="${escape(meta.title)}">`,
          `<meta name="twitter:description" content="${escape(meta.description)}">`,
          `<meta name="twitter:image" content="${meta.image}">`,
          `<script type="application/ld+json" id="organization-data">${jsonLD}</script>`
        ].map(line=>'  '+line).join('\n');
        const replacements = {
          locale:escape(copy.locale), title:escape(meta.title), seo,
          description:escape(meta.description), cssVersion:digest(path.join(dist,'assets/site.css')).slice(0,12), analyticsCssVersion:digest(path.join(dist,'assets/analytics.css')).slice(0,12),
          scripts:scriptTags, skip:escape(copy.skip), homePath:routeTable.path('home',lang),
          menu:escape(copy.menu), language:escape(copy.language), navigation:renderer.navigation(section),
          languages:routeTable.languages.map(code=>`<a data-lang="${code}" lang="${site.copy[code].locale}" hreflang="${site.copy[code].locale}" href="${routeTable.path(section,code,year)}"${code === lang ? ' aria-current="page"' : ''}>${code.toUpperCase()}</a>`).join('\n'),
          main:renderer.view(section), footer:renderer.footer()
        };
        const html = template.replace(/\{\{(\w+)\}\}/g,(_,key)=>{
          if (!(key in replacements)) throw new Error('Unknown placeholder '+key);
          return replacements[key];
        }).replace(/[ \t]+$/gm,'');
        fs.mkdirSync(path.dirname(path.join(dist,file)),{recursive:true});
        fs.writeFileSync(path.join(dist,file),html);
        const sha256 = crypto.createHash('sha256').update(html).digest('hex');
        const prior = previous?.pages.find(page=>page.path === url);
        // Ignore cache-busting script hashes for lastmod: changing a script alone
        // is not a significant editorial update to every page.
        const contentHash = crypto.createHash('sha256').update(replacements.main+replacements.title+replacements.description+seo).digest('hex');
        const lastmod = prior?.contentHash === contentHash ? prior.lastmod : buildDate;
        pages.push({path:url,file,section,lang,year:year || null,sha256,contentHash,lastmod});
      }
    }
  }
  // Remove only stale files explicitly owned by the previous build; never archives.
  const files = new Set(pages.map(page=>page.file));
  for (const page of previous?.pages || []) {
    if (!files.has(page.file) && /^(?:(?:pt|es)\/)?videos\/20\d{2}\/index\.html$/.test(page.file)) fs.rmSync(path.join(dist,page.file),{force:true});
  }
  const inputs = Object.fromEntries([...sources.map(file=>'dist/assets/'+file),'dist/assets/site.css','dist/assets/site.js','dist/assets/analytics.js','dist/assets/analytics.css','templates/site.html','scripts/build_site.cjs','docs/seo/archive-canonical-routes.json'].map(file=>[file,digest(path.join(root,file))]));
  const receipt = {schema:1,buildDate,publication:'Release state recorded in docs/seo/release-validation.md',inputs,counts:{pages:pages.length,recordings:site.youtubeCatalog.videos.length,videoGroups:gallery.groups.length,members:site.siteContent.members.length,collaborators:site.siteContent.collaborators.length},pages};
  fs.mkdirSync(path.dirname(receiptPath),{recursive:true});
  const archived = JSON.parse(fs.readFileSync(path.join(root,'docs/seo/archive-canonical-routes.json'),'utf8'));
  // Instrument only canonical archive HEADs, preserving every source body and
  // legacy alias. Stable URLs avoid recurring archive edits on catalog updates.
  const archiveAnalytics = '<!-- LAFMAT_ANALYTICS_BEGIN -->\n<link rel="stylesheet" href="/assets/analytics.css">\n'+['i18n.js','routes.js','privacy.js','analytics-config.js','analytics-core.js','analytics.js'].map(file=>`<script defer src="/assets/${file}"></script>`).join('\n')+'\n<!-- LAFMAT_ANALYTICS_END -->\n';
  for (const page of archived) {
    const target=path.join(dist,page.file);
    const original=fs.readFileSync(target,'utf8');
    const without=original.replace(/<!-- LAFMAT_ANALYTICS_BEGIN -->[\s\S]*?<!-- LAFMAT_ANALYTICS_END -->\n?/g,'');
    fs.writeFileSync(target,without.replace('</head>',archiveAnalytics+'</head>'));
  }
  const sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+[
    ...pages.map(page=>`  <url><loc>https://lafmat.com${page.path}</loc><lastmod>${page.lastmod}</lastmod></url>`),
    // The archive's significant original update date is unknown; omit lastmod.
    ...archived.map(page=>`  <url><loc>https://lafmat.com${page.path}</loc></url>`)
  ].join('\n')+'\n</urlset>\n';
  fs.writeFileSync(path.join(dist,'sitemap.xml'),sitemap);
  fs.writeFileSync(path.join(dist,'robots.txt'),'User-agent: *\nAllow: /\n\nSitemap: https://lafmat.com/sitemap.xml\n');
  receipt.artifacts = Object.fromEntries(['sitemap.xml','robots.txt'].map(file=>[file,digest(path.join(dist,file))]));
  fs.writeFileSync(receiptPath,JSON.stringify(receipt,null,2)+'\n');
  console.log(`Built ${pages.length} static pages; ${receipt.counts.recordings} recordings; date ${buildDate}`);
  return receipt;
}
if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length && (args.length !== 2 || args[0] !== '--date')) throw new Error('Usage: node scripts/build_site.cjs [--date YYYY-MM-DD]');
  build({today:args[1]});
}
module.exports = {build,load};
