#!/usr/bin/env python3
"""Generates the CubeStack AI static site. Run: python3 build/build.py  (from the site folder)"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from content import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = "https://cubestackai.com"
FONTS = "https://fonts.googleapis.com/css2?family=Anton&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap"

GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>'

def head(p, title, desc, path, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="https://framerusercontent.com/assets/lPtmWEvxub0d5lkE0mqucYCT1U8.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0c">
<link rel="icon" type="image/png" href="{img(M['icon'], 64)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://framerusercontent.com">
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{p}assets/css/site.css">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

NAV = [("Home", ""), ("About", "about/"), ("Our Clients", "work/"), ("Contact", "contact/")]

def header(p, current):
    links = "".join(f'<a href="{p}{h}"{" aria-current=\"page\"" if n == current else ""}>{n}</a>' for n, h in NAV)
    mlinks = "".join(f'<a href="{p}{h}"><small>0{i+1}</small>{n}</a>' for i, (n, h) in enumerate(NAV))
    return f"""<header class="hdr">
  <div class="wrap">
    <a class="logo" href="{p}" aria-label="CubeStack AI home"><img src="{img(M['logo'], 600)}" alt="CubeStack AI"></a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <div class="hdr-r">
      <span class="clock mono">{GLOBE}Local time <span data-clock="Asia/Kolkata">--:--</span></span>
      <a class="btn lime sm" href="{p}contact/">Start growing</a>
      <button class="menu-btn" id="menu-open" aria-expanded="false" aria-controls="menu">Menu</button>
    </div>
  </div>
</header>
<div class="menu" id="menu" aria-hidden="true">
  <video muted loop playsinline preload="none" src="{V_EARTH}" aria-hidden="true"></video>
  <div class="menu-head">
    <a class="logo" href="{p}"><img src="{img(M['logo'], 600)}" alt="CubeStack AI"></a>
    <button class="menu-btn" id="menu-close" style="display:inline-flex">Close</button>
  </div>
  <nav aria-label="Mobile">{mlinks}</nav>
  <div class="menu-foot mono"><span>Email on {EMAIL}</span><span>{PHONE_MAIN}</span><span>Delhi NCR · Toronto · Dubai</span></div>
</div>
<a class="access" href="{WA_ACCESS}" target="_blank" rel="noopener"><span>Request access<small>Get it for free</small></span><i aria-hidden="true">→</i></a>
"""

def final_cta(p):
    strip = "".join(f'<img src="{img(i, 500)}" alt="" loading="lazy">' for i in MOTION)
    return f"""<section class="final" aria-label="Start growing">
  <div class="wrap">
    <p class="mono tag" style="justify-content:center;display:flex">Start growing today</p>
    <h2 class="rv" style="margin-top:22px">Your next</h2>
    <div class="strip rv" aria-hidden="true">{strip}</div>
    <h2 class="rv">Customer is <span class="lime">searching</span><br>for you</h2>
    <div class="cta-row">
      <a class="btn lime" href="{p}contact/">Start growing today <span class="arr">↗</span></a>
      <a class="btn" href="{WA_MAIN}" target="_blank" rel="noopener">Chat on WhatsApp</a>
    </div>
  </div>
