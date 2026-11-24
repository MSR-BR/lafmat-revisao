/* Explicit, minimal event model; transport and consent UI live in analytics.js. */
'use strict';
window.createLafmatMeasurement = ({routeInfo, send, config}) => {
  let consent = false;
  let lastPage = '';
  let previousPage = '';
  let pageReferrer = '';
  function currentPage() {
    const current=routeInfo();
    if (!current) return null;
    try {
      const url=new URL(current.url);
      if (url.origin !== 'https://lafmat.com' || url.search || url.hash || url.username || url.password || !['en','pt','es'].includes(current.lang)) return null;
    } catch {return null;}
    return current;
  }
  const cleanReferrer = value => {
    try {
      const url = new URL(value);
      if (!/^https?:$/.test(url.protocol) || url.username || url.password) return '';
      if (url.origin === 'https://lafmat.com') {
        const year=url.pathname.match(/\/videos\/(20\d\d)\/$/)?.[1];
        const route=window.siteRoutes.resolve(new URL(url.origin+url.pathname),year ? [year] : []);
        return route ? 'https://lafmat.com'+window.siteRoutes.path(route.route,route.lang,route.year === 'all' ? '' : route.year) : '';
      }
      // Do not forward arbitrary private hosts, paths, queries or fragments.
      const host=url.hostname.toLowerCase();
      if (/^(?:www\.)?google\.(?:com|com\.br|co\.uk|[a-z]{2})$/.test(host)) return 'https://www.google.com/';
      const known=['bing.com','duckduckgo.com','search.yahoo.com','youtube.com','facebook.com'];
      const match=known.find(domain=>host === domain || host === 'www.'+domain);
      return match ? 'https://'+match+'/' : '';
    } catch { return ''; }
  };
  function page(referrer = '') {
    if (!consent) return;
    const current = currentPage();
    if (!current || lastPage === current.url) return;
    pageReferrer=previousPage || cleanReferrer(referrer);
    send('page_view',{
      page_location:current.url,page_title:current.title,
      page_referrer:pageReferrer,
      app_surface:current.section,app_language:current.lang
    });
    previousPage = current.url;
    lastPage = current.url;
  }
  function action(name, detail = {}) {
    if (!consent) return;
    const current = currentPage();
    if (!current) return;
    const allowed = {
      video_outbound_click:['network','gimatefun','recording','channel'],
      file_download_click:['pdf','zip'],
      contact_click:['email','phone'],
      contact_draft_open:['email'],
      outbound_click:['facebook','scholar','other'],
      conference_archive_open:['2023']
    };
    if (!allowed[name]?.includes(detail.category)) return;
    send(name,{page_location:current.url,page_title:current.title,page_referrer:pageReferrer,app_surface:current.section,app_language:current.lang,app_action_category:detail.category});
  }
  return {
    grant(referrer='') { consent=true; page(referrer); },
    deny() { consent=false;lastPage='';previousPage='';pageReferrer=''; },
    page,action,
    isGranted:()=>consent
  };
};
