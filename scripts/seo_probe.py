"""Read-only bounded HTTP baseline for the local SEO inventory (run at repo root)."""
import csv,json,concurrent.futures,urllib.request,urllib.error
from urllib.parse import urljoin,urlsplit,quote,urlunsplit
from html.parser import HTMLParser
from pathlib import Path
class Meta(HTMLParser):
 def __init__(self):super().__init__();self.meta={};self.title=False;self.text=''
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='meta' and a.get('name') in ('robots','description'):self.meta[a['name']]=a.get('content','')[:200]
  if t=='meta' and a.get('http-equiv','').lower()=='refresh':self.meta['refresh']=a.get('content','')
  if t=='link' and a.get('rel')=='canonical':self.meta['canonical']=a.get('href')
  if t=='title':self.title=True
 def handle_endtag(self,t):
  if t=='title':self.title=False
 def handle_data(self,d):
  if self.title:self.text+=d
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*a,**k):return None
opener=urllib.request.build_opener(NoRedirect)
rs=list(csv.DictReader(open('docs/seo/url-inventory.csv')))
urls={r['url'] for r in rs if 'legacy_page' in r['kind'] or 'legacy_post' in r['kind']}
urls.update(['http://lafmat.com/','https://www.lafmat.com/','https://lafmat.com/','https://lafmat.com/robots.txt','https://lafmat.com/sitemap.xml','https://lafmat.com/wp-sitemap.xml','https://lafmat.com/home/wp-sitemap.xml','https://lafmat.com/home/sitemap_index.xml','https://lafmat.com/seo-check-nonexistent-20261123','https://lafmat.com/verification.json','https://lafmat.com/assets/debora-vasconcelos-2026-11-28.jpg'])
# A bounded sample of historic media and query URLs, not a mass crawl of media.
urls.update(r['url'] for r in [r for r in rs if 'legacy_query_alias' in r['kind']][:3])
urls.update(r['url'] for r in [r for r in rs if 'legacy_media' in r['kind']][:5])
def probe(url):
 out={'url':url,'hops':[]};current=url
 try:
  for step in range(6):
   p=urlsplit(current);encoded=urlunsplit((p.scheme,p.netloc,quote(p.path,safe='/%:@'),p.query,''))
   try:r=opener.open(urllib.request.Request(encoded,headers={'User-Agent':'LAFMAT-SEO-inventory/1.0'}),timeout=20)
   except urllib.error.HTTPError as e:r=e
   with r:
    status=r.code;loc=r.headers.get('Location');out['hops'].append({'url':current,'status':status,**({'location':loc} if loc else {})})
    if status in (301,302,303,307,308) and loc:
     current=urljoin(current,loc)
     if urlsplit(current).hostname not in ('lafmat.com','www.lafmat.com'):break
     continue
    out.update({'final_url':current,'final_status':status,'content_type':r.headers.get('Content-Type'),'x_robots_tag':r.headers.get('X-Robots-Tag')})
    if 'text/html' in r.headers.get('Content-Type',''):
     parser=Meta();parser.feed(r.read(1048576).decode('utf8',errors='replace'));out['html']=parser.meta;out['title']=parser.text
    break
 except Exception as e:out['error']=type(e).__name__
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=sorted(pool.map(probe,urls),key=lambda x:x['url'])
Path('docs/seo/http-baseline-2026-11-23.json').write_text(json.dumps({'checked_date':'2026-11-23','method':'GET with TLS verification; up to 6 redirects, bounded metadata inspection, no login','results':results},ensure_ascii=False,indent=2)+'\n')
statuses={r['url']:str(r.get('final_status','ERROR')) for r in results}
for file in ['url-inventory.csv','redirect-map.csv']:
 path=Path('docs/seo')/file;data=list(csv.DictReader(path.open()));fields=list(data[0])
 for row in data:row['http_status']=statuses.get(row['url'],'NOT_CHECKED')
 with path.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(data)
from collections import Counter
print('Checked',len(results),'URLs; final statuses',dict(Counter(str(x.get('final_status','ERROR')) for x in results)))
for r in results:
 if '/wp-content/uploads/' not in r['url']:print(r['url'],r.get('final_status'),r.get('html',{}).get('robots',''),r.get('html',{}).get('refresh',''))