</section>
"""

def footer(p):
    return f"""<footer class="ftr">
  <div class="ftr-bg"><img src="{img(M['crowd'], 1200)}" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="ftr-grid">
      <div>
        <a class="logo" href="{p}"><img src="{img(M['logo'], 600)}" alt="CubeStack AI"></a>
        <p class="tagline">Ranked. Trusted.<br><span class="lime">Chosen.</span></p>
        <p style="color:var(--mute);margin-top:14px;max-width:40ch">Engineering local dominance through search, reputation, and AI-powered conversion systems.</p>
      </div>
      <div>
        <h4>Pages</h4>
        <ul><li><a href="{p}">Home</a></li><li><a href="{p}about/">About</a></li><li><a href="{p}work/">Our Clients</a></li><li><a href="{p}contact/">Contact</a></li><li><a href="{p}legal-pages/privacy-policy/">Privacy Policy</a></li></ul>
      </div>
      <div>
        <h4>Contact info</h4>
        <ul>
          <li class="copyable"><span>{PHONE_MAIN}</span><button type="button" class="copy-btn" data-copy="{PHONE_MAIN_RAW}">Copy</button></li>
          <li class="copyable"><span>{EMAIL}</span><button type="button" class="copy-btn" data-copy="{EMAIL}">Copy</button></li>
          <li style="color:var(--soft)">{'<br>'.join(ADDRESS)}</li>
        </ul>
      </div>
      <div>
        <h4>Follow the journey</h4>
        <ul><li><a href="{IG}" target="_blank" rel="noopener">Instagram ↗</a></li><li><a href="{LI}" target="_blank" rel="noopener">LinkedIn ↗</a></li><li><a href="{WA_MAIN}" target="_blank" rel="noopener">WhatsApp ↗</a></li></ul>
      </div>
    </div>
    <div class="wordmark" aria-hidden="true">CubeStack</div>
    <div class="legal mono">
      <span>© <span data-year>2026</span> CubeStack AI</span>
      <span>28.69° N 77.15° E · DEL <span data-clock="Asia/Kolkata">--:--</span> · TOR <span data-clock="America/Toronto">--:--</span> · DXB <span data-clock="Asia/Dubai">--:--</span></span>
      <a href="{p}legal-pages/privacy-policy/">Privacy policy</a>
    </div>
  </div>
</footer>
<script src="{p}assets/js/site.js" defer></script>
"""

def faq_block():
    items = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}<i aria-hidden="true"></i></summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ))
    return f'<div class="faq">{items}</div>'

def sec_head(k, label, title, lede=""):
    l = f'<p class="lede rv">{lede}</p>' if lede else ""
    return f"""<div class="sec-head">
  <div><div class="k"><span class="idx">[{k}]</span><span class="mono">{label}</span></div><h2 class="d2 rv">{title}</h2></div>
  {l}
</div>"""

def proof_badge():
    avs = "".join(f'<img src="{img(a, 120)}" alt="" loading="lazy">' for a in AVATARS) + '<span>+38</span>'
    return f'<div class="proof"><div class="avs">{avs}</div><div><span class="stars" aria-label="5 stars">★★★★★</span><div class="mono">Based on 54+ project reviews</div></div></div>'

def case_card(p, c):
    chips = "".join(f"<span>{t}</span>" for t in c["tags"])
    return f"""<a class="case rv" href="{p}work/{c['slug']}/">
  <div class="ph"><img src="{img(c['card'], 900)}" alt="{c['name']}" loading="lazy"><span class="mono">{c['area']}</span></div>
  <div class="b"><div class="chips">{chips}</div><h3>{c['name']}</h3><p>{c['kind']}</p><span class="go">View case ↗</span></div>
</a>"""

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)
    print("wrote", path)

# ---------------- HOME ----------------
def home():
    p = ""
    svc = ""
    for i, s in enumerate(SERVICES):
        incl = "".join(f"<li>{x}</li>" for x in s["incl"])
        svc += f"""<article class="svc" style="z-index:{i+1}">
  <div class="svc-copy">
    <div class="svc-top"><span class="idx">({i+1:02d})</span><span class="word">{s['word']}</span></div>
    <div style="display:grid;gap:18px"><h3>{s['title']}</h3><p>{s['text']}</p></div>
    <div class="incl"><span class="mono">What's included</span><ul>{incl}</ul></div>
  </div>
  <div class="svc-img"><img src="{img(STEPS[i], 1000)}" alt="" loading="lazy"><span class="mono">Fig. 0{i+1}</span></div>
</article>"""
    why = "".join(f'<article class="rv{" hl" if i == 0 else ""}"><h3 class="d4">{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(WHY))
    tabs = "".join(f'<button type="button" role="tab">{t["name"]}</button>' for t in TESTIMONIALS)
    quotes = "".join(f"""<figure class="q" role="tabpanel"><blockquote>{t['text']}</blockquote>
  <figcaption class="who"><img src="{img(t['img'], 120)}" alt="" loading="lazy"><span><b>{t['name']}</b><span class="mono">{t['org']}</span></span></figcaption></figure>""" for t in TESTIMONIALS)
    team = "".join(f'<a class="person" href="{p}about/#team"><img src="{img(m["img"], 200)}" alt="{m["name"]}" loading="lazy"><span><b>{m["name"]}</b><span class="mono">{m["role"]}</span></span></a>' for m in TEAM)
    cases = "".join(case_card(p, c) for c in CASES)
    words = "".join(f"<span>{w}</span>" for w in ["Rank high", "Own local", "Earn trust", "Stay top"] * 2)
    html = head(p, "CubeStack AI | #1 Google Business Profile Management &amp; Local SEO Agency – Delhi NCR | Toronto",
                "CubeStack AI helps businesses rank higher on Google Maps, win more customers, and protect their reputation — through AI-powered review management, full GBP management, local SEO, and conversion systems. Trusted by businesses across Delhi, Toronto &amp; Dubai.", "/",
                f'<link rel="preload" as="video" href="{V_EARTH}">\n') + header(p, "Home") + f"""
