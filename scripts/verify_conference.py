"""Independent source-parity, local-link and binary checks for the 2023 archive."""
import hashlib,json,re,zipfile
from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent.parent
DIST=ROOT/'dist'
report=json.loads((ROOT/'docs/conference-2023-inventory.json').read_text())
count=0
for page in report['pages']:
 source=ROOT/'sources/conference-2023'/(page['slug']+'.html')
 assert hashlib.sha256(source.read_bytes()).hexdigest()==page['source_sha256']
 s=BeautifulSoup(source.read_text(),'html.parser').select_one('.et_builder_inner_content')
 for menu in s.select('.et_pb_fullwidth_menu,.et_pb_menu'):menu.decompose()
 expected=' '.join(s.get_text(' ',strip=True).split())
 for name in ['output','legacy_path']:
  output=DIST/page[name];d=BeautifulSoup(output.read_text(),'html.parser');m=d.select_one('main')
  actual=' '.join(m.get_text(' ',strip=True).split())
  assert expected==actual,(output,'text mismatch')
  assert len(s.select('img'))==len(m.select('img'))
  assert len(s.select('table'))==len(m.select('table'))
  assert [x.get('src') for x in s.select('iframe')]==[x.get('src') for x in m.select('iframe')]
  assert len(d.select('nav a'))==11
  assert not d.select('form')
  allowed={'/assets/i18n.js','/assets/routes.js','/assets/privacy.js','/assets/analytics-config.js','/assets/analytics-core.js','/assets/analytics.js'}
  for script in d.select('script'):
   assert script.parent==d.head and script.get('src') in allowed and script.has_attr('defer')
  for tag in d.select('[href],[src]'):
   for attr in ['href','src']:
    url=tag.get(attr)
    if not url:continue
    parsed=urlsplit(url)
    if parsed.scheme or parsed.netloc:
     assert parsed.hostname not in ('www.lafmat.com','lafmat.com'),(output,url,'WordPress dependency')
     continue
    target=(DIST/unquote(parsed.path).lstrip('/')).resolve() if parsed.path.startswith('/') else ((output.parent/unquote(parsed.path)).resolve() if parsed.path else output.resolve())
    assert target.is_relative_to(DIST.resolve())
    assert target.is_file(),(output,url)
    if parsed.fragment and target.suffix=='.html':
     if target == (DIST/'index.html').resolve() and parsed.fragment=='conferences':continue  # Main site's JS route.
     other=BeautifulSoup(target.read_text(),'html.parser');assert other.find(id=parsed.fragment),(output,url)
  count+=1
for asset in report['assets']:
 path=DIST/asset['path'];data=path.read_bytes()
 assert len(data)==asset['bytes'] and hashlib.sha256(data).hexdigest()==asset['sha256']
 if path.suffix=='.pdf':assert data.startswith(b'%PDF-')
 elif path.suffix=='.zip':
  with zipfile.ZipFile(path) as z:assert z.testzip() is None
 elif path.suffix=='.png':assert data.startswith(b'\x89PNG\r\n\x1a\n')
 elif path.suffix in ('.jpeg','.jpg'):assert data.startswith(b'\xff\xd8')
assert all((DIST/'conferences/2023'/s/'index.html').is_file() for s in re.findall(r'href="([^"/]+)/index.html"',(DIST/'conferences/2023/index.html').read_text()))
print(f'PASS: {count} archive/legacy pages; source text, images, tables, embeds, navigation, local links and {len(report["assets"])} asset hashes/signatures checked.')
