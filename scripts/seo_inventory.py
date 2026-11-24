"""Build a local SEO inventory from public URL metadata; never export WXR bodies."""
import csv, hashlib, html, json, re, subprocess
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit, unquote, parse_qsl, urlencode
ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
OUT = ROOT / 'docs/seo'
PRIVATE = ROOT / '.private-backups/wordpress-2026-11-19'
NS = {'wp':'http://wordpress.org/export/1.2/', 'content':'http://purl.org/rss/1.0/modules/content/'}
records = {}
def add(url, source, kind):
    url = html.unescape(url.strip())
    try:
        p = urlsplit(url)
        if p.username or p.password or '@' in p.path: return
        if p.scheme not in ('http','https') or p.hostname not in ('lafmat.com','www.lafmat.com'):
            return
        if any(x in p.path for x in ('wp-admin','wp-login','xmlrpc')): return
        query = parse_qsl(p.query, keep_blank_values=True)
        if any(k not in ('p','page_id','attachment_id','year') for k,v in query): return
        path = p.path or '/'
        if any(c in path for c in '\\<>[]{}'):return
        fragment = p.fragment if path == '/' and p.fragment in ('home','members','gallery','news','seminars','conferences','contact') else ''
        normalized = urlunsplit(('https','lafmat.com',path,urlencode(query),fragment))
    except ValueError:return
    row = records.setdefault(normalized, {'url':normalized,'sources':set(),'kinds':set()})
    row['sources'].add(source); row['kinds'].add(kind)
class Links(HTMLParser):
    def __init__(self, base, source):super().__init__();self.base=base;self.source=source
    def handle_starttag(self, tag, attrs):
        for k,v in attrs:
            if k in ('href','src','poster') and v:
                add(urljoin(self.base,v),self.source,'internal_reference')
manifest=json.loads((DIST/'verification.json').read_text())
sha_paths={}
for path,digest in manifest['files'].items():sha_paths.setdefault(digest,[]).append(path)
for p in sorted(DIST.rglob('*')):
    if not p.is_file() or p.name in ('.DS_Store','CNAME','.nojekyll'):continue
    rel=p.relative_to(DIST).as_posix()
    path='/' + (rel[:-10] if rel.endswith('index.html') else rel)
    add('https://lafmat.com'+path,'dist:'+rel,'current_html' if p.suffix=='.html' else 'current_resource')
    if p.suffix=='.html':Links('https://lafmat.com'+path,'dist-links:'+rel).feed(p.read_text())
items=ET.parse(PRIVATE/'wordpress-content.xml').getroot().findall('./channel/item')
public_items=[];attachments=[];wpids={}
for item in items:
    kind=item.findtext('wp:post_type',namespaces=NS);status=item.findtext('wp:status',namespaces=NS)
    ident=item.findtext('wp:post_id',namespaces=NS)
    if kind in ('page','post') and status=='publish':
        link=item.findtext('link')
        add(link,'WXR:published:'+ident, 'legacy_'+kind);public_items.append((ident,link))
        wpids[ident]=link
        add('https://lafmat.com/home/?'+urlencode({'page_id' if kind=='page' else 'p':ident}),'WXR:query-alias:'+ident,'legacy_query_alias')
        content=item.findtext('content:encoded',default='',namespaces=NS)
        Links(link,'WXR:published-links:'+ident).feed(content)
        for match in re.findall(r'https?://(?:www\.)?lafmat\.com/[^\s<>"\]\[\'}]+',content):
            add(match.rstrip('.,;'),'WXR:published-links:'+ident,'internal_reference')
    elif kind=='attachment':
        link=item.findtext('link');media=item.findtext('wp:attachment_url',namespaces=NS)
        if link:add(link,'WXR:attachment-link:'+ident,'legacy_attachment_page')
        if media:add(media,'WXR:attachment-url:'+ident,'legacy_media');attachments.append(media)
for row in json.loads((PRIVATE/'media-backup-validation.json').read_text()):
    add(row['url'],'backup:public-media-url','legacy_media')
media_hash={urlsplit(r['url']).path:r['sha256'] for r in json.loads((PRIVATE/'media-backup-validation.json').read_text())}
# Preserve known hash entry links separately from server-side URLs.
for route in ['home','members','gallery','news','seminars','conferences','contact']:
    add('https://lafmat.com/#'+route,'site.js:routes','current_hash_view')
