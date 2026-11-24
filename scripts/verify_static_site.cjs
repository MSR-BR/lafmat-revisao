#!/usr/bin/env node
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {load} = require('./build_site.cjs');
const root = path.resolve(__dirname,'..');
const dist = path.join(root,'dist');
const receipt = JSON.parse(fs.readFileSync(path.join(root,'docs/seo/static-build.json'),'utf8'));
const site = load();
const gallery = site.buildVideoGallery(site.youtubeCatalog);
for (const [file,expected] of Object.entries(receipt.artifacts || {})) {
  assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(dist,file))).digest('hex'),expected,'Generated SEO artifact modified; rebuild '+file);
}
for (const [file,expected] of Object.entries(receipt.inputs)) {
  const digest = crypto.createHash('sha256').update(fs.readFileSync(path.join(root,file))).digest('hex');
  assert.equal(digest,expected,`Stale generated HTML: ${file} changed. Run node scripts/build_site.cjs before updating the manifest.`);
}
const decode = value=>value.replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>');
const expectedCount = site.siteRoutes.languages.length*(site.siteRoutes.sections.length+gallery.years.length);
assert.equal(receipt.pages.length,expectedCount);
assert.equal(new Set(receipt.pages.map(page=>page.path)).size,expectedCount);
let checkedLinks = 0;
for (const page of receipt.pages) {
  const html = fs.readFileSync(path.join(dist,page.file),'utf8');
  assert.equal(crypto.createHash('sha256').update(html).digest('hex'),page.sha256,'Generated output modified; rebuild '+page.path);
  const text = decode(html.replace(/<[^>]*>/g,' '));
  const main = html.match(/<main\b[^>]*>([\s\S]*?)<\/main>/)?.[1];
  assert(main && main.length > 100,`Empty main: ${page.path}`);
  assert.equal((main.match(/<h1\b/g) || []).length,1,page.path);
  assert(html.includes(`<html lang="${site.copy[page.lang].locale}">`));
  assert(!html.includes('Ative JavaScript para navegar'));
  assert(!/href="#(?:home|members|gallery|news|seminars|conferences|contact)(?:["/])/.test(html),'Legacy hash in crawlable navigation');
  const resolved = site.siteRoutes.resolve(new URL('https://lafmat.com'+page.path),gallery.years);
  assert.equal(resolved.route,page.section);
  assert.equal(resolved.lang,page.lang);
  assert.equal(resolved.year,page.year || 'all');
  for (const lang of site.siteRoutes.languages) assert(html.includes(`href="${site.siteRoutes.path(page.section,lang,page.year || '')}"`),'Missing language counterpart');
  if (page.section === 'members') {
    for (const row of site.siteContent.members) assert(text.includes(row[1]),'Missing member '+row[1]);
    for (const row of site.siteContent.collaborators) assert(text.includes(row[0]),'Missing collaborator '+row[0]);
    assert.equal((main.match(/class="member card"/g) || []).length,site.siteContent.members.length+site.siteContent.collaborators.length);
  }
  if (page.section === 'gallery') {
    const groups = gallery.groups.filter(item=>!page.year || item.year === page.year);
    assert.equal((main.match(/class="record card"/g) || []).length,groups.length);
    for (const item of groups) {
      assert(text.includes(item.title),`Missing video title ${item.id}`);
      for (const source of item.sources) assert(main.includes(source.url.replace(/&/g,'&amp;')),`Missing recording ${source.id}`);
    }
  }
  if (page.section === 'seminars') {
    const expected = site.siteContent.seminars.filter(row=>row[0] >= receipt.buildDate);
    const dates = Array.from(main.matchAll(/<time datetime="(\d{4}-\d\d-\d\d)">/g),match=>match[1]);
    assert.deepEqual([...new Set(dates)].sort(),Array.from(expected,row=>row[0]).sort());
    for (const row of expected) for (const value of row.slice(1,5)) if (value) assert(text.includes(value),'Schedule lost '+value);
  }
  for (const [,attribute,encoded] of html.matchAll(/\b(href|src)="([^"]+)"/g)) {
    const value = decode(encoded);
    const url = new URL(value,'https://lafmat.com'+page.path);
    if (url.origin !== 'https://lafmat.com') continue;
    assert(value.startsWith('/') || value.startsWith('#') || value.startsWith('https://lafmat.com/'),'Relative local link: '+value);
    const localFile = path.join(dist,url.pathname.endsWith('/') ? url.pathname+'index.html' : url.pathname);
    assert(fs.existsSync(localFile),'Broken local link: '+page.path+' -> '+url.pathname);
    if (attribute === 'href' && url.hash && url.pathname === page.path) assert(html.includes(`id="${decodeURIComponent(url.hash.slice(1))}"`),'Broken page anchor');
    checkedLinks++;
  }
}
// Old shared URLs retain their section/year/anchor; explicit locales win over storage.
for (const route of site.siteRoutes.sections) {
  const parsed = site.siteRoutes.resolve(new URL('https://lafmat.com/#'+route),gallery.years,'es');
  assert.equal(parsed.route,route);
  assert.equal(parsed.lang,'es');
}
assert.equal(site.siteRoutes.resolve(new URL('https://lafmat.com/#gallery/2023'),gallery.years).year,'2023');
assert.equal(site.siteRoutes.resolve(new URL('https://lafmat.com/#news/item-0'),gallery.years).sub,'item-0');
assert.equal(site.siteRoutes.resolve(new URL('https://lafmat.com/pt/members/'),gallery.years,'es').lang,'pt');
for (const bad of ['/missing/','/videos/1900/','/members/extra/','/conferences/2023/event-home/']) assert.equal(site.siteRoutes.resolve(new URL('https://lafmat.com'+bad),gallery.years),null);
// Current date is dynamic in the browser and controllable for deterministic static builds.
const state = {lang:'en',year:'all',country:'',memberQuery:'',galleryQuery:'',galleryChannel:'',galleryLimit:24};
assert(site.createSiteRenderer(state,{today:'2026-11-24'}).view('home').includes('debora-vasconcelos-2026-11-28.jpg'));
assert(!site.createSiteRenderer(state,{today:'2026-11-29'}).view('home').includes('debora-vasconcelos-2026-11-28.jpg'));
assert(!site.createSiteRenderer(state,{today:'2027-08-01'}).view('home').includes('debora-vasconcelos-2026-11-28.jpg'));
const results = site.createSiteRenderer({...state,memberQuery:'Mario Reis'}).memberResults();
assert(results.members.includes('Mario Reis') && !results.members.includes('J. Albino Aguiar'));
assert(!/src="assets\//.test(results.members),'Filtered avatar path must remain absolute');
const limited = site.createSiteRenderer(state).galleryResults();
assert.equal((limited.html.match(/class="record card"/g) || []).length,24);
assert(limited.more);
const empty = site.createSiteRenderer({...state,galleryQuery:'nonexistent-unique-lecture-xyz'}).galleryResults();
assert.equal(empty.more,false);
assert.equal(empty.count,'0 '+site.copy.en.videoResults);
console.log(`PASS: ${receipt.pages.length} complete static routes; ${checkedLinks} local links/assets; ${site.youtubeCatalog.videos.length} recording links; source parity, dates, filters, languages and legacy routes`);
