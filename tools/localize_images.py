#!/usr/bin/env python3
"""Download every image the site loads from cubestackai.com's Framer CDN into
assets/img/ and point the pages at the local copies.

Run from the project root on any computer with internet access:

    python3 tools/localize_images.py

Safe to run more than once. Needs only the Python standard library.
"""
import re, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'img'
OUT.mkdir(parents=True, exist_ok=True)
FILES = [ROOT / 'index.html', ROOT / 'about' / 'index.html', ROOT / 'assets' / 'js' / 'home.js',
         ROOT / 'build' / 'pages' / 'home.html', ROOT / 'build' / 'pages' / 'about.html']
URL = re.compile(r"(?:https://framerusercontent\.com/images/|\{FR\}|IMG\(')([A-Za-z0-9]+\.(?:jpe?g|png|webp|svg))(\?width=\d+)?")

ids = set()
for f in FILES:
    if f.exists():
        ids.update(m.group(1) for m in URL.finditer(f.read_text(encoding='utf-8')))
print(f'{len(ids)} images referenced')
for name in sorted(ids):
    dest = OUT / name
    if dest.exists():
        continue
    url = f'https://framerusercontent.com/images/{name}' + ('' if name.endswith('.svg') else '?width=1600')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        dest.write_bytes(urllib.request.urlopen(req, timeout=30).read())
        print('  saved', name)
    except Exception as e:
        print('  FAILED', name, e)

def local(prefix):
    return lambda m: (prefix + 'assets/img/' + m.group(1)) if (OUT / m.group(1)).exists() else m.group(0)

for f, prefix in [(ROOT / 'index.html', ''), (ROOT / 'about' / 'index.html', '../')]:
    if f.exists():
        s = re.sub(r"https://framerusercontent\.com/images/([A-Za-z0-9]+\.(?:jpe?g|png|webp|svg))(\?width=\d+)?", local(prefix), f.read_text(encoding='utf-8'))
        f.write_text(s, encoding='utf-8')
js = ROOT / 'assets' / 'js' / 'home.js'
s = js.read_text(encoding='utf-8')
s = s.replace("const IMG = id => 'https://framerusercontent.com/images/' + id;",
              "const IMG = id => (document.documentElement.dataset.root || '') + 'assets/img/' + id;")
s = s.replace("${IMG(img)}?width=700", "${IMG(img)}").replace("${IMG(g)}?width=600", "${IMG(g)}")
js.write_text(s, encoding='utf-8')
print('Done. Pages now load images from assets/img/.')
