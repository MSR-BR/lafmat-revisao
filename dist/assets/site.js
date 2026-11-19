'use strict';

const data = window.siteContent;
const archive = window.archive;
const videoCatalog = window.youtubeCatalog;
const videoGallery = window.buildVideoGallery(videoCatalog);
const languages = window.copy;
const routes = ['home','members','gallery','news','seminars','conferences','contact'];
const main = document.querySelector('main');
const nav = document.querySelector('nav');
const menu = document.querySelector('.menu-button');
const state = {lang:'en', year:'all', country:'', memberQuery:'', galleryQuery:'', galleryChannel:'', galleryLimit:24};
const collaborators = data.collaborators.map(([name,affiliation,country])=>[country,name,affiliation]);
try { state.lang = localStorage.getItem('lafmat-language') || 'en'; } catch {}
if (!Object.hasOwn(languages, state.lang)) state.lang = 'en';
let t;
let currentRoute;
const esc = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const normalized = value => value.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase();
const paragraphs = lines => lines.map(line => `<p>${esc(line)}</p>`).join('');
const external = (url, label, classes = 'text-link') => {
  if (!/^(https?:\/\/|mailto:)/i.test(url ?? '')) return '';
  return `<a class="${classes}" href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(label)} <span aria-hidden="true">↗</span></a>`;
};
const pageTitle = (title, intro = '') => `<div class="page-heading"><h1>${esc(title)}</h1>${intro ? `<p>${esc(intro)}</p>` : ''}</div>`;
const localizedDate = (iso, options) => new Intl.DateTimeFormat(t.locale, {timeZone:'UTC', ...options}).format(new Date(iso + 'T12:00:00Z'));
const countryName = country => new Intl.DisplayNames([t.locale], {type:'region'}).of(country);
const today = () => new Intl.DateTimeFormat('sv-SE', {timeZone:'America/Sao_Paulo', year:'numeric', month:'2-digit', day:'2-digit'}).format(new Date());
const calendar = () => data.seminars.toSorted((a,b) => a[0].localeCompare(b[0]));
const dateLabel = date => localizedDate(date, {day:'numeric',month:'long',year:'numeric'});
const nextEvent = () => calendar().find(row => row[0] >= today() && row[1] && !['pending','recommended','proposed'].includes(row[5]));
function currentFlyer(next) {
  const banner = data.weeklyBanner;
  if (!next || banner?.date !== next[0] || !banner.image) return '';
  return `<img src="${esc(banner.image)}" alt="${esc(banner.alt?.[state.lang] || t.flyer)}" width="1600" height="900">`;
}

const newsItems = () => [...data.news, ...archive.news];
const featuredNews = {
  pt:'LAFMAT na China: fortalecendo a cooperação científica internacional',
  en:'LAFMAT in China: strengthening international scientific cooperation',
  es:'LAFMAT en China: fortaleciendo la cooperación científica internacional'
};

