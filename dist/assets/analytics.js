/* Basic opt-in: no Google code/request before consent; no free-text payloads. */
'use strict';
(() => {
  const config = window.lafmatAnalyticsConfig;
  const key = 'lafmat-analytics-consent-v1';
  const id = config.measurementId;
  const production = config.enabled && /^G-[A-Z0-9]+$/.test(id) && location.protocol === 'https:' && config.allowedHosts.includes(location.hostname);
  const escape = value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const lang = ()=>document.documentElement.lang.startsWith('pt') ? 'pt' : document.documentElement.lang.startsWith('es') ? 'es' : 'en';
  const text = ()=>window.lafmatPrivacy[lang()];
  const archiveSlugs = ['event-home','venue','topics','commitee','poster-2','publications','registration','2757-2','event-contact','important-dates','program'];
  let loaded = false;
  let choice = '';
  function routeInfo() {
    const pathname = location.pathname.replace(/\/index\.html$/,'/');
    const year = pathname.match(/\/videos\/(20\d\d)\/$/)?.[1];
    const parsed = window.siteRoutes.resolve(new URL(location.origin+pathname),year ? [year] : []);
    if (parsed) {
      const t = window.copy[parsed.lang];
      const url = 'https://lafmat.com'+window.siteRoutes.path(parsed.route,parsed.lang,parsed.year === 'all' ? '' : parsed.year);
      const title = parsed.route === 'home' ? 'LAFMAT · '+t.footer : t.nav[window.siteRoutes.sections.indexOf(parsed.route)]+(parsed.year !== 'all' ? ' · '+parsed.year : '')+' · LAFMAT';
      return {url,title,section:parsed.route,lang:parsed.lang};
    }
    const match = pathname.match(/^\/conferences\/2023\/(?:([^/]+)\/)?$/);
    if (match && (!match[1] || archiveSlugs.includes(match[1]))) return {url:'https://lafmat.com'+pathname,title:'Conference 2023 · LAFMAT',section:'conference_2023',lang:'en'};
    return null;
  }
  function send(name,params) {
    if (!production || choice !== 'granted' || !loaded) return;
    window.gtag('set',{page_location:params.page_location,page_title:params.page_title,page_referrer:params.page_referrer});
    const debug = new URL(location.href).searchParams.get('lafmat_analytics_test') === '1';
    window.gtag('event',name,{...params,...(debug ? {debug_mode:true,traffic_type:'internal'} : {})});
  }
  const measurement = window.createLafmatMeasurement({routeInfo,send,config});
  function readChoice() {
    try {
      const saved = JSON.parse(localStorage.getItem(key));
      if (saved?.version === 1 && ['granted','denied'].includes(saved.choice) && Number.isFinite(saved.time) && saved.time <= Date.now() && Date.now()-saved.time < config.consentDays*86400000) return saved.choice;
    } catch {}
    return '';
  }
  function saveChoice(value) {
    choice=value;
    try { localStorage.setItem(key,JSON.stringify({version:1,choice:value,time:Date.now()})); } catch {}
  }
  function clearCookies() {
    for (const cookie of document.cookie.split(';')) {
      const name = cookie.split('=')[0].trim();
      if (!/^_ga(?:_|$)/.test(name)) continue;
      for (const domain of ['',location.hostname,'.'+location.hostname,'.lafmat.com']) {
        document.cookie=name+'=; Max-Age=0; Path=/; SameSite=Lax'+(domain ? '; Domain='+domain : '');
      }
    }
  }
  function load() {
    if (loaded || !production || choice !== 'granted') return;
    loaded=true;
    window['ga-disable-'+id]=false;
    window.dataLayer=window.dataLayer || [];
    window.gtag=function(){window.dataLayer.push(arguments);};
    window.gtag('consent','default',{analytics_storage:'granted',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
    window.gtag('set','ads_data_redaction',true);
    window.gtag('js',new Date());
    const page=routeInfo();
    window.gtag('config',id,{send_page_view:false,allow_google_signals:false,allow_ad_personalization_signals:false,url_passthrough:false,cookie_expires:config.consentDays*86400,cookie_update:false,page_location:page?.url || 'https://lafmat.com/',page_title:page?.title || 'LAFMAT',page_referrer:''});
    const script=document.createElement('script');
    script.async=true;
    script.referrerPolicy='no-referrer';
    script.src='https://www.googletagmanager.com/gtag/js?id='+id;
    script.id='lafmat-google-tag';
    document.head.append(script);
  }
  const panel=document.createElement('section');
  panel.id='analytics-consent';
  panel.setAttribute('role','dialog');
  panel.setAttribute('aria-labelledby','analytics-consent-title');
  panel.setAttribute('aria-describedby','analytics-consent-text');
  panel.hidden=true;
  document.body.append(panel);
  let returnFocus;
  function renderPanel() {
    const t=text();
    panel.innerHTML=`<h2 id="analytics-consent-title">${escape(t.heading)}</h2><p id="analytics-consent-text">${escape(t.banner)}</p><div class="analytics-choices"><button type="button" data-analytics-choice="granted">${escape(t.accept)}</button><button type="button" data-analytics-choice="denied">${escape(t.reject)}</button><a href="${window.siteRoutes.path('privacy',lang())}">${escape(t.policy)}</a></div>`;
  }
  function open() {
    returnFocus=document.activeElement;
    renderPanel();panel.hidden=false;
    panel.querySelector('button')?.focus({preventScroll:true});
  }
  function close() { panel.hidden=true;returnFocus?.focus?.({preventScroll:true}); }
  function footerControls() {
    let footer=document.querySelector('footer');
    if (!footer) {footer=document.createElement('footer');document.body.append(footer);}
    let controls=footer.querySelector('.analytics-preferences');
    if (!controls) {controls=document.createElement('div');controls.className='analytics-preferences';footer.append(controls);}
    const t=text();
    controls.innerHTML=`<a href="${window.siteRoutes.path('privacy',lang())}">${escape(t.policy)}</a><button type="button" data-analytics-preferences>${escape(t.preferences)}</button>`;
  }
  panel.addEventListener('click',event=>{
    const button=event.target.closest('[data-analytics-choice]');
    if (!button) return;
    const value=button.dataset.analyticsChoice;
    const revoking=loaded && value === 'denied';
    saveChoice(value);
    if (value === 'granted') {load();measurement.grant(document.referrer);}
    else {
      measurement.deny();
      window['ga-disable-'+id]=true;
      clearCookies();
    }
    close();
    // Unload Google's already-loaded runtime after withdrawal. No denied-mode
    // Google tag or consent ping is deliberately loaded/sent by this site.
    if (revoking) location.reload();
  });
  document.addEventListener('click',event=>{
    if (event.target.closest('[data-analytics-preferences]')) {open();return;}
    const anchor=event.target.closest('a[href]');
    if (!anchor || !measurement.isGranted()) return;
    let url;
    try {url=new URL(anchor.href,location.href);} catch {return;}
    if (url.protocol === 'mailto:') return measurement.action('contact_click',{category:'email'});
    if (url.protocol === 'tel:') return measurement.action('contact_click',{category:'phone'});
    if (!/^https?:$/.test(url.protocol)) return;
    if (/\.(pdf|zip)$/i.test(url.pathname)) return measurement.action('file_download_click',{category:url.pathname.split('.').at(-1).toLowerCase()});
    if (url.origin === location.origin && /^\/conferences\/2023\//.test(url.pathname)) return measurement.action('conference_archive_open',{category:'2023'});
    if (['youtube.com','www.youtube.com','youtu.be'].includes(url.hostname)) {
      const category=url.pathname.includes('/watch') || url.hostname === 'youtu.be' ? 'recording' : url.pathname.toLowerCase().includes('gimatefun') ? 'gimatefun' : 'network';
      return measurement.action('video_outbound_click',{category});
    }
    if (url.origin !== location.origin) measurement.action('outbound_click',{category:url.hostname.endsWith('facebook.com') ? 'facebook' : url.hostname === 'scholar.google.com' ? 'scholar' : 'other'});
  });
  window.addEventListener('lafmat:navigation',()=>{footerControls();if (!panel.hidden) renderPanel();measurement.page(document.referrer);});
  window.addEventListener('lafmat:contact-draft',()=>measurement.action('contact_draft_open',{category:'email'}));
  window.addEventListener('storage',event=>{
    if (event.key !== key && event.key !== null) return;
    const next=readChoice();
    const revoking=loaded && next !== 'granted';
    choice=next;
    if (next === 'granted') {load();measurement.grant(document.referrer);panel.hidden=true;}
    else {
      measurement.deny();window['ga-disable-'+id]=true;clearCookies();
      panel.hidden=next === 'denied';
      if (revoking) location.reload();
    }
  });
  choice=readChoice();
  footerControls();renderPanel();
  if (choice === 'granted') {load();measurement.grant(document.referrer);}
  else if (!choice) panel.hidden=false;
})();
