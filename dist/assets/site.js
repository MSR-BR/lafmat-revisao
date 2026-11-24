/* Progressive enhancement: the initial HTML is already complete. */
'use strict';
const data = window.siteContent;
const languages = window.copy;
const routeTable = window.siteRoutes;
const videoGallery = window.buildVideoGallery(window.youtubeCatalog);
const main = document.querySelector('main');
const nav = document.querySelector('nav');
const menu = document.querySelector('.menu-button');
const state = {lang:'en', year:'all', country:'', memberQuery:'', galleryQuery:'', galleryChannel:'', galleryLimit:24};
let currentRoute;
let renderer;
function memberResults() {
  const results = window.createSiteRenderer(state).memberResults();
  document.getElementById('member-results').innerHTML = results.members;
  document.getElementById('collaborator-results').innerHTML = results.collaborators;
}
function galleryResults() {
  const results = window.createSiteRenderer(state).galleryResults();
  document.getElementById('gallery-results').innerHTML = results.html;
  document.getElementById('gallery-count').textContent = results.count;
  document.getElementById('gallery-more').hidden = !results.more;
}
function setMenu(open) {
  menu.setAttribute('aria-expanded',String(open));
  nav.classList.toggle('open',open);
  if (!open) setConferenceMenu(false);
}
function setConferenceMenu(open) {
  const button = nav.querySelector('.conference-toggle');
  const submenu = nav.querySelector('#conference-years');
  if (!button || !submenu) return;
  button.setAttribute('aria-expanded',String(open));
  submenu.hidden = !open;
}
function render({focus = false} = {}) {
  let savedLang = 'en';
  try { savedLang = localStorage.getItem('lafmat-language') || 'en'; } catch {}
  const resolved = routeTable.resolve(new URL(location.href), videoGallery.years, savedLang);
  if (!resolved) return; // Unknown addresses must remain server 404s.
  const {route,lang,sub,year} = resolved;
  if (route !== currentRoute || year !== state.year) {
    state.year = year;
    state.galleryQuery = '';
    state.galleryChannel = '';
    state.galleryLimit = 24;
  }
  state.lang = lang;
  currentRoute = route;
  const canonicalPath = routeTable.path(route,lang,sub);
  if (location.pathname+location.hash !== canonicalPath) {
    const destination = new URL(canonicalPath,location.origin);
    destination.search = location.search;
    history.replaceState(null,'',destination.pathname+destination.search+destination.hash);
  }
  renderer = window.createSiteRenderer(state);
  const t = languages[lang];
  document.documentElement.lang = t.locale;
  document.documentElement.classList.add('js');
  document.title = renderer.title(route);
  const meta = window.siteSEO(route,lang,year);
  document.title = meta.title;
  for (const [selector,value] of [
    ['meta[name="description"]',meta.description],
    ['meta[property="og:title"]',meta.title],
    ['meta[property="og:description"]',meta.description],
    ['meta[property="og:url"]',meta.canonical],
    ['meta[property="og:locale"]',meta.locale],
    ['meta[name="twitter:title"]',meta.title],
    ['meta[name="twitter:description"]',meta.description]
  ]) document.querySelector(selector)?.setAttribute('content',value);
  for (const item of meta.alternates) document.querySelector(`link[rel="alternate"][hreflang="${item.lang}"]`)?.setAttribute('href',item.url);
  document.querySelector('#skip').textContent = t.skip;
  document.querySelector('.brand').href = routeTable.path('home',lang);
  menu.setAttribute('aria-label',t.menu);
  nav.setAttribute('aria-label',t.menu);
  document.querySelector('.languages').setAttribute('aria-label',t.language);
  nav.innerHTML = renderer.navigation(route);
  document.querySelectorAll('[data-lang]').forEach(link=>{
    link.href = routeTable.path(route,link.dataset.lang,sub);
    if (link.dataset.lang === lang) link.setAttribute('aria-current','page');
    else link.removeAttribute('aria-current');
  });
  const canonical = document.querySelector('link[rel="canonical"]');
  if (canonical) canonical.href = 'https://lafmat.com'+routeTable.path(route,lang,year === 'all' ? '' : year);
  main.innerHTML = renderer.view(route,sub);
  document.querySelector('footer').innerHTML = renderer.footer();
  setMenu(false);
  const target = sub && document.getElementById(sub);
  if (target && main.contains(target)) {
    target.focus({preventScroll:true});
    target.scrollIntoView({block:'start'});
  } else if (focus) {
    window.scrollTo(0,0);
    main.focus({preventScroll:true});
  }
}
// Preserve native opening in a new tab and ordinary links outside this route set.
// A real href always works without JavaScript; History API is only an enhancement.
document.addEventListener('click',event=>{
  const link = event.target.closest('a[href]');
  if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || link.target || link.hasAttribute('download')) return;
  const url = new URL(link.href,location.href);
  if (url.origin !== location.origin || url.search !== location.search) return;
  const resolved = routeTable.resolve(url,videoGallery.years);
  if (!resolved || (!link.dataset.lang && url.pathname === location.pathname && url.hash && !routeTable.sections.includes(url.hash.slice(1).split('/')[0]))) return;
  const draft = link.dataset.lang && currentRoute === 'contact' ? new FormData(document.querySelector('#contact-form')) : null;
  event.preventDefault();
  if (link.dataset.lang) try { localStorage.setItem('lafmat-language',link.dataset.lang); } catch {}
  history.pushState(null,'',url.pathname+url.search+url.hash);
  render({focus:!link.dataset.lang});
  if (draft) for (const [name,value] of draft) document.querySelector('#contact-form').elements.namedItem(name).value = value;
});
nav.addEventListener('click',event=>{
  const toggle = event.target.closest('.conference-toggle');
  if (toggle) setConferenceMenu(toggle.getAttribute('aria-expanded') !== 'true');
  if (event.target.closest('a')) setMenu(false);
});
nav.addEventListener('keydown',event=>{
  if (event.key === 'ArrowDown' && event.target.closest('.conference-toggle')) {
    event.preventDefault();
    setConferenceMenu(true);
    nav.querySelector('#conference-years a')?.focus();
  }
});
nav.addEventListener('focusout',event=>{
  if (event.target.closest('.nav-dropdown') && !event.relatedTarget?.closest('.nav-dropdown')) setConferenceMenu(false);
});
document.addEventListener('click',event=>{
  if (!event.target.closest('.nav-dropdown')) setConferenceMenu(false);
});
menu.addEventListener('click',()=>setMenu(menu.getAttribute('aria-expanded') !== 'true'));
document.addEventListener('keydown',event=>{
  if (event.key !== 'Escape') return;
  const conferenceButton = nav.querySelector('.conference-toggle');
  if (conferenceButton?.getAttribute('aria-expanded') === 'true') {
    setConferenceMenu(false);
    conferenceButton.focus();
  } else if (menu.getAttribute('aria-expanded') === 'true') { setMenu(false); menu.focus(); }
});
document.querySelector('#skip').addEventListener('click',event=>{event.preventDefault(); main.focus();});
main.addEventListener('input',event=>{
  const {id,value} = event.target;
  if (id === 'member-search') {state.memberQuery = value; memberResults();}
  if (id === 'gallery-search') {state.galleryQuery = value; state.galleryLimit = 24; galleryResults();}
});
main.addEventListener('change',event=>{
  if (event.target.id === 'country-filter') {state.country = event.target.value; memberResults();}
  if (event.target.id === 'gallery-channel') {state.galleryChannel = event.target.value; state.galleryLimit = 24; galleryResults();}
});
main.addEventListener('click',event=>{
  if (event.target.closest('#gallery-more')) {state.galleryLimit += 24; galleryResults();}
});
main.addEventListener('submit',event=>{
  if (event.target.id !== 'contact-form') return;
  event.preventDefault();
  const fields = new FormData(event.target);
  const body = `${fields.get('message')}\r\n\r\n${fields.get('name')} <${fields.get('email')}>`;
  location.href = `mailto:${data.contact.email}?subject=${encodeURIComponent(fields.get('subject'))}&body=${encodeURIComponent(body)}`;
});
window.addEventListener('hashchange',()=>render({focus:true}));
window.addEventListener('popstate',()=>render({focus:true}));
render();
