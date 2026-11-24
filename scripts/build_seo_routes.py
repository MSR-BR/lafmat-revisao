"""Generate bounded Vercel redirects and a decision for every inventoried URL.

Reads only the public inventory and previously verified route ledger; does not
read or publish private backup content. Unknown resources remain unchanged.
"""
import csv
import html
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
OUT = ROOT / 'docs/seo'
rows = list(csv.DictReader((OUT / 'url-inventory.csv').open()))
conference = json.loads((ROOT / 'docs/conference-2023-inventory.json').read_text())
destinations = {
    '/home/': '/', '/home/know-us/': '/members/', '/home/about-us/': '/',
    '/home/contacts/': '/contact/', '/home/seminars/': '/seminars/',
    '/home/video-gallery/': '/videos/', '/home/__trashed/': '/news/',
    '/home/conferences/': '/conferences/',
    '/home/video-galery-2022/': '/videos/2022/',
    '/home/video-gallery-2023/': '/videos/2023/',
    '/home/video-galery-2024/': '/videos/2024/',
    '/home/video-gallery-2025-2/': '/videos/2025/',
    '/home/video-gallery-2026/': '/videos/2026/',
}
# Authorized explicitly on 24/11/2026: consolidate these 11 aliases only.
for page in conference['pages']:
    destinations[urlsplit(page['source']).path] = '/' + page['output'].removesuffix('index.html')
for row in rows:
    if row['evidence'] == 'matching_previously_verified_sha256':
        source = urlsplit(row['url']).path
        target = urlsplit(row['proposed_destination']).path
        if source != target:
            destinations[source] = target

def local_file(path):
    p = DIST / unquote(path).lstrip('/')
    return p / 'index.html' if path.endswith('/') else p

def source_pattern(path):
    # Path-to-regexp literals: dots/hyphens are literal already.
    return re.sub(r'([():*+?{}\[\]\\])', r'\\\1', path)

redirects = []
query_destinations = {}
for row in rows:
    if 'legacy_query_alias' not in row['kind']:
        continue
    params = parse_qs(urlsplit(row['url']).query)
    key = next(key for key in ('p', 'page_id') if key in params)
    ident = params[key][0]
    original = next(r for r in rows if 'WXR:published:' + ident in r['sources'].split(';'))
    old_path = urlsplit(original['url']).path
    # When no equivalent exists, preserve its existing missing-page outcome;
    # do not send it to a successful unrelated home page.
    target = destinations.get(old_path, old_path)
    query_destinations[(key, ident)] = target
    for base in ('/home/', '/home/index.html'):
        redirects.append({'source':base, 'has':[{'type':'query','key':key,'value':'^'+ident+'$'}], 'destination':target, 'permanent':True})

for old, new in sorted(destinations.items()):
    item = {'source':source_pattern(old), 'destination':new, 'permanent':True}
    if old == '/home/':
        item['missing'] = [{'type':'query','key':key} for key in ('p','page_id','attachment_id')]
    redirects.append(item)
    if old.endswith('/'):
        redirects.append({**item, 'source':source_pattern(old+'index.html')})
redirects.extend([
    {'source':'/index.html','destination':'/','permanent':True},
    {'source':'/:path*/index.html','destination':'/:path*/','permanent':True},
])

headers = [
    {'source':'/:path*','headers':[{'key':'X-Content-Type-Options','value':'nosniff'},{'key':'Referrer-Policy','value':'strict-origin-when-cross-origin'}]},
    {'source':'/:path*','has':[{'type':'host','value':r'(?!lafmat\.com$).*'}], 'headers':[{'key':'X-Robots-Tag','value':'noindex, nofollow'}]},
    {'source':'/verification.json','headers':[{'key':'X-Robots-Tag','value':'noindex'}]},
    {'source':'/404.html','headers':[{'key':'X-Robots-Tag','value':'noindex'}]},
]
archive_entries = []
for file in [DIST / 'conferences/2023/index.html'] + [DIST / page['output'] for page in conference['pages']]:
    canonical_path = '/' + file.relative_to(DIST).as_posix().removesuffix('index.html')
    # Header canonical covers the existing HTML without touching its content.
    for request_path in (canonical_path, canonical_path+'index.html'):
        headers.append({'source':request_path,'headers':[{'key':'Link','value':'<https://lafmat.com'+canonical_path+'>; rel="canonical"'}]})
    archive_entries.append({'path':canonical_path,'file':file.relative_to(DIST).as_posix()})

