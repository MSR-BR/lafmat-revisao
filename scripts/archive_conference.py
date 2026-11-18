"""Build the 2023 archive from preserved public HTML; --download fetches its media.
Requires beautifulsoup4; no WordPress credentials or server execution required.
"""
import argparse, hashlib, html, json, os, re
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
SOURCE = ROOT / 'sources/conference-2023'
BASE = 'https://www.lafmat.com/home/'
PAGES = [('event-home','Event Home'),('venue','Venue'),('topics','Topics'),('commitee','Commitee'),('poster-2','Poster'),('publications','Publications'),('registration','Registration'),('2757-2','Invited Speakers'),('event-contact','Event Contact'),('important-dates','Important Dates'),('program','Program')]
SLUGS = {slug for slug, _ in PAGES}
ASSET_RECOVERY = {
    '/home/wp-content/uploads/2023/02/logoevent-e1677099273566.jpeg':
    '/home/wp-content/uploads/2023/02/logoevent-removebg-preview.png',
}
HEADER_PREVIEW = 'https://www.lafmat.com/home/wp-content/uploads/2023/02/Head-1080x555.png'
ALLOWED = {'div','span','p','br','strong','b','em','i','u','s','sup','sub','h1','h2','h3','h4','h5','h6','ul','ol','li','table','thead','tbody','tfoot','tr','td','th','caption','a','img','iframe','blockquote','hr','section'}

def text(node):
    return ' '.join(node.get_text(' ',strip=True).split())

def content(soup):
    node = soup.select_one('.et_builder_inner_content')
    if node is None: raise ValueError('Missing source content')
    for menu in node.select('.et_pb_fullwidth_menu, .et_pb_menu'): menu.decompose()
    for bad in node.select('script,style,form'): bad.decompose()
    return node

def local_target(url):
    parsed = urlsplit(urljoin(BASE,url))
    if parsed.hostname not in ('www.lafmat.com','lafmat.com'): return None
    path = unquote(parsed.path)
    path = ASSET_RECOVERY.get(path, path)
    if path.startswith('/home/wp-content/uploads/'):
        return DIST / path.lstrip('/')
    slug = path.removeprefix('/home/').strip('/')
    if slug in SLUGS: return DIST / 'conferences/2023' / slug / 'index.html'
    return None

def relative(target, output):
    return os.path.relpath(target,output.parent).replace(os.sep,'/')