function home() {
  const next = nextEvent();
  const item = newsItems()[0];
  const newsTitle = item?.title === archive.news[0]?.title ? featuredNews[state.lang] : item?.title;
  const date = next ? dateLabel(next[0]) : '';
  const flyer = currentFlyer(next);
  return `<section class="hero">
    <div class="shell hero-inner">
      <div class="hero-copy">
        <p class="eyebrow"><span></span>${t.region}</p>
        <h1>${t.headline}</h1>
        <p class="hero-intro">${t.hero}</p>
        <div class="actions"><a class="button accent" href="#seminars">${t.agenda} <span aria-hidden="true">→</span></a><a class="button ghost" href="#home/institutional-video"><span aria-hidden="true">▷</span> ${t.watchVideo}</a></div>
      </div>
      <div class="hero-art" aria-hidden="true"><div class="orbital orbital-a"></div><div class="orbital orbital-b"></div><div class="orbital orbital-c"></div><div class="orbital orbital-d"></div><div class="orbital orbital-e"></div><i></i><i></i><i></i><i></i><i></i><div class="hero-mark"><img src="assets/logo.png" alt=""></div></div>
    </div>
  </section>
  <div class="shell">
    <section class="highlights" aria-label="${esc(t.next + ' · ' + t.latest)}">
      <a href="#seminars" class="highlight">
        <span class="highlight-icon" aria-hidden="true">▦</span>
        <span><span class="kicker">${t.next}${date ? ' · '+esc(date) : ''}</span><strong>${esc(next ? next[2] || next[1] : t.noUpcoming)}</strong>${next ? `<span class="secondary">${esc(next[1])}</span>` : ''}</span><span class="arrow" aria-hidden="true">→</span>
      </a>
      ${item ? `<a href="#news/item-0" class="highlight"><span class="highlight-icon" aria-hidden="true">▤</span><span><span class="kicker">${t.latest}</span><strong>${esc(newsTitle)}</strong></span><span class="arrow" aria-hidden="true">→</span></a>` : ''}
    </section>
    ${flyer ? `<a class="home-flyer" href="#seminars">${flyer}</a>` : ''}
    <section class="about section" id="about"><div><h2>${t.about}</h2>${paragraphs(state.lang === 'en' ? archive.homeEnglish : t.aboutText)}</div>
      <div id="institutional-video" tabindex="-1"><h3>${t.watchVideo}</h3><video controls playsinline preload="metadata" src="assets/lafmat.mp4" aria-label="${t.watchVideo}"></video></div>
    </section>
    <section class="section"><h2>${t.institutions}</h2>
      <div class="institutions">${Object.entries(data.institutions).map(([code,lines])=>`<article><h3>${esc(countryName(code))}</h3><ul>${lines.map(line=>`<li>${esc(line)}</li>`).join('')}</ul></article>`).join('')}</div>
    </section>
    <section class="section sponsors"><h2>${t.sponsors}</h2>${archive.sponsor ? `<img src="${esc(archive.sponsor)}" alt="${t.sponsors}" loading="lazy">` : ''}</section>
  </div>`;
}

function memberCard([country,name,affiliation,index]) {
  const bio = archive.bios[index];
  const initials = name.split(' ').slice(0,2).map(part=>part[0]).join('');
  return `<article class="member card">
    ${bio?.image ? `<img class="avatar" src="${esc(bio.image)}" alt="" loading="lazy">` : `<span class="avatar initials" aria-hidden="true">${esc(initials)}</span>`}
    <div class="member-data"><span class="kicker">${esc(index === '0' ? t.president : countryName(country))}</span><h3>${esc(name)}</h3><p>${esc(affiliation)}</p></div>
    ${bio ? `<details><summary>${t.biography}</summary>${paragraphs(bio.lines)}</details>` : ''}
  </article>`;
}
function memberResults() {
  const query = normalized(state.memberQuery.trim());
  const matches = ([country,name,affiliation]) => (!state.country || state.country === country) && normalized(name+' '+affiliation).includes(query);
  for (const [id,people] of [['member-results',data.members],['collaborator-results',collaborators]]) {
    document.getElementById(id).innerHTML = people.filter(matches).map(memberCard).join('') || `<p>${t.none}</p>`;
  }
}
function members() {
  const countries = [...new Set([...data.members,...collaborators].map(row=>row[0]))].sort((a,b)=>countryName(a).localeCompare(countryName(b), t.locale));
  return `<div class="shell inner">${pageTitle(t.nav[1],t.memberIntro)}
    <div class="filters"><label>${t.filterMembers}<input id="member-search" type="search" value="${esc(state.memberQuery)}"></label>
    <label>${t.filterCountry}<select id="country-filter"><option value="">${t.countries}</option>${countries.map(code=>`<option value="${code}"${code === state.country ? ' selected' : ''}>${esc(countryName(code))}</option>`).join('')}</select></label></div>
    <h2>${t.reps}</h2><div class="member-grid" id="member-results"></div>
    <section class="section"><h2>${t.collaborators}</h2><div class="member-grid" id="collaborator-results"></div></section>
  </div>`;
}