<main id="main">
<section class="hero">
  <div class="hero-media"><video data-bg autoplay muted loop playsinline poster="{img(M['hero_bg'], 1600)}" src="{V_EARTH}" aria-hidden="true"></video></div>
  <canvas id="gl" aria-hidden="true"></canvas>
  <div class="rank-card" aria-hidden="true"><span class="mono">Map pack · position</span><b>#1</b><strong>Your business</strong><span class="stars">★★★★★</span></div>
  <div class="wrap">
    <div class="hero-hud mono"><span class="tag">Google &amp; AI search agency</span><span>Delhi NCR · Toronto · Dubai</span></div>
    <h1 class="d1" style="font-size:clamp(60px,9.6vw,178px)" aria-label="Become the business Google and AI recommends">
      <span class="ln"><span>Become the</span></span>
      <span class="ln"><span>business <span class="out">Google</span></span></span>
      <span class="ln"><span>&amp; AI <span class="lime">recommends</span></span></span>
    </h1>
    <div class="hero-foot">
      <p class="lede" style="color:var(--paper)">Grow your business with Google Profile optimization. AI workflows for feedback, reviews, and automation.</p>
      {proof_badge()}
      <div class="cta-row"><a class="btn lime" href="{p}contact/">Start growing <span class="arr">↗</span></a><a class="btn" href="{p}work/">Our clients</a></div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="track">{words}</div></div>

<section class="sec" aria-labelledby="cube">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:28px"><div><div class="k"><span class="idx">[01]</span><span class="mono">Cube</span></div></div></div>
    <div class="intro">
      <div>
        <h2 id="cube" class="big rv">Helping businesses get <em>discovered</em>, <em>trusted</em>, and <em>recommended</em> across Google &amp; AI Search.</h2>
        <div class="team-mini">{team}</div>
        <div class="cta-row" style="margin-top:22px"><a class="btn sm" href="{p}about/">About CubeStack ↗</a><a class="btn sm" href="{IG}" target="_blank" rel="noopener">Instagram ↗</a></div>
      </div>
      <div class="frame rv" style="aspect-ratio:1"><img src="{img(M['fisheye'], 1000)}" alt="" loading="lazy"><div class="cap mono"><span>Fig. 00</span><span>Seen first</span></div></div>
    </div>
  </div>
</section>

<section class="sec tight" aria-labelledby="stack">
  <div class="wrap">
    {sec_head("02", "Stack", '<span id="stack">Four layers. One growth system.</span>', "We plug into your business as a dedicated growth partner — ranking you higher on Google, managing your reputation, and converting that visibility into real inquiries. Every month. On autopilot.")}
    <div class="stack-list">{svc}</div>
  </div>
</section>

<section class="interlude" aria-label="Our approach">
  <video data-bg autoplay muted loop playsinline src="{V_TREES}" aria-hidden="true"></video>
  <div class="wrap"><p class="mono tag" style="justify-content:center;display:flex;margin-bottom:20px">How we work</p><h2 class="rv">We don't run campaigns. We build infrastructure that <span class="lime">compounds.</span></h2></div>
  <div class="hud mono"><span>Fig. 05 · Signal</span><span>Search · Reputation · Conversion</span></div>
</section>

