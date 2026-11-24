"""Check planning inventory coverage, target files, privacy and public HTTP evidence."""
import csv,json
from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'docs/seo'
rows=list(csv.DictReader((base/'url-inventory.csv').open()))
mapping=list(csv.DictReader((base/'redirect-map.csv').open()))
summary=json.loads((base/'inventory-summary.json').read_text())
assert len(rows)==summary['inventory_urls']
assert len({r['url'] for r in rows})==len(rows)
assert len(mapping)==summary['redirect_map_rows']
assert {r['url'] for r in mapping}<={r['url'] for r in rows}
assert Counter(r['classification'] for r in rows)==summary['classification_counts']
assert sum('legacy_page' in r['kind'].split(';') or 'legacy_post' in r['kind'].split(';') for r in rows)==31
assert sum('legacy_media' in r['kind'].split(';') for r in rows)==512
assert sum('legacy_attachment_page' in r['kind'].split(';') for r in rows)==512
for r in rows:
 p=urlsplit(r['url'])
 assert p.scheme=='https' and p.netloc=='lafmat.com' and not p.username
 assert '@' not in unquote(r['url'])
 assert r['sources'] and r['reason'] and r['evidence']
 assert 'wp-admin' not in p.path and 'wp-login' not in p.path
 if r['classification']=='review_required':assert r['destination_state']=='REVIEW_REQUIRED'
 else:assert r['current_equivalent'] and r['proposed_destination']
 if r['destination_state']=='CURRENT_LOCAL_TARGET':
  path=urlsplit(r['current_equivalent']).path
  f=ROOT/'dist'/unquote(path).lstrip('/')
  if path.endswith('/'):f=f/'index.html'
  assert f.is_file(),r['url']
 if r['destination_state']=='PROPOSED_ROUTE_NOT_IMPLEMENTED':assert p.fragment
receipt=json.loads((base/'http-baseline-2026-11-23.json').read_text())
checked=receipt['results'];assert len(checked)==50
by_url={r['url']:r for r in checked}
for r in rows:
 if 'legacy_page' in r['kind'] or 'legacy_post' in r['kind']:assert r['url'] in by_url
assert by_url['https://lafmat.com/']['final_status']==200
assert by_url['http://lafmat.com/']['hops'][0]['status']==308
assert by_url['https://www.lafmat.com/']['hops'][0]['status']==308
assert by_url['https://lafmat.com/seo-check-nonexistent-20261123']['final_status']==404
print('PASS inventory:',len(rows),'unique URLs;',len(mapping),'mapping rows; all 31 published pages/posts and 512 media records covered.')
print('PASS target existence, explicit review reasons, privacy checks and 50-URL HTTP receipt.')
