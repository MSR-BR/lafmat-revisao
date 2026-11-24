/* Metadata follows the same section/language contract as visible content. */
'use strict';
window.siteSEO = (route,lang,year = '') => {
  const t = window.copy[lang];
  const path = window.siteRoutes.path(route,lang,year === 'all' ? '' : year);
  const descriptions = {
    home:t.footer+'. '+t.hero,
    members:t.memberIntro+' · LAFMAT',
    gallery:t.galleryIntro+(year && year !== 'all' ? ' · '+year : '')+' · LAFMAT',
    news:t.newsIntro+' · LAFMAT',
    seminars:(lang === 'en' ? window.archive.seminarEnglish : t.seminarIntro)[0],
    conferences:t.confIntro+' · LAFMAT',
    contact:t.write+'. '+t.formHint,
    privacy:window.lafmatPrivacy[lang].intro
  };
  return {
    title:route === 'home' ? 'LAFMAT · '+t.footer : t.nav[window.siteRoutes.sections.indexOf(route)]+(route === 'gallery' && year && year !== 'all' ? ' · '+year : '')+' · LAFMAT',
    description:descriptions[route],canonical:'https://lafmat.com'+path,
    alternates:[...window.siteRoutes.languages.map(code=>({lang:window.copy[code].locale,url:'https://lafmat.com'+window.siteRoutes.path(route,code,year === 'all' ? '' : year)})),{lang:'x-default',url:'https://lafmat.com'+window.siteRoutes.path(route,'en',year === 'all' ? '' : year)}],
    image:'https://lafmat.com/assets/lafmat-social.png',
    locale:{en:'en_US',pt:'pt_BR',es:'es_ES'}[lang],
    organization:{'@context':'https://schema.org','@type':'Organization','@id':'https://lafmat.com/#organization',name:'LAFMAT',alternateName:window.copy.en.footer,url:'https://lafmat.com/',logo:'https://lafmat.com/assets/logo.png',sameAs:[window.siteContent.youtube,window.siteContent.facebook]}
  };
};