<section class="geo sec">
  <div class="wrap">
    <div class="copy">
      <div class="k" style="display:flex;gap:16px"><span class="idx">[03]</span><span class="mono">Geo-grid rank scan</span></div>
      <h2 class="d2 rv">Own every street around you.</h2>
      <p class="lede">A geo-grid scan checks where you rank for one search from 49 points around your business. Grey means customers there can't find you. Lime means you're number one.</p>
      <div class="seg" role="group" aria-label="Scan timing"><button type="button" data-mode="before" aria-pressed="false">Before</button><button type="button" data-mode="after" aria-pressed="true">After 60 days</button></div>
      <div><span class="mono">Average map rank</span><div class="avg" id="avg">1.9</div></div>
      <div class="legend mono"><span><i style="background:var(--lime)"></i>#1</span><span><i style="background:#9fd12a"></i>#2–3</span><span><i style="background:#5b4aa8"></i>#4–7</span><span><i style="background:#352e55"></i>#8–12</span><span><i style="background:#222226;box-shadow:0 0 0 1px rgba(255,255,255,.2) inset"></i>13+</span></div>
    </div>
    <div class="map" aria-label="Sample geo-grid showing map rankings around a business">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="M0 62 C 30 55, 55 70, 100 58" stroke="rgba(255,255,255,.08)" stroke-width="2.2" fill="none"/><path d="M38 0 C 42 30, 30 60, 44 100" stroke="rgba(255,255,255,.08)" stroke-width="1.6" fill="none"/><path d="M0 20 L 100 34" stroke="rgba(255,255,255,.05)" stroke-width="1" fill="none"/><path d="M72 0 L 64 100" stroke="rgba(255,255,255,.05)" stroke-width="1" fill="none"/></svg>
      <div class="grid7" id="grid"></div><span class="pin" aria-hidden="true"></span>
      <div class="map-cap mono"><span>Search: “dermatologist near me”</span><span>Sample scan · illustrative</span></div>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="clients">
  <div class="wrap">
    {sec_head("04", "Our clients", '<span id="clients">Results you can find on the map.</span>', "Clinics, diagnostic centres and restaurants across Delhi and Toronto. Every result is a live Google profile you can look up.")}
    <div class="cases">{cases}</div>
    <div class="cta-row" style="margin-top:28px"><a class="btn" href="{p}work/">View all clients ↗</a><a class="btn lime" href="{p}contact/">Contact us ↗</a></div>
  </div>
</section>

<section class="sec tight" aria-labelledby="why">
  <div class="wrap">
    {sec_head("05", "Why CubeStack", '<span id="why">Built on data. Run every day.</span>')}
    <div class="why">
      <div class="frame rv"><img src="{img(M['group'], 1000)}" alt="" loading="lazy"><div class="cap mono"><span>Fig. 06</span><span>Inside your loop</span></div></div>
      <div class="why-list">{why}</div>
    </div>
  </div>
</section>

<section class="sec tight" aria-labelledby="voices">
  <div class="wrap">
    <div class="voices rv">
      <video data-bg autoplay muted loop playsinline src="{V_RIBBON}" aria-hidden="true"></video>
      <div class="voices-in">
        <div style="display:grid;gap:22px;align-content:space-between">
          <div><div class="k" style="display:flex;gap:16px;margin-bottom:18px"><span class="idx">[06]</span><span class="mono">What our clients say</span></div><h2 id="voices" class="d2">In their words.</h2></div>
          <div><div class="count">54+</div><p class="mono">Project reviews · ★★★★★</p></div>
          <div class="q-tabs" role="tablist" aria-label="Client testimonials">{tabs}</div>
        </div>
        <div class="quotes">{quotes}</div>
      </div>
    </div>
  </div>
</section>

{final_cta(p)}
</main>
{footer(p)}<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>
<script src="{p}assets/js/hero3d.js" defer></script>
</body>
</html>
"""
    write("index.html", html)

# ---------------- ABOUT ----------------
def about():
    p = "../"
    sectors = "".join(f'<div class="sector rv"><h3>{a}</h3><p><b style="color:var(--paper)">{b}</b></p><p>{c}</p></div>' for a, b, c in SECTORS)
    pimgs = "".join(f'<img src="{img(s, 1000)}" alt=""{" class=\"on\"" if i == 0 else ""} loading="lazy">' for i, s in enumerate(STEPS))
    steps = ""
    for i, s in enumerate(SERVICES):
        incl = "".join(f"<li>{x}</li>" for x in s["incl"])
        steps += f"""<div class="step{' on' if i == 0 else ''}" data-step="{i}">
  <span class="idx">{i+1:02d} / {s['word']}</span>
  <div class="step-img"><img src="{img(STEPS[i], 900)}" alt="" loading="lazy"></div>
  <h3>{s['title']}</h3><p>{s['text']}</p>
  <div class="incl"><span class="mono">Included</span><ul>{incl}</ul></div>