function galleryResults() {
  const query = normalized(state.galleryQuery.trim());
  const rows = videoGallery.groups.filter(item=>
    (state.year === 'all' || item.year === state.year) &&
    (!state.galleryChannel || item.sources.some(source=>source.channelId === state.galleryChannel)) &&
    normalized([item.title,item.publishedDate,...item.sources.map(source=>source.channelName)].join(' ')).includes(query));
  document.querySelector('#gallery-results').innerHTML = rows.slice(0,state.galleryLimit).map(item=>`<article class="record card">
    <a class="video-preview" href="${esc(item.sources.find(source=>source.channelId === state.galleryChannel)?.url || item.url)}" target="_blank" rel="noopener noreferrer" aria-label="${esc(t.video+': '+item.title)}"><img src="${esc(item.image)}" alt="" width="320" height="180" loading="lazy"></a>
    <div class="card-body"><p class="kicker">${t.published} ${dateLabel(item.publishedDate)}</p><h2>${esc(item.title)}</h2>
    <p class="video-channels">${esc([...new Set(item.sources.map(source=>source.channelName))].join(' · '))}</p>
    <div class="video-links">${item.sources.filter(source=>!state.galleryChannel || source.channelId === state.galleryChannel).map(source=>external(source.url,t.video+' · '+source.channelName)).join('')}</div></div></article>`).join('') || `<p>${t.none}</p>`;
  document.querySelector('#gallery-count').textContent = rows.length+' '+(rows.length === 1 ? t.videoResult : t.videoResults);
  document.querySelector('#gallery-more').hidden = rows.length <= state.galleryLimit;
}
function gallery() {
  return `<div class="shell inner">${pageTitle(t.nav[2],t.galleryIntro)}
    <div class="video-source-links">${videoCatalog.channels.map(channel=>external(channel.url,channel.name)).join('')}</div>
    <div class="year-nav" aria-label="${t.year}">${['all',...videoGallery.years].map(year=>`<a href="#gallery${year === 'all' ? '' : '/'+year}"${year === state.year ? ' aria-current="page"' : ''}>${year === 'all' ? t.allVideos : year}</a>`).join('')}</div>
    <div class="filters gallery-tools"><label>${t.searchGallery}<input id="gallery-search" type="search" value="${esc(state.galleryQuery)}"></label>
    <label>${t.videoChannel}<select id="gallery-channel"><option value="">${t.allChannels}</option>${videoCatalog.channels.map(channel=>`<option value="${esc(channel.id)}"${state.galleryChannel === channel.id ? ' selected' : ''}>${esc(channel.name)}</option>`).join('')}</select></label></div>
    <p id="gallery-count" role="status" aria-live="polite"></p>
    <div class="gallery-grid" id="gallery-results"></div><div class="gallery-more"><button class="button outline" id="gallery-more" type="button">${t.loadMore}</button></div>
  </div>`;
}

function news(article) {
  const items = newsItems();
  return `<div class="shell inner">${pageTitle(t.nav[3],t.newsIntro)}
    <div class="news-layout"><div class="news-list">
    ${items.map((item,index)=>`<article class="card card-body" id="item-${index}" tabindex="-1"><p class="kicker">${esc(item.date)}</p><h2>${esc(item.title)}</h2>
      ${item.image ? `<img class="news-photo" src="${esc(item.image)}" alt="${esc(item.imageAlt?.[state.lang])}" loading="lazy">` : ''}
      <details${article === 'item-'+index ? ' open' : ''}><summary>${t.read}</summary>${paragraphs(item.lines || [])}${(item.links || []).map(([label,url])=>external(url,label)).join(' ')}</details>
    </article>`).join('')}
    </div><aside class="card card-body article-search"><h2>${t.articleSearch}</h2><p>${t.articleHelp}</p>
    <form id="article-form" action="https://scholar.google.com/scholar" method="get" target="_blank" rel="noopener noreferrer">
      <label>${t.chooseMember}<select name="q" required><option value="">—</option>${data.members.toSorted((a,b)=>a[1].localeCompare(b[1],t.locale)).map(([,name,affiliation])=>`<option value="${esc('"'+name+'" "'+affiliation+'"')}">${esc(name)}</option>`).join('')}</select></label>
      <button class="button primary" type="submit">${t.openSearch} <span aria-hidden="true">↗</span></button>
    </form><p class="secondary">${t.searchPreview}</p>
    ${data.publications.map(({title,url})=>external(url,title)).join(' ')}
    </aside></div></div>`;
}

