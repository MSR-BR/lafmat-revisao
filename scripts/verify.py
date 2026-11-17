"""Verify the local site against its published SHA-256 manifest."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "dist/verification.json").read_text())
actual = {
    path.relative_to(root / "dist").as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
    for path in sorted((root / "dist").rglob("*"))
    if path.is_file() and path.name != "verification.json" and path.name != ".DS_Store"
}
if actual != manifest["files"]:
    raise SystemExit("FAIL: local files differ from the verified publication.")
digest = hashlib.sha256(json.dumps(actual, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
if digest != manifest["sha256"]:
    raise SystemExit("FAIL: invalid verification manifest.")
print("PASS", manifest["code"])
print("SHA256", digest)
print(len(actual), "site files verified")