</div>"""
    team = "".join(f"""<article class="member rv">
  <div class="ph"><img src="{img(m['img'], 1000)}" alt="Portrait of {m['name']}" loading="lazy"></div>
  <div class="b"><div><h3>{m['name']}</h3><span class="mono">{m['role']} / {m['city']}</span></div>
  <div class="socials"><a href="{m['ig']}" target="_blank" rel="noopener" aria-label="{m['name']} on Instagram">IG</a><a href="{m['li']}" target="_blank" rel="noopener" aria-label="{m['name']} on LinkedIn">in</a></div></div>
</article>""" for m in TEAM)
    html = head(p, "About CubeStack AI | Local Growth Partner – Delhi NCR | Toronto | Dubai",
                "CubeStack AI is a local growth partner combining local search intelligence, AI-powered reputation management, and conversion funnel architecture.", "/about") + header(p, "About") + f"""
<main id="main">
<section class="phero">
  <div class="wrap">
    <div class="crumbs mono"><a href="{p}">Home</a><span>/</span><span>About</span></div>
    <div class="case-hero">
      <div style="display:grid;gap:28px">
        <h1 class="d1">We plug into <span class="lime">your business.</span></h1>
        <p class="lede">We plug into your business as a dedicated growth partner — ranking you higher on Google, managing your reputation, and converting that visibility into real inquiries. Every month. On autopilot.</p>
        {proof_badge()}
      </div>
      <div class="frame"><img src="{img(M['street'], 1200)}" alt="" fetchpriority="high"><div class="cap mono"><span>Delhi</span><span>Est. CubeStack AI</span></div></div>
    </div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("01", "Impact we create", "Infrastructure that compounds.")}
    <div class="intro" style="align-items:start">
      <div class="body-copy" style="font-size:19px">
        <p>We are CubeStack AI — a local growth partner that engineers your entire digital presence from the ground up.</p>
        <p>We combine local search intelligence, AI-powered reputation management, and conversion funnel architecture to build one thing: a system that sends you more customers, more calls, and more revenue — every single month.</p>
        <p style="color:var(--paper);font-weight:600">We don't run one-off campaigns. We build infrastructure that compounds.</p>
      </div>
      <div>
        <p class="mono" style="margin-bottom:10px">Who we work for</p>
        <div class="sectors">{sectors}</div>
      </div>
    </div>
  </div>
</section>

<div class="marquee dark" aria-hidden="true"><div class="track">{"".join(f"<span>{w}</span>" for w in ["Local search", "Reputation", "Visibility", "Conversion"] * 2)}</div></div>

<section class="sec">
  <div class="wrap">
    {sec_head("02", "How we work", "Four stages. One system.")}
    <div class="process">
      <div class="process-media" aria-hidden="true"><span class="mono">Step 01 / 04</span>{pimgs}</div>
      <div class="steps">{steps}</div>
    </div>
  </div>
</section>

<section class="sec tight" id="team">
  <div class="wrap">
    {sec_head("03", "Team", "The people inside your growth loop.", "You work directly with the founders, from the first audit to the day you rank #1.")}
    <div class="team">{team}</div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("04", "FAQ's", "Still have a question?", "We are here to help you.")}
    {faq_block()}
  </div>
</section>
{final_cta(p)}
</main>
{footer(p)}</body>
</html>
"""
    write("about/index.html", html)

# ---------------- WORK (clients) ----------------
def work():
    p = "../"
    rows = "".join(f"""<a class="row rv" href="{p}work/{c['slug']}/">
  <span class="idx">({i+1:02d})</span>
  <div style="display:grid;gap:10px"><h3>{c['name']}</h3><div class="chips">{''.join(f'<span>{t}</span>' for t in c['tags'])}</div></div>
  <p style="color:var(--soft)">{c['kind']} · {c['area']}</p>
  <div class="thumb"><img src="{img(c['card'], 700)}" alt="{c['name']}" loading="lazy"></div>
</a>""" for i, c in enumerate(CASES))
    html = head(p, "Our Clients | CubeStack AI", "Case studies from CubeStack AI: Google Business Profile management, AEO and GEO for clinics, wellness centres and restaurants in Delhi and Toronto.", "/work") + header(p, "Our Clients") + f"""
