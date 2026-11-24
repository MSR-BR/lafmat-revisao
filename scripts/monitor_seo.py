#!/usr/bin/env python3
"""Paced, read-only checks of the public LAFMAT site; no Analytics execution."""
import argparse
import datetime as dt
import json
from html.parser import HTMLParser
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = 'https://lafmat.com'
ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ['/', '/pt/', '/es/', '/pt/seminars/', '/es/videos/',
           '/videos/2026/', '/conferences/2023/', '/conferences/2023/program/',
           '/contact/', '/pt/privacy/', '/es/members/', '/pt/news/']
ALIASES = {'/home/program/': '/conferences/2023/program/',
           '/home/event-home/': '/conferences/2023/event-home/'}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = ''
        self.robots = ''
        self.lang = ''
        self.title = ''
        self.in_title = False
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang', '')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href', '')
        if tag == 'meta' and attrs.get('name', '').lower() in ('robots', 'googlebot'):
            self.robots += ' ' + attrs.get('content', '')
        if tag == 'title':
            self.in_title = True
        if tag == 'h1':
            self.h1 += 1

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def run(output):
    result = {'checkedAt': dt.datetime.now(dt.timezone.utc).isoformat(),
              'base': BASE, 'mode': 'public HTTP only; no JS or GA events',
              'checks': [], 'findings': [], 'requests': 0}
    opener = urllib.request.build_opener(NoRedirect())
    last = 0.0

    def get(url):
        nonlocal last
        # Never follow an external location or visit a protected deployment.
        parsed = urllib.parse.urlsplit(url)
        if parsed.hostname not in ('lafmat.com', 'www.lafmat.com'):
            raise RuntimeError('Unexpected host; stopped')
        if result['requests'] >= 35:
            raise RuntimeError('Request budget exceeded; stopped')
        time.sleep(max(0, 1.2 - (time.monotonic() - last)))
        last = time.monotonic()
        req = urllib.request.Request(url, headers={'User-Agent': 'LAFMAT-SEO-Monitor/1.0'})
        try:
            response = opener.open(req, timeout=25)
        except urllib.error.HTTPError as exc:
            response = exc
        result['requests'] += 1
        headers = response.headers
        if headers.get('x-vercel-mitigated') == 'challenge' or response.code == 429:
            raise RuntimeError('Provider challenge/rate limit; stopped, not evidence of missing content')
        return response.code, headers, response.read()

    def require(condition, detail):
        if not condition:
            result['findings'].append(detail)

    try:
        status, _, body = get(BASE + '/verification.json')
        require(status == 200, 'Public manifest unavailable')
        manifest = json.loads(body)
        require(str(manifest.get('code', '')).startswith('LAFMAT-')
                and re.fullmatch(r'[0-9a-f]{64}', str(manifest.get('sha256', '')))
                and bool(manifest.get('files')), 'Malformed public verification manifest')
        result['publicManifest'] = {k: v for k, v in manifest.items() if k != 'files'}
        status, _, body = get(BASE + '/sitemap.xml')
        require(status == 200, 'Sitemap not HTTP 200')
        tree = ET.fromstring(body)
        ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [x.text for x in tree.findall('s:url/s:loc', ns)]
        result['sitemapCanonicalUrls'] = len(urls)
        require(len(urls) == len(set(urls)) and len(urls) > 0, 'Empty/duplicate sitemap URLs')
        require(all(x.startswith(BASE + '/') and '?' not in x and '#' not in x for x in urls),
                'Sitemap has noncanonical host/query/fragment')
        status, _, body = get(BASE + '/robots.txt')
        robots = body.decode('utf-8')
        require(status == 200 and 'Sitemap: ' + BASE + '/sitemap.xml' in robots,
                'Missing robots sitemap declaration')
        require(not re.search(r'^Disallow:\s*/\s*$', robots, re.M | re.I), 'robots blocks all crawling')

        for path in SAMPLES:
            status, headers, body = get(BASE + path)
            page = Page()
            page.feed(body.decode('utf-8', errors='replace'))
            canonical = page.canonical
            if not canonical:
                match = re.search(r'<([^>]+)>;\s*rel="?canonical"?', headers.get('Link', ''), re.I)
                canonical = match.group(1) if match else ''
            ok = (status == 200 and canonical == BASE + path and page.title.strip()
                  and page.h1 > 0 and 'noindex' not in (page.robots + headers.get('X-Robots-Tag', '')).lower())
            require(ok, 'Status/canonical/indexability/title/H1 failed: ' + path)
            require(BASE + path in urls, 'Sample absent from sitemap: ' + path)
            expected_lang = 'pt' if path.startswith('/pt/') else 'es' if path.startswith('/es/') else None
            if expected_lang:
                require(page.lang.startswith(expected_lang), 'Wrong document language: ' + path)
            result['checks'].append({'path': path, 'status': status,
                                     'declaredCanonical': canonical, 'valid': bool(ok)})

        for path, target in ALIASES.items():
            status, headers, _ = get(BASE + path)
            require(status in (301, 308) and headers.get('Location') == target,
                    'Retired alias no longer permanently redirects: ' + path)
            result['checks'].append({'path': path, 'status': status, 'location': headers.get('Location')})
        for variant in ('http://lafmat.com/', 'https://www.lafmat.com/'):
            current = variant
            chain = []
            for _ in range(5):
                status, headers, _ = get(current)
                chain.append({'url': current, 'status': status})
                if status == 200:
                    break
                require(status in (301, 308), 'Nonpermanent domain normalization: ' + variant)
                location = headers.get('Location')
                if not location:
                    break
                current = urllib.parse.urljoin(current, location)
            require(current == BASE + '/' and status == 200, 'Bad normalization/loop: ' + variant)
            result['checks'].append({'variant': variant, 'chain': chain, 'final': current})
        status, _, _ = get(BASE + '/lafmat-healthcheck-unknown-page/')
        require(status == 404, 'Unknown path must return true 404, not home/soft404')
        result['checks'].append({'path': '/lafmat-healthcheck-unknown-page/', 'status': status})
        status, _, body = get(BASE + '/assets/analytics-config.js')
        config = re.sub(r'\s+', '', body.decode('utf-8'))
        require(status == 200 and "measurementId:'G-R5KQ774N5V'" in config
                and 'enabled:true' in config and "allowedHosts:['lafmat.com']" in config,
                'Unexpected public Analytics identity/host configuration')
    except Exception as exc:
        result['findings'].append(str(exc))

    result['result'] = 'FAIL' if result['findings'] else 'PASS'
    result['limits'] = ['HTTP checks do not prove Google index coverage or client consent behavior',
                        'No personal data, account credentials or free search terms collected',
                        'Google reports and existing GA4 consent tests are separate evidence']
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'result': result['result'], 'requests': result['requests'],
                      'validSamples': sum(x.get('valid', False) for x in result['checks']),
                      'findings': result['findings'], 'report': str(output)}, ensure_ascii=False))
    return bool(result['findings'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '.cache/seo-monitoring/latest-http.json')
    raise SystemExit(run(parser.parse_args().output))