conference=json.loads((ROOT/'docs/conference-2023-inventory.json').read_text())
conf_map={urlsplit(p['source']).path:'/'+p['output'].removesuffix('index.html') for p in conference['pages']}
known={'/home/':'/','/home/know-us/':'/#members','/home/about-us/':'/#home','/home/contacts/':'/#contact','/home/seminars/':'/#seminars','/home/video-gallery/':'/#gallery','/home/__trashed/':'/#news','/home/conferences/':'/#conferences'}
proposed={'/#home':'/','/#members':'/members/','/#contact':'/contact/','/#seminars':'/seminars/','/#gallery':'/videos/','/#news':'/news/','/#conferences':'/conferences/'}
fields=['url','kind','sources','classification','current_equivalent','proposed_destination','destination_state','priority','language','evidence','reason','http_status']
rows=[]
for url,r in sorted(records.items()):
    p=urlsplit(url);path=unquote(p.path);kinds=r['kinds'];dest='';future='';state='REVIEW_REQUIRED';action='review_required';evidence='source_metadata_only';reason='Sem equivalência comprovada; revisar antes do release, não redirecionar genericamente nem remover.'
    local=DIST/path.lstrip('/')
    if path.endswith('/'):local=local/'index.html'
    current=local.is_file()
    if p.query:
        params=dict(parse_qsl(p.query));ident=params.get('page_id',params.get('p'))
        if ident in wpids:
            oldpath=urlsplit(wpids[ident]).path;dest=known.get(oldpath,conf_map.get(oldpath,''));future=proposed.get(dest,dest)
            state='CURRENT_HASH_TARGET' if '#' in dest else ('CURRENT_LOCAL_TARGET' if dest else 'REVIEW_REQUIRED')
            action='redirect' if dest else 'review_required';reason='Alias WordPress conhecido por ID; confirmar equivalência e regra de query antes de publicar.'
    elif p.fragment:
        if p.fragment in ['home','members','gallery','news','seminars','conferences','contact']:
            dest=url;future=proposed.get('/#'+p.fragment,'/');state='PROPOSED_ROUTE_NOT_IMPLEMENTED';action='consolidate';reason='Vista cliente por hash; preservar compatibilidade e gerar URL real no Change 003.'
    elif path in known:
        dest='https://lafmat.com'+known[path];future=proposed.get(known[path],known[path]);state='CURRENT_HASH_TARGET' if '#' in dest else 'CURRENT_LOCAL_TARGET';action='redirect';evidence='local_legacy_alias';reason='Alias atual usa meta refresh/noindex HTTP 200; substituir por redirect permanente no servidor atual.'
    elif path in conf_map:
        dest='https://lafmat.com'+conf_map[path];future=dest;state='CURRENT_LOCAL_TARGET';action='consolidate';evidence='existing_conference_route_ledger';reason='Conteúdo histórico já preservado; somente registrar duplicação. Alterar alias depende de escopo específico, sem reauditar conteúdo.'
    elif 'legacy_media' in kinds or '/wp-content/uploads/' in path:
        matches=sha_paths.get(media_hash.get(path),[])
        if matches:
            dest='https://lafmat.com/'+sorted(matches)[0];future=dest;state='CURRENT_LOCAL_TARGET';action='redirect';evidence='matching_previously_verified_sha256';reason='Mesmo binário identificado no manifesto atual e recibo privado; futuro redirect deve preservar tipo de recurso.'
        else:reason='Mídia antiga sem binário idêntico no manifesto atual; recuperação/seleção editorial pendente. Não publicar backup em massa.'
    elif current:
        dest='https://lafmat.com'+p.path;future=dest;state='CURRENT_LOCAL_TARGET';action='keep';evidence='dist_file_exists';reason='Arquivo atual preservado; HTML recebe revisão de metadados, recurso não vira entrada de sitemap por padrão.'
    if dest.startswith('/') :dest='https://lafmat.com'+dest
    if future.startswith('/'):future='https://lafmat.com'+future
    if path=='/verification.json':action='keep';reason='Manifesto técnico público; manter como utilitário, fora do sitemap.'
    priority='P1' if any(k in kinds for k in ('legacy_page','legacy_post','legacy_query_alias','current_hash_view')) else ('P2' if 'legacy_media' in kinds or 'legacy_attachment_page' in kinds else 'P3')
    if path=='/':priority='P1'
    rows.append(dict(zip(fields,[url,';'.join(sorted(kinds)),';'.join(sorted(r['sources'])),action,dest,future,state,priority,'mixed_or_unverified',evidence,reason,'NOT_CHECKED'])))
OUT.mkdir(exist_ok=True,parents=True)
with (OUT/'url-inventory.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
legacy=[r for r in rows if any(x in r['kind'] for x in ('legacy_','internal_reference','current_hash_view'))]
with (OUT/'redirect-map.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fields,lineterminator='\n');writer.writeheader();writer.writerows(legacy)
summary={'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'manifest':manifest['code'],'current_dist_files':len(manifest['files']),'published_wxr_pages_posts':len(public_items),'attachment_media_records':len(attachments),'inventory_urls':len(rows),'redirect_map_rows':len(legacy),'classification_counts':dict(Counter(r['classification'] for r in rows)),'destination_state_counts':dict(Counter(r['destination_state'] for r in rows)),'coverage_limits':['No Search Console or GA4 account evidence','No traffic/backlink priority measured; priority is structural','WXR exported published metadata may include obsolete pages','Media inherit visibility not independently checked; public URL metadata only','Source snapshots referenced only for route ledger; conference content not reaudited','External domains excluded; wp-admin/login excluded; no WXR bodies/authors/emails exported','Language mixed/unverified; finalize route and locale contract in Change 003']}
(OUT/'inventory-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