<main id="main">
<section class="phero">
  <div class="phero-bg"><img src="{img(M['hero_bg'], 1600)}" alt=""></div>
  <div class="wrap">
    <div class="crumbs mono"><a href="{p}">Home</a><span>/</span><span>Our Clients</span></div>
    <h1 class="d1">Our <span class="lime">clients</span></h1>
    <p class="lede">Every project below is a live Google profile. Open a case to see the audit, the three-phase build and the results.</p>
  </div>
</section>
<section class="sec tight"><div class="wrap"><div class="rows">{rows}</div></div></section>
{final_cta(p)}
</main>
{footer(p)}</body>
</html>
"""
    write("work/index.html", html)

# ---------------- CASE PAGES ----------------
def case_pages():
    p = "../../"
    for i, c in enumerate(CASES):
        prev_c = CASES[i - 1] if i > 0 else None
        next_c = CASES[i + 1] if i < len(CASES) - 1 else CASES[0]
        phases = "".join(f'<div class="phase rv"><h3>{t}</h3><ol>{"".join(f"<li><span>{x}</span></li>" for x in items)}</ol></div>' for t, items in c["phases"])
        stats = "".join(f'<div class="res rv"><b>{v}</b><p>{l}</p></div>' for v, l in c["stats"])
        gal = "".join(f'<figure><img src="{img(g, 900)}" alt="{c["short"]} project asset" loading="lazy"></figure>' for g in c["gallery"])
        over = "".join(f"<p>{x}</p>" for x in c["overview"])
        res = "".join(f"<p>{x}</p>" for x in c["results"])
        pager = ""
        if prev_c: pager += f'<a href="{p}work/{prev_c["slug"]}/"><span class="mono">← Previous work</span><h3>{prev_c["name"]}</h3></a>'
        else: pager += f'<a href="{p}work/"><span class="mono">← All clients</span><h3>Our clients</h3></a>'
        pager += f'<a href="{p}work/{next_c["slug"]}/"><span class="mono">Next work →</span><h3>{next_c["name"]}</h3></a>'
        html = head(p, c["title"].replace("&amp;", "&amp;") + " | CubeStack AI", re.sub("<.*?>", "", c["overview"][0])[:155], f"/work/{c['slug']}") + header(p, "Our Clients") + f"""
<main id="main">
<section class="phero">
  <div class="wrap">
    <div class="crumbs mono"><a href="{p}">Home</a><span>/</span><a href="{p}work/">Our Clients</a><span>/</span><span>{c['short']}</span></div>
    <div class="case-hero">
      <div style="display:grid;gap:28px">
        <div class="chips">{''.join(f'<span>{t}</span>' for t in c['tags'])}</div>
        <h1 class="d2">{c['name']}</h1>
        <p class="lede">{c['kind']} in {c['area']}.</p>
        <div class="meta">
          <div><span class="mono">Category</span><b>{c['category']}</b></div>
          <div><span class="mono">Year</span><b>{c['year']}</b></div>
          <div><span class="mono">Client</span><b>{c['client']}</b></div>
          <div><span class="mono">Location</span><b>{c['location']}</b></div>
        </div>
        <div class="cta-row"><a class="btn lime" href="{c['live']}" target="_blank" rel="noopener">View live profile ↗</a></div>
      </div>
      <div class="frame"><img src="{img(c['hero'], 1200)}" alt="{c['name']}" fetchpriority="high"></div>
    </div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("01", "Project overview", c['headline'], c['pull'])}
    <div class="body-copy">{over}</div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("02", "Our approach", "Three phases.", c['approach'])}
    <div class="phases">{phases}</div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("03", "The results", "What changed.")}
    <div class="results" style="margin-bottom:48px">{stats}</div>
    <div class="body-copy">{res}</div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    <div class="big-quote">
      <div class="who" style="align-self:start"><img src="{img(c['quote_img'], 160)}" alt="" loading="lazy" style="width:64px;height:64px;object-fit:contain;background:var(--ink-3)"><span><b>{c['quote_name']}</b><span class="mono">{c['quote_role']}</span></span></div>
      <blockquote class="rv">{c['quote']}</blockquote>
    </div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("04", "Work we shipped", "Posts, funnels &amp; reports.", "A selection of the Google Posts, review funnels and performance reports from this project.")}
    <div class="gallery">{gal}</div>
  </div>
</section>