function eventMarkup([date,speaker,title,affiliation,moderator,status,host]) {
  const special = !speaker;
  return `<li class="event"><time datetime="${date}"><strong>${date.slice(8)}</strong><span>${esc(localizedDate(date,{month:'short'}))}</span></time>
    <div><h3>${esc(special ? t.status[status] : title || speaker)}</h3>
    ${speaker && title ? `<p><strong>${esc(speaker)}</strong></p>` : ''}
    ${affiliation ? `<p>${esc(affiliation)}</p>` : ''}
    ${speaker && !title ? `<p class="secondary">${t.noTitle}</p>` : ''}
    ${moderator ? `<p>${t.moderator}: ${esc(moderator)}</p>` : ''}
    ${host ? `<p>${status === 'recommended' ? t.recommendedBy : t.invitedBy}: ${esc(host)}</p>` : ''}
    ${status === 'reserved' ? `<p>${t.forum}</p>` : ''}
    ${status && !special && ['pending','proposed'].includes(status) ? `<span class="status">${t.status[status]}</span>` : ''}
    </div></li>`;
}
function upcomingSchedule() {
  const start = today();
  const groups = {};
  for (const row of calendar()) {
    if (row[0] >= start) (groups[row[0].slice(0,7)] ||= []).push(row);
  }
  return Object.entries(groups).map(([month,rows])=>`<section class="month"><h3>${esc(localizedDate(month+'-01',{month:'long',year:'numeric'}))}</h3><ul>${rows.map(eventMarkup).join('')}</ul></section>`).join('') || `<p>${t.noUpcoming}</p>`;
}
function seminars() {
  const next = nextEvent();
  const flyer = currentFlyer(next);
  return `<div class="shell inner">${pageTitle(t.nav[4])}
    ${next ? `<section class="seminar-feature${flyer ? ' has-flyer' : ''}">
      <div><p class="kicker">${t.next} · <time datetime="${next[0]}">${esc(dateLabel(next[0]))}</time></p>
      <h2>${esc(next[2] || next[1])}</h2>
      <p>${esc([next[2] && next[1],next[3]].filter(Boolean).join(' · '))}</p>
      ${next[4] ? `<p>${t.moderator}: ${esc(next[4])}</p>` : ''}
      ${external(data.youtube,t.watch,'button accent')}</div>
      ${flyer}
    </section>` : ''}
    <div class="seminar-intro"><div>${paragraphs(state.lang === 'en' ? archive.seminarEnglish : t.seminarIntro)}<div class="actions">${external(data.youtube,t.watch,'button primary')}<a href="#gallery" class="button outline">${t.nav[2]}</a></div></div>
    <aside class="card card-body"><h2>${t.times}</h2><dl class="times">${['07:30','08:30','09:30','10:30'].map((time,i)=>`<div><dt>${time}</dt><dd>${t.timeRegions[i]}</dd></div>`).join('')}</dl></aside></div>
    <section class="section"><h2>${t.future}</h2>${upcomingSchedule()}</section>
  </div>`;
}
function conferences() {
  return `<div class="shell inner">${pageTitle(t.nav[5],t.confIntro)}
  <div class="actions">${data.conferences.map(edition=>`<a class="button primary" href="${esc(edition.url)}" target="_blank" rel="noopener noreferrer">${edition.year === 2023 ? t.conf2023 : esc(edition.year)}</a>`).join('')}</div></div>`;
}
function contact() {
  const {name,email,phone,tel} = data.contact;
  return `<div class="shell inner">${pageTitle(t.nav[6])}
  <div class="contact-layout">
    <article class="card card-body"><h2>${esc(name)}</h2><p>${t.contactRole}</p><p><a href="mailto:${esc(email)}">${esc(email)}</a></p><p><a href="tel:${esc(tel)}">${esc(phone)}</a></p></article>
    <form id="contact-form" class="card card-body"><h2>${t.write}</h2><p id="contact-hint">${t.formHint}</p>
      <label>${t.name}<input name="name" autocomplete="name" maxlength="100" required></label>
      <label>${t.email}<input type="email" name="email" autocomplete="email" maxlength="180" required></label>
      <label>${t.subject}<input name="subject" maxlength="120" required></label>
      <label>${t.message}<textarea name="message" rows="6" maxlength="1800" required></textarea></label>
      <button class="button primary" type="submit" aria-describedby="contact-hint">${t.send}</button>
    </form>
  </div></div>`;
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
  t = languages[state.lang];
  const [requested, sub] = location.hash.slice(1).split('/');
  const route = routes.includes(requested) ? requested : 'home';
  const galleryYear = videoGallery.years.includes(sub) ? sub : 'all';
  if (route === 'gallery' && galleryYear !== state.year) {
    state.year = galleryYear;
    state.galleryQuery = '';
    state.galleryLimit = 24;
  }
  currentRoute = route;
  document.documentElement.lang = t.locale;
  document.title = route === 'home' ? 'LAFMAT · '+t.footer : t.nav[routes.indexOf(route)]+' · LAFMAT';
  document.querySelector('#skip').textContent = t.skip;
  menu.setAttribute('aria-label',t.menu);
  nav.setAttribute('aria-label',t.menu);
  document.querySelector('.languages').setAttribute('aria-label',t.language);
  nav.innerHTML = routes.map((path,i)=>path === 'conferences'
    ? `<div class="nav-dropdown"><button type="button" class="conference-toggle${route === path ? ' current' : ''}" aria-expanded="false" aria-controls="conference-years">${t.nav[i]} <span aria-hidden="true">⌄</span></button><ul id="conference-years" class="nav-submenu" hidden>${data.conferences.map(edition=>`<li><a href="${esc(edition.url)}" target="_blank" rel="noopener noreferrer">${esc(edition.year)}</a></li>`).join('')}</ul></div>`
    : `<a href="#${path}"${path === route ? ' aria-current="page"' : ''}>${t.nav[i]}</a>`).join('');
  document.querySelectorAll('[data-lang]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.lang === state.lang)));
  const views = {home,members,gallery,news,seminars,conferences,contact};
  main.innerHTML = views[route](sub);
  document.querySelector('footer').innerHTML = `<div class="shell footer-inner"><div><a href="#home" class="footer-brand">LAFMAT</a><p>${t.footer}</p></div><div>${external(data.youtube,'YouTube')}</div></div>`;
  if (route === 'members') memberResults();
  if (route === 'gallery') galleryResults();
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
document.querySelector('.languages').addEventListener('click',event=>{
  const button = event.target.closest('[data-lang]');
  if (!button || button.dataset.lang === state.lang) return;
  const draft = currentRoute === 'contact' ? new FormData(document.querySelector('#contact-form')) : null;
  state.lang = button.dataset.lang;
  try { localStorage.setItem('lafmat-language',state.lang); } catch {}
  render();
  if (draft) for (const [name,value] of draft) document.querySelector('#contact-form').elements.namedItem(name).value = value;
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
render();