config = {'$schema':'https://openapi.vercel.sh/vercel.json','trailingSlash':True,'redirects':redirects,'headers':headers}
(DIST / 'vercel.json').write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
(OUT / 'archive-canonical-routes.json').write_text(json.dumps(archive_entries,indent=2)+'\n')

decisions = []
for row in rows:
    parsed = urlsplit(row['url'])
    path = parsed.path
    target = ''
    reason = ''
    if parsed.fragment:
        target = {'home':'/','gallery':'/videos/'}.get(parsed.fragment,'/'+parsed.fragment+'/')
        behavior = 'CLIENT_HASH_COMPATIBILITY'
        reason = 'Fragment is not sent to HTTP; browser normalizes to the real route; without JS home navigation stays usable.'
    elif parsed.query:
        params = parse_qs(parsed.query)
        pair = next(((key,params[key][0]) for key in ('p','page_id') if key in params),None)
        target = query_destinations.get(pair,'')
        behavior = 'REDIRECT_EQUIVALENT' if target and local_file(target).is_file() else 'REDIRECT_TO_EXISTING_MISSING_PATH'
        reason = 'Known WordPress ID mapped to its own page intent; query forwarding must be verified on Vercel; no generic home fallback.'
    elif path in destinations:
        behavior = 'REDIRECT_EQUIVALENT'
        target = destinations[path]
        reason = 'Known section/year, approved conference alias, or previously verified identical binary.'
    elif local_file(path).is_file():
        behavior = 'KEEP_FILE'
        target = path
        reason = 'Existing public file preserved; resources excluded from sitemap; archive canonical supplied by HTTP header.'
    elif 'legacy_attachment_page' in row['kind']:
        behavior = 'EXCEPTION_KEEP_MISSING_ATTACHMENT_PAGE'
        reason = 'Already absent before this release; no HTML equivalent. No recovery, deletion, 410, or home redirect authorized/introduced.'
    elif 'legacy_media' in row['kind'] or '/wp-content/uploads/' in path:
        behavior = 'EXCEPTION_KEEP_UNMIGRATED_MEDIA'
        reason = 'No identical public binary established. Preserve existing 403/404 outcome; private backups not published. Recovery remains separate content work.'
    elif 'legacy_page' in row['kind'] or 'legacy_post' in row['kind']:
        behavior = 'EXCEPTION_KEEP_UNMAPPED_PAGE'
        reason = 'No equivalent content established in approved new site; retain existing 404 rather than claim a false migration or restore old forms/templates.'
    else:
        behavior = 'EXCEPTION_KEEP_MISSING_REFERENCE'
        reason = 'Historic internal reference, not a current required file; retain existing missing response; no substitute proved.'
    decisions.append({'url':row['url'],'kind':row['kind'],'behavior':behavior,'destination':('https://lafmat.com'+target) if target else '', 'reason':reason,'verification':'LOCAL_MODEL_PENDING_HTTP_RELEASE'})
with (OUT / 'migration-decisions.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,decisions[0].keys(),lineterminator='\n');w.writeheader();w.writerows(decisions)
summary={'date':'2026-11-24','inventory_urls':len(rows),'behavior_counts':dict(Counter(row['behavior'] for row in decisions)),'redirect_rules':len(redirects),'canonical_archive_pages':len(archive_entries),'limits':['Exception means an explicitly retained pre-existing missing resource, not recovered content.','HTTP results must be checked against the deployed candidate before claiming public success.','Unknown WordPress IDs are not assigned a made-up destination.','No private backup content is emitted by this generator.']}
(OUT / 'migration-decisions-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