<section class="sec tight"><div class="wrap"><div class="pager">{pager}</div></div></section>
{final_cta(p)}
</main>
{footer(p)}</body>
</html>
"""
        write(f"work/{c['slug']}/index.html", html)

# ---------------- CONTACT ----------------
def contact():
    p = "../"
    html = head(p, "Contact CubeStack AI | Free Google Profile Audit", "Get in touch with CubeStack AI. Call +91 95772 97297 or email admin@cubestackai.com — Pitampura, New Delhi.", "/contact") + header(p, "Contact") + f"""
<main id="main">
<section class="phero" style="padding-bottom:40px">
  <div class="wrap">
    <div class="crumbs mono"><a href="{p}">Home</a><span>/</span><span>Contact</span></div>
    <h1 class="d1">Get in <span class="lime">touch</span></h1>
    <p class="lede">At CubeStack, we're helping businesses become the answer in the age of AI-powered search.</p>
  </div>
</section>
<section class="sec tight">
  <div class="wrap">
    <div class="contact">
      <div class="frame"><img src="{img(M['phone'], 1100)}" alt="A hand holding out a lime-green phone receiver against a blue sky" loading="lazy"><div class="cap mono"><span>[01] Contact</span><span>Hey you! Call your client.</span></div></div>
      <form class="form" data-brief novalidate>
        <div class="who"><img src="{img(M['adarsh'], 160)}" alt="" style="object-position:top"><span><b>Adarsh Ghai</b><span class="mono">Founder | CubeStack</span></span></div>
        <div class="two">
          <div class="field"><label for="f-name">Name*</label><input id="f-name" name="name" required data-label="your name" autocomplete="name" placeholder="Riley Brooks"></div>
          <div class="field"><label for="f-email">Email address*</label><input id="f-email" name="email" type="email" required data-label="your email" autocomplete="email" placeholder="example@gmail.com"></div>
        </div>
        <div class="field"><label for="f-subject">Subject*</label><input id="f-subject" name="subject" required data-label="a subject" placeholder="What's the subject"></div>
        <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="4" placeholder="Tell us the purpose"></textarea></div>
        <button class="btn lime" type="submit" style="justify-self:start">Submit <span class="arr">↗</span></button>
        <div class="form-out" hidden></div>
      </form>
    </div>
    <div class="info">
      <div><span class="mono">Call</span><span class="v copyable"><span>{PHONE_MAIN}</span></span><button type="button" class="copy-btn" data-copy="{PHONE_MAIN_RAW}" style="justify-self:start">Copy number</button></div>
      <div><span class="mono">Email</span><span class="v copyable" style="font-size:clamp(18px,1.6vw,24px)"><span>{EMAIL}</span></span><button type="button" class="copy-btn" data-copy="{EMAIL}" style="justify-self:start">Copy email</button></div>
      <div><span class="mono">Office</span><span style="color:var(--soft)">{'<br>'.join(ADDRESS)}</span></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    {sec_head("02", "FAQ's", "Still have a question?", "We are here to help you.")}
    {faq_block()}
  </div>
</section>
</main>
{footer(p)}</body>
</html>
"""
    write("contact/index.html", html)

# ---------------- PRIVACY ----------------
def privacy():
    p = "../../"
    body = ""
    for h, paras, items in PRIVACY:
        ul = f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>' if items else ""
        body += f'<section>{f"<h2>{h}</h2>" if h else ""}{"".join(f"<p>{x}</p>" for x in paras)}{ul}</section>'
    html = head(p, "Privacy Policy | CubeStack AI", "How CubeStack AI collects, uses and protects your information.", "/legal-pages/privacy-policy") + header(p, "") + f"""
<main id="main">
<section class="phero" style="padding-bottom:40px">
  <div class="wrap">
    <div class="crumbs mono"><a href="{p}">Home</a><span>/</span><span>Privacy Policy</span></div>
    <h1 class="d1">Privacy <span class="lime">policy</span></h1>
    <p class="mono">Last updated: Apr 13, 2026</p>
  </div>
</section>
<section class="sec tight"><div class="wrap"><div class="legal-body">{body}</div></div></section>
</main>
{footer(p)}</body>
</html>
"""
    write("legal-pages/privacy-policy/index.html", html)

if __name__ == "__main__":
    home(); about(); work(); case_pages(); contact(); privacy()
