#!/usr/bin/env python3
"""
Downloads every photo and video this site loads from Framer (framerusercontent.com)
into assets/media/ and rewrites the pages to use the local copies.

Run this once BEFORE you cancel your Framer plan:
    python3 localize-media.py
Needs Python 3.8+ and an internet connection. Safe to run again.
"""
import os, re, urllib.request, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(ROOT, "assets", "media")
URL_RE = re.compile(r"https://framerusercontent\.com/(?:images|assets)/[A-Za-z0-9_\-]+\.(?:png|jpe?g|webp|svg|gif|mp4)(?:\?width=\d+)?")
os.makedirs(MEDIA, exist_ok=True)

def local_name(url):
    base, _, q = url.partition("?")
    name = base.rsplit("/", 1)[-1]
    if q:
        stem, ext = name.rsplit(".", 1)
        name = f"{stem}-{q.split('=')[-1]}w.{ext}"
    return name

pages = []
for d, _, files in os.walk(ROOT):
    if "build" in d.split(os.sep) or os.sep + "media" in d:
        continue
    for f in files:
        if f.endswith((".html", ".css", ".js")) and f != os.path.basename(__file__):
            pages.append(os.path.join(d, f))

urls = set()
for p in pages:
    urls.update(URL_RE.findall(open(p, encoding="utf-8").read()))
print(f"Found {len(urls)} media files")

for u in sorted(urls):
    dest = os.path.join(MEDIA, local_name(u))
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        continue
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as out:
            out.write(r.read())
        print("downloaded", local_name(u))
    except Exception as e:
        print("FAILED", u, e)

for p in pages:
    s = open(p, encoding="utf-8").read()
    rel = os.path.relpath(MEDIA, os.path.dirname(p)).replace(os.sep, "/")
    new = URL_RE.sub(lambda m: f"{rel}/{local_name(m.group(0))}" if os.path.exists(os.path.join(MEDIA, local_name(m.group(0)))) else m.group(0), s)
    if new != s:
        open(p, "w", encoding="utf-8").write(new)
        print("updated", os.path.relpath(p, ROOT))
print("Done. The site now loads its photos and videos from assets/media/.")
