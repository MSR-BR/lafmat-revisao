'use strict';

// The catalog is authoritative for video identity, title, source and publication
// date. The older WordPress gallery stays preserved in archive.js.
window.buildVideoGallery = catalog => {
  const channels = new Map(catalog.channels.map(channel => [channel.id,channel]));
  const normalize = value => value.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase().replace(/[^\p{L}\p{N}]+/gu,' ').trim();
  const seen = new Set();
  const groups = [];
  const keys = new Map();
  for (const video of [...catalog.videos].sort((a,b)=>b.publishedAt.localeCompare(a.publishedAt) || a.id.localeCompare(b.id))) {
    if (seen.has(video.id)) continue;
    seen.add(video.id);
    const channel = channels.get(video.channelId);
    if (!channel || !/^[A-Za-z0-9_-]{11}$/.test(video.id)) continue;
    const titleKey = normalize(video.title);
    const key = video.publishedDate+'|'+titleKey;
    // Only combine exact scientific titles from different channels on the same
    // date. Generic stream titles and uploads from one channel stay separate.
    const generic = /transmision en directo|live stream|live streaming/.test(titleKey) || titleKey.length < 40;
    const match = !generic && (keys.get(key) || []).find(group =>
      !group.sources.some(source=>source.channelId === video.channelId) &&
      Math.abs(group.duration-video.duration) <= Math.max(180,group.duration*.15));
    const source = {id:video.id,channelId:channel.id,channelName:channel.name,url:video.url};
    if (match) {
      match.sources.push(source);
      continue;
    }
    const group = {...video,year:video.publishedDate.slice(0,4),sources:[source]};
    groups.push(group);
    if (!keys.has(key)) keys.set(key,[]);
    keys.get(key).push(group);
  }
  return {groups,years:[...new Set(groups.map(group=>group.year))].sort().reverse()};
};
