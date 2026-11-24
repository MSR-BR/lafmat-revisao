"""Serve the static candidate locally, optionally disabling all JavaScript via CSP."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--port', type=int, default=8765)
parser.add_argument('--no-js', action='store_true')
args = parser.parse_args()


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if args.no_js:
            self.send_header('Content-Security-Policy', "script-src 'none'")
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


directory = Path(__file__).resolve().parent.parent / 'dist'
server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, directory=str(directory)))
print(f'Local preview http://127.0.0.1:{args.port}/; JavaScript {"blocked" if args.no_js else "enabled"}', flush=True)
server.serve_forever()
