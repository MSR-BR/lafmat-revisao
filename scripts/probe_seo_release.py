"""Bounded, read-only HEAD checks of known LAFMAT migration URLs over normal TLS."""
import argparse
import csv
import json
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--base', default='https://lafmat.com')
parser.add_argument('--output', required=True)
parser.add_argument('--workers', type=int, default=4, choices=range(1,5))
args = parser.parse_args()
base = urlsplit(args.base)
if base.scheme != 'https' or base.hostname not in ('lafmat.com','www.lafmat.com'):
    raise SystemExit('This public probe is restricted to the authorized LAFMAT production hosts over TLS')

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        return None

stop = threading.Event()
rows = list(csv.DictReader((ROOT/'docs/seo/url-inventory.csv').open()))
# Add new routes/SEO utilities and explicit normalization/negative cases.
extra = [page['path'] for page in json.loads((ROOT/'docs/seo/static-build.json').read_text())['pages']]
extra += ['/robots.txt','/sitemap.xml','/assets/lafmat-social.png','/not-a-real-lafmat-page/','/members','/members/index.html','/home/?page_id=37000','/home/seminars/index.html','/home/program/index.html']
urls = list(dict.fromkeys([row['url'] for row in rows] + ['https://lafmat.com'+path for path in extra]))

def request_head(url):
    opener = build_opener(NoRedirect)
    req = Request(url,method='HEAD',headers={'User-Agent':'LAFMAT-owner-migration-validation/1.0'})
    try:
        response = opener.open(req,timeout=20)
    except HTTPError as error:
        response = error
    headers = response.headers
    result = {'status':response.code,'location':headers.get('Location'),'content_type':headers.get('Content-Type'),'canonical_header':headers.get('Link'),'robots_header':headers.get('X-Robots-Tag'),'security_mitigation':headers.get('x-vercel-mitigated')}
    response.close()
    if result['status'] == 429 or result['security_mitigation'] == 'challenge':
        stop.set()
    return result

def check(original):
    if stop.is_set():
        return {'url':original,'error':'SKIPPED_RATE_LIMIT'}
    source = urlsplit(original)
    path = quote(source.path,safe='/%:@!$&\'()*+,;=-._~')
    url = urlunsplit((base.scheme,base.netloc,path,source.query,''))
    result = {'url':original,'requested':url,'fragment_not_sent':bool(source.fragment),'chain':[]}
    try:
        for _ in range(6):
            response = request_head(url)
            result['chain'].append({'url':url,**response})
            if response['status'] not in (301,302,303,307,308) or not response['location']:
                break
            target = urljoin(url,response['location'])
            parsed = urlsplit(target)
            if parsed.scheme != 'https' or parsed.hostname not in ('lafmat.com','www.lafmat.com'):
                raise ValueError('Unexpected redirect host/protocol; not followed')
            if any(step['url'] == target for step in result['chain']):
                raise ValueError('Redirect loop')
            url = target
        else:
            raise ValueError('More than five redirects')
        result['final_status'] = result['chain'][-1]['status']
        result['final_url'] = result['chain'][-1]['url']
    except (URLError, ValueError, TimeoutError, OSError) as error:
        # Never log request headers, cookies, credentials or page content.
        result['error'] = type(error).__name__+': '+str(error)[:160]
    time.sleep(.10)
    return result

with ThreadPoolExecutor(max_workers=args.workers) as pool:
    results = list(pool.map(check,urls))
summary = {'base':args.base,'method':'HEAD; normal certificate validation; <=4 workers; no retries; stop on 429 or Vercel security challenge','urls':len(results),'status_counts':dict(Counter(str(row.get('final_status','ERROR')) for row in results)),'first_status_counts':dict(Counter(str((row.get('chain') or [{}])[0].get('status','ERROR')) for row in results)),'errors':sum('error' in row for row in results),'rate_limit_or_security_challenge_seen':stop.is_set()}
output = ROOT/args.output
output.parent.mkdir(exist_ok=True,parents=True)
output.write_text(json.dumps({'summary':summary,'results':results},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
raise SystemExit(1 if summary['errors'] or stop.is_set() else 0)