def main():
    args=argparse.ArgumentParser();args.add_argument('--download',action='store_true');opts=args.parse_args()
    records=[];media={};external=set()
    soups={slug:BeautifulSoup((SOURCE/(slug+'.html')).read_text(),'html.parser') for slug,_ in PAGES}
    # Every source image is copied at original resolution. Resized srcset variants
    # are replaced by that same original, avoiding reliance on WordPress thumbnails.
    for slug,_ in PAGES:
        m=content(soups[slug])
        for img in m.select('img[src]'):
            url=urljoin(BASE,img['src']).replace('http://','https://',1)
            target=local_target(url)
            if target is None: raise ValueError('Unexpected remote image '+url)
            if urlsplit(url).path in ASSET_RECOVERY:
                url = 'https://www.lafmat.com' + ASSET_RECOVERY[urlsplit(url).path]
            media[url]=target
        for a in m.select('a[href]'):
            url=urljoin(BASE,a['href']);target=local_target(url)
            if target and '/wp-content/uploads/' in str(target):media[url.replace('http://','https://',1)]=target
            elif not target and not url.startswith(('#','mailto:','tel:')): external.add(url)
    media[HEADER_PREVIEW] = local_target(HEADER_PREVIEW)
    media_records=[]
    for url,target in sorted(media.items()):
        if opts.download:
            target.parent.mkdir(parents=True,exist_ok=True)
            with urlopen(Request(url,headers={'User-Agent':'LAFMAT archive preservation'}),timeout=45) as response:
                payload=response.read()
                if response.headers.get('Content-Type','').startswith('text/html'):raise ValueError('HTML instead of media '+url)
            target.write_bytes(payload)
        payload=target.read_bytes()
        media_records.append({'source':url,'path':target.relative_to(DIST).as_posix(),'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest()})
    for slug,title in PAGES:
        original=soups[slug].select_one('.et_builder_inner_content')
        expected=text(original)
        source_images=len(original.select('img'));source_iframes=[x['src'] for x in original.select('iframe[src]')]
        for tag in list(original.find_all(True)):
            if tag.name not in ALLOWED:tag.unwrap();continue
            keep={k:v for k,v in tag.attrs.items() if k in ('href','src','alt','title','rowspan','colspan','scope','id','class')}
            tag.attrs=keep
            if tag.name=='iframe':
                if urlsplit(tag.get('src','')).hostname not in ('www.youtube.com','www.youtube-nocookie.com'):raise ValueError('Unknown embed')
                tag['title']='Conference venue video';tag['loading']='lazy';tag['allowfullscreen']=''
            if tag.name=='img':
                tag['loading']='lazy'
                if not tag.get('alt'):tag['alt']=tag.get('title') or 'Conference 2023 image'
            if tag.name=='h1':tag.name='h2'
        for img in original.select('img[src]'):
            if urlsplit(img['src']).path.endswith('/Head.png'):
                original_url=img['src'];img['src']=HEADER_PREVIEW
                link=soups[slug].new_tag('a',href=original_url,title='Open original conference banner')
                img.wrap(link)
        for table in original.select('table'):
            wrapper=soups[slug].new_tag('div',attrs={'class':'table-scroll','role':'region','aria-label':'Historical registration fees','tabindex':'0'})
            table.wrap(wrapper)
        # Retain the source text exactly, including historical spelling/date discrepancies.
        for output in [DIST/'conferences/2023'/slug/'index.html', DIST/'home'/slug/'index.html']:
            rendered=BeautifulSoup(str(original),'html.parser')
            for tag in rendered.select('[href],img[src]'):
                attr='src' if tag.name=='img' else 'href';url=tag.get(attr)
                if not url:continue
                target=local_target(url)
                if target:tag[attr]=relative(target,output)
                elif tag.name=='a' and url.startswith(('http:','https:')):tag['rel']='noopener noreferrer'
            nav=''.join('<a '+('aria-current="page" ' if slug==s else '')+'href="'+relative(DIST/'conferences/2023'/s/'index.html',output)+'">'+html.escape(t)+'</a>' for s,t in PAGES)
            css=relative(DIST/'conferences/2023/archive.css',output)
            home=relative(DIST/'index.html',output)+'#conferences'
            page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} · Conference 2023 · LAFMAT</title><meta name="description" content="Historical archive of the II Latin American Conference on Superconductivity and Magnetism, Lima, October 2023."><link rel="stylesheet" href="{css}"></head>
<body><a class="skip" href="#content">Skip to content</a><header><div class="shell"><a class="brand" href="{home}">LAFMAT <span>Conference archive · 2023</span></a></div></header><div class="shell"><p class="archive-notice">Historical archive / Arquivo histórico / Archivo histórico · 2023. Dates, fees and submission instructions refer to the past event; registration is closed.</p><h1>{html.escape(title)}</h1><nav aria-label="Conference 2023">{nav}</nav><main id="content" tabindex="-1">{rendered}</main><footer>II Latin American Conference on Superconductivity and Magnetism · Lima, Peru · 2023.<br>Content preserved from the LAFMAT WordPress site. YouTube videos and institutional references remain external.</footer></div></body></html>'''
            output.parent.mkdir(parents=True,exist_ok=True);output.write_text(page)
            check=BeautifulSoup(page,'html.parser').select_one('main')
            assert text(check)==expected,(slug,'Text mismatch')
            assert len(check.select('img'))==source_images
            assert [x['src'] for x in check.select('iframe')]==source_iframes
        records.append({'slug':slug,'title':title,'source':BASE+slug+'/','source_sha256':hashlib.sha256((SOURCE/(slug+'.html')).read_bytes()).hexdigest(),'text_sha256':hashlib.sha256(expected.encode()).hexdigest(),'text_characters':len(expected),'images':source_images,'embeds':len(source_iframes),'tables':len(original.select('table')),'text_parity':'PASS','legacy_path':'home/'+slug+'/index.html','output':'conferences/2023/'+slug+'/index.html'})
    # Root archive entry is a generated copy so directory links work without JS.
    index=DIST/'conferences/2023/index.html'
    # Generate a simple index whose first action is the full archived event.
    index.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Conference 2023 · LAFMAT</title><link rel="stylesheet" href="archive.css"></head><body><div class="shell"><header><a class="brand" href="../../index.html#conferences">LAFMAT</a></header><h1>II Latin American Conference on Superconductivity and Magnetism</h1><p>Lima, Peru · October 2023 · Historical archive</p><nav aria-label="Conference 2023">'+''.join(f'<a href="{s}/index.html">{html.escape(t)}</a>' for s,t in PAGES)+'</nav><p>Registration is closed. The original texts, images, program and downloadable templates are preserved in this archive.</p></div></body></html>')
    report={'date':'2026-11-18','scope':'All 11 pages in the conference navigation and every locally hosted image/download referenced by their content. Public content only.','pages':records,'assets':media_records,'external_links':sorted(external),'external_embeds':sorted(set(url for s in soups.values() for url in [x['src'] for x in s.select('iframe[src]')])),'limitations':['External YouTube videos are embedded, not downloaded.','Institutional, map, journal and consular reference links remain external.','Historical spelling, dates, fees and public contact information are preserved verbatim; the source contains differing event date ranges.','WordPress database, administrative records, theme and unrelated site pages are outside this conference archive.']}
    report['source_repairs']=[{'missing':k,'replacement':v,'reason':'Original image returns HTTP 404; event logo recovered from the WordPress public media library, attachment 1603.'} for k,v in ASSET_RECOVERY.items()]
    (ROOT/'docs/conference-2023-inventory.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'PASS: {len(records)} pages, {len(media_records)} local assets, text/image/embed parity verified.')

if __name__=='__main__':main()
