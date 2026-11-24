"""Preserve former WordPress entry paths on any static deployment base path."""
import html
from pathlib import Path
root=Path(__file__).resolve().parent.parent/'dist'
routes={'home':'','home/know-us':'members/','home/video-gallery':'videos/','home/__trashed':'news/','home/contacts':'contact/','home/seminars':'seminars/','home/conferences':'conferences/','home/about-us':''}
for path,route in routes.items():
 target='../'*len(path.split('/'))+route
 directory=root/path;directory.mkdir(parents=True,exist_ok=True)
 (directory/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url='+html.escape(target,quote=True)+'"><title>LAFMAT — page moved</title></head><body><p>This page has moved. <a href="'+html.escape(target,quote=True)+'">Continue to LAFMAT</a>.</p></body></html>\n')
print('Built',len(routes),'legacy navigation routes')
