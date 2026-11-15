#!/usr/bin/env python3
"""Builds the CubeStack AI static site from shared partials.

    python3 build/build.py

Writes index.html and about/index.html at the project root.
Page bodies live in build/pages/*.html and use {R} for the path to the site root.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / 'build' / 'pages'

FR = 'https://framerusercontent.com/images/'
WA_CALL = 'https://wa.me/919599993737?text=Hi%20CubeStack%20AI%2C%20I%27d%20like%20to%20book%20a%20call.'
WA = 'https://wa.me/919577297297?text=Hi%20CubeStack%20AI%2C%20I%27d%20like%20a%20free%20audit.'

SITE = {
    'home': {
        'out': 'index.html', 'R': '', 'active': 'home', 'scripts': ['three', 'home'],
        'title': 'CubeStack AI | Search has evolved. Get discovered through AI.',
        'desc': 'CubeStack AI helps hospitality and local businesses get discovered on Google Maps, search and AI assistants: Google Business Profile management, AI review replies, local SEO and generative engine optimisation. Delhi NCR, Toronto and Dubai.',
    },
    'about': {
        'out': 'about/index.html', 'R': '../', 'active': 'about', 'scripts': ['about'],
        'title': 'About CubeStack AI | AI capability. Human creativity.',
        'desc': 'Meet CubeStack AI: a local growth partner combining AI workflows, automations and creative strategy to help hospitality businesses grow through AI visibility. Founded by Adarsh Ghai and Samaksh Kalra.',
    },
}

NAV = [('home', 'Home', 'index.html'), ('about', 'About', 'about/index.html'), ('work', 'Clients', '#work'), ('contact', 'Contact', '#contact')]


def head(p):
    R = p['R']
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="theme-color" content="#0b0b0b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CubeStack AI">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:image" content="https://framerusercontent.com/assets/lPtmWEvxub0d5lkE0mqucYCT1U8.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{R}assets/brand/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{R}assets/brand/favicon-192.png">
<link rel="apple-touch-icon" href="{R}assets/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="preconnect" href="https://framerusercontent.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Geist:wght@400;500;600&family=Geist+Mono:wght@500&display=swap">
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=clash-grotesk@400,500,600&display=swap">
<link rel="stylesheet" href="{R}assets/css/site.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"CubeStack AI","url":"https://cubestackai.com/","email":"admin@cubestackai.com","telephone":"+91 95772 97297","address":{{"@type":"PostalAddress","streetAddress":"Ground Floor, PP Towers, Plot No. C-1, 2 & 3, Netaji Subhash Place, Pitampura","addressLocality":"New Delhi","postalCode":"110034","addressCountry":"IN"}},"areaServed":["Delhi NCR","Toronto","Dubai"],"sameAs":["https://www.instagram.com/cubestackai/","https://www.linkedin.com/company/cubestackai/"]}}</script>
</head>
'''


def chrome(p, key):
    R = p['R']
    links = []
    for k, label, href in NAV:
        url = (R + href) if not href.startswith('#') else (href if key == 'home' else R + href)
        cur = ' aria-current="page"' if k == p['active'] else ''
        links.append((k, label, url, cur))
    nav = '\n      '.join(f'<a href="{u}"{c} data-scramble>{l}</a>' for _, l, u, c in links)
    mnav = '\n    '.join(f'<a href="{u}"{c}><small>0{i+1}</small><span>{l}</span></a>' for i, (_, l, u, c) in enumerate(links))
    return f'''<body class="locked">
<a class="skip" href="#main">Skip to content</a>
<div class="grain" aria-hidden="true"></div>
<div class="progress" aria-hidden="true"></div>
<div class="c-dot" aria-hidden="true"></div>
<div class="c-ring" aria-hidden="true"><span></span></div>

<div class="loader" id="loader" role="dialog" aria-label="Loading CubeStack AI">
  <div class="loader-mid">
    <div class="stackmark" aria-hidden="true"><i></i><i></i><i></i></div>
    <div class="loader-count"><span id="count">0</span><small>%</small></div>
    <p class="loader-status mono" id="status">Indexing Google Maps</p>
    <div class="loader-enter">
      <button class="btn pri" type="button" data-enter="sound">Enter with sound</button>
      <button class="btn" type="button" data-enter="silent">Enter silently</button>
    </div>
  </div>
  <div class="loader-foot mono"><img class="logo-img" src="{R}assets/brand/cubestack-logo-white.png" alt="CubeStack" width="180" height="36"><span>AI capability. Human creativity.</span></div>
</div>

<header class="hdr">
  <div class="wrap">
    <a class="logo" href="{R}index.html" aria-label="CubeStack AI home"><img src="{R}assets/brand/cubestack-logo-white.png" alt="CubeStack" width="130" height="26"></a>
    <nav class="nav" aria-label="Main">
      {nav}
    </nav>
    <div class="hdr-r">
      <button class="sound" id="sound" type="button" aria-pressed="false" aria-label="Toggle sound"><span class="bars" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span class="t">Sound</span></button>
      <a class="btn pri sm" href="{WA_CALL}" target="_blank" rel="noopener">Book a call</a>
      <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Menu"><i></i><i></i></button>
    </div>
  </div>
</header>

<div class="menu" id="menu" aria-hidden="true">
  <nav aria-label="Mobile">
    {mnav}
  </nav>
  <div class="menu-foot">
    <div>
      <a href="{WA_CALL}" target="_blank" rel="noopener" class="g">Book a call ↗</a>
      <a href="mailto:admin@cubestackai.com">admin@cubestackai.com</a>
      <a href="tel:+919577297297">+91 95772 97297</a>
    </div>
    <video muted loop playsinline preload="none" src="{R}assets/video/hero-loop-sm.mp4" aria-hidden="true"></video>
  </div>
</div>
'''


def footer(p):
    R = p['R']
    home = R + 'index.html'
    return f'''
<footer class="ftr" id="contact">
  <div class="wrap">
    <div class="ftr-top">
      <div>
        <div class="kicker"><span class="idx">(✦)</span><span class="label">Start growing today</span></div>
        <h2 class="chroma rv-lines"><span class="ln"><span>Your next customer</span></span><span class="ln"><span>is <span class="g">searching</span></span></span><span class="ln"><span>for you.</span></span></h2>
      </div>
      <div class="links">
        <a href="{WA_CALL}" target="_blank" rel="noopener" class="mag" data-cursor="Book"><span><small>For owners ready to talk</small><span class="val">Book a call</span></span><span class="g">↗</span></a>
        <a href="{WA}" target="_blank" rel="noopener" class="mag" data-cursor="Chat"><span><small>WhatsApp</small><span class="val">+91 95772 97297</span></span><span class="g">↗</span></a>
        <a href="mailto:admin@cubestackai.com" class="mag" data-cursor="Write"><span><small>Email</small><span class="val">admin@cubestackai.com</span></span><span class="g">↗</span></a>
        <a href="https://www.instagram.com/cubestackai/" target="_blank" rel="noopener" class="mag" data-cursor="DM"><span><small>Prefer a direct conversation?</small><span class="val">DM us @cubestackai</span></span><span class="g">↗</span></a>
      </div>
    </div>
    <nav class="ftr-nav" aria-label="Footer">
      <a href="{home}">Home</a><a href="{R}about/index.html">About</a><a href="{home}#work">Clients</a><a href="https://www.linkedin.com/company/cubestackai/" target="_blank" rel="noopener">LinkedIn</a><a href="https://www.instagram.com/cubestackai/" target="_blank" rel="noopener">Instagram</a><a href="https://cubestackai.com/legal-pages/privacy-policy" target="_blank" rel="noopener">Privacy policy</a>
    </nav>
    <div class="word" id="word" aria-label="CubeStack" data-cursor="Tap">
      <span>C</span><span>U</span><span>B</span><span>E</span><span>S</span><span>T</span><span>A</span><span>C</span><span>K</span>
    </div>
    <div class="legal mono">
      <span>© <span data-year>2026</span> CubeStack AI · Ground Floor, PP Towers, Netaji Subhash Place, Pitampura, New Delhi 110034</span>
      <span>DEL <span data-clock="Asia/Kolkata">--:--</span> · TOR <span data-clock="America/Toronto">--:--</span> · DXB <span data-clock="Asia/Dubai">--:--</span></span>
    </div>
  </div>
</footer>

<div class="film" id="film" role="dialog" aria-modal="true" aria-label="CubeStack AI film">
  <button class="btn sm film-close" type="button">Close ✕</button>
  <div class="film-box"><video controls playsinline preload="none" poster="{R}assets/video/film-poster.jpg" data-src="{R}assets/video/cubestack-film.mp4"></video></div>
</div>
'''


def scripts(p):
    R = p['R']
    s = []
    if 'three' in p['scripts']:
        s.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>')
    s += ['<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>',
          '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>',
          '<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>',
          f'<script src="{R}assets/js/core.js"></script>']
    for name in p['scripts']:
        if name != 'three':
            s.append(f'<script src="{R}assets/js/{name}.js"></script>')
    return '\n'.join(s) + '\n</body>\n</html>\n'


def build():
    for key, p in SITE.items():
        body = (PAGES / f'{key}.html').read_text(encoding='utf-8')
        body = body.replace('{R}', p['R']).replace('{FR}', FR).replace('{WA_CALL}', WA_CALL).replace('{WA}', WA)
        html = head(p) + chrome(p, key) + '\n<main id="main">\n' + body + '\n</main>\n' + footer(p) + scripts(p)
        out = ROOT / p['out']
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding='utf-8')
        print('wrote', out.relative_to(ROOT), f'{len(html)//1024} KB')


if __name__ == '__main__':
    build()
