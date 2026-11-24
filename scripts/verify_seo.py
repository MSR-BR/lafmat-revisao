"""Check generated metadata, sitemap and bounded migration rules offline."""
import csv
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
receipt = json.loads((ROOT / 'docs/seo/static-build.json').read_text())
config = json.loads((DIST / 'vercel.json').read_text())
assert config['trailingSlash'] is True
assert not any(key in config for key in ('rewrites', 'routes', 'proxy', 'crons', 'env', 'functions'))
redirects = config['redirects']
assert all(rule['permanent'] is True for rule in redirects)
assert all(rule['destination'].startswith('/') and not rule['destination'].startswith('//') and '#' not in rule['destination'] for rule in redirects)
assert not any(rule['source'] in ('/(.*)', '/:path*', '/home/:path*') for rule in redirects),'Broad redirect would hide errors'
assert any('X-Robots-Tag' in str(rule) and rule.get('has',[{}])[0].get('type') == 'host' for rule in config['headers'] if rule.get('has'))
assert 'noindex' in BeautifulSoup((DIST / '404.html').read_text(),'html.parser').find('meta',attrs={'name':'robots'})['content']
assert (DIST / 'assets/lafmat-social.png').read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
canonical_urls = set()
for page in receipt['pages']:
    doc = BeautifulSoup((DIST / page['file']).read_text(),'html.parser')
    canonical = 'https://lafmat.com'+page['path']
    assert doc.find('link',rel='canonical')['href'] == canonical
    assert not doc.find('meta',attrs={'name':'robots','content':re.compile('noindex')})
    assert doc.find('meta',attrs={'name':'description'})['content'].strip()
    assert doc.title.string.strip()
    assert doc.find('meta',attrs={'property':'og:url'})['content'] == canonical
    assert doc.find('meta',attrs={'property':'og:title'})['content'] == doc.title.string
    assert doc.find('meta',attrs={'property':'og:image'})['content'] == 'https://lafmat.com/assets/lafmat-social.png'
    variants = {link['hreflang']:link['href'] for link in doc.select('link[rel="alternate"][hreflang]')}
    assert set(variants) == {'en','pt-BR','es','x-default'}
    for language, url in variants.items():
        parsed = urlsplit(url)
        assert parsed.scheme == 'https' and parsed.hostname == 'lafmat.com' and not parsed.query and not parsed.fragment
        target = BeautifulSoup((DIST / (parsed.path.lstrip('/')+'index.html')).read_text(),'html.parser')
        assert target.find('link',rel='canonical')['href'] == url
        assert target.find('link',attrs={'rel':'alternate','hreflang':doc.html['lang']})['href'] == canonical
    organization = json.loads(doc.select_one('#organization-data').string)
    assert organization['@type'] == 'Organization' and organization['url'] == 'https://lafmat.com/'
    assert organization['sameAs'] == ['https://www.youtube.com/@Lafmatnetwork','https://www.facebook.com/61583070328062']
    assert '@type' not in doc.select_one('#organization-data').string.replace('"@type"',''), 'Unexpected structured data'
    canonical_urls.add(canonical)
archive = json.loads((ROOT / 'docs/seo/archive-canonical-routes.json').read_text())
for page in archive:
    assert (DIST / page['file']).is_file()
    canonical_urls.add('https://lafmat.com'+page['path'])
    assert any(rule['source'] == page['path'] and rule['headers'][0]['value'] == '<https://lafmat.com'+page['path']+'>; rel="canonical"' for rule in config['headers'])
ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
entries = ET.parse(DIST / 'sitemap.xml').getroot().findall('s:url',ns)
urls = [entry.findtext('s:loc',namespaces=ns) for entry in entries]
assert len(urls) == len(set(urls)) and set(urls) == canonical_urls
for entry in entries:
    value = entry.findtext('s:lastmod',namespaces=ns)
    if value: assert re.fullmatch(r'20\d{2}-\d{2}-\d{2}',value) and value <= receipt['buildDate']
assert 'Sitemap: https://lafmat.com/sitemap.xml' in (DIST / 'robots.txt').read_text()
assert 'Disallow: /' not in (DIST / 'robots.txt').read_text()
inventory = list(csv.DictReader((ROOT / 'docs/seo/url-inventory.csv').open()))
decisions = list(csv.DictReader((ROOT / 'docs/seo/migration-decisions.csv').open()))
assert {row['url'] for row in decisions} == {row['url'] for row in inventory}
assert len(decisions) == len(inventory) == 1672
assert all(row['behavior'] and row['reason'] for row in decisions)
for row in decisions:
    if row['behavior'] == 'REDIRECT_EQUIVALENT':
        dest = urlsplit(row['destination']).path
        file = DIST / (dest.lstrip('/')+('index.html' if dest.endswith('/') else ''))
        assert file.is_file(),row
    if row['behavior'].startswith('EXCEPTION_'):
        assert not row['destination'], 'Unproved exception must not acquire a fabricated destination'
assert len([rule for rule in redirects if rule['source'].startswith('/home/') and rule['destination'].startswith('/conferences/2023/') and not rule.get('has')]) == 22
print(f'PASS SEO: {len(receipt["pages"])} metadata/reciprocal language sets; {len(urls)} canonical sitemap URLs; {len(redirects)} permanent rules; {len(decisions)} explicit migration decisions')
