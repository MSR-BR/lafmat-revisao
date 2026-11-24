/* Single route contract shared by the static builder and browser. */
'use strict';
window.siteRoutes = (() => {
  const sections = ['home','members','gallery','news','seminars','conferences','contact','privacy'];
  const slugs = {home:'',members:'members',gallery:'videos',news:'news',seminars:'seminars',conferences:'conferences',contact:'contact',privacy:'privacy'};
  const languages = ['en','pt','es'];
  function path(section, lang = 'en', sub = '') {
    if (!sections.includes(section) || !languages.includes(lang)) throw new Error('Unknown route');
    const parts = [lang === 'en' ? '' : lang, slugs[section]];
    if (section === 'gallery' && /^20\d{2}$/.test(sub)) parts.push(sub);
    const base = '/'+parts.filter(Boolean).join('/')+(parts.some(Boolean) ? '/' : '');
    return base + (sub && !(section === 'gallery' && /^20\d{2}$/.test(sub)) ? '#'+encodeURIComponent(sub) : '');
  }
  function resolve(url, years = [], legacyLang = 'en') {
    const parts = url.pathname.replace(/\/index\.html$/, '/').split('/').filter(Boolean);
    const lang = ['pt','es'].includes(parts[0]) ? parts.shift() : 'en';
    const section = parts.length ? sections.find(key=>slugs[key] === parts[0]) : 'home';
    if (!section || parts.length > 2 || (parts[1] && !(section === 'gallery' && years.includes(parts[1])))) return null;
    let route = section;
    let sub = parts[1] || '';
    let resultLang = lang;
    const [oldRoute, oldSub] = url.hash.slice(1).split('/');
    if (sections.includes(oldRoute)) {
      route = oldRoute;
      sub = oldSub || '';
      if (!parts.length && lang === 'en' && languages.includes(legacyLang)) resultLang = legacyLang;
    } else if (url.hash) {
      try { sub = decodeURIComponent(url.hash.slice(1)); } catch { return null; }
    }
    if (route === 'gallery' && sub && !years.includes(sub)) return null;
    return {route,lang:resultLang,sub,year:route === 'gallery' && sub ? sub : 'all'};
  }
  return {sections,languages,path,resolve};
})();
