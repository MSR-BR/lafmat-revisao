"""Regenerate the local publication manifest after an intentional site change."""
import hashlib,json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
root=Path(__file__).resolve().parent.parent/'dist'
files={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and p.name not in ('verification.json','.DS_Store')}
digest=hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()
date=datetime.now(ZoneInfo('America/Sao_Paulo')).strftime('%Y%m%d')
manifest={'code':f'LAFMAT-{date}-{digest[:12].upper()}','sha256':digest,'files':files}
(root/'verification.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(manifest['code'])
