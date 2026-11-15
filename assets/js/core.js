/* CubeStack AI — shared site behaviour (all pages) */
(() => {
'use strict';
const REDUCE = matchMedia('(prefers-reduced-motion: reduce)').matches;
const FINE = matchMedia('(hover: hover) and (pointer: fine)').matches;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const CS = window.CS = { REDUCE, FINE, $, $$, clamp, lenis: null, pointer: { x: innerWidth / 2, y: innerHeight / 2, nx: 0, ny: 0 } };

/* year + clocks work even without animation libraries */
$$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
const tick = () => $$('[data-clock]').forEach(el => { try { el.textContent = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: el.dataset.clock }).format(new Date()); } catch (e) {} });
tick(); setInterval(tick, 15000);

const hasGsap = !!(window.gsap && window.ScrollTrigger);
CS.ready = hasGsap;
if (!hasGsap) { const l = $('#loader'); l && l.remove(); document.body.classList.remove('locked'); setupMenuBasic(); return; }
gsap.registerPlugin(ScrollTrigger);
gsap.defaults({ ease: 'power4.out', duration: 1.2 });
ScrollTrigger.config({ ignoreMobileResize: true });

/* ---------------- SOUND (WebAudio, off until the visitor opts in) ---------------- */
CS.Sound = (() => {
  let ctx, master, on = false;
  const init = () => {
    if (ctx) return; const AC = window.AudioContext || window.webkitAudioContext; if (!AC) return;
    ctx = new AC(); master = ctx.createGain(); master.gain.value = 0; master.connect(ctx.destination);
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 420; lp.Q.value = 6;
    const lfo = ctx.createOscillator(), lfoG = ctx.createGain(); lfo.frequency.value = .07; lfoG.gain.value = 220; lfo.connect(lfoG).connect(lp.frequency); lfo.start();
    const padG = ctx.createGain(); padG.gain.value = .045;
    [55, 82.4, 110.3].forEach((f, i) => { const o = ctx.createOscillator(); o.type = i === 1 ? 'triangle' : 'sawtooth'; o.frequency.value = f; o.detune.value = (i - 1) * 7; o.connect(lp); o.start(); });
    lp.connect(padG).connect(master);
  };
  const blip = (freq = 1400, dur = .05, vol = .05, type = 'sine') => {
    if (!on || !ctx) return; const o = ctx.createOscillator(), g = ctx.createGain(), t = ctx.currentTime;
    o.type = type; o.frequency.setValueAtTime(freq, t); o.frequency.exponentialRampToValueAtTime(freq * .6, t + dur);
    g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(.0001, t + dur); o.connect(g).connect(master); o.start(t); o.stop(t + dur + .02);
  };
  const set = v => {
    on = v; if (v) init(); const b = $('#sound'); b && b.setAttribute('aria-pressed', String(v));
    try { localStorage.setItem('cs-sound', v ? '1' : '0'); } catch (e) {}
    if (!ctx) return; ctx.resume && ctx.resume();
    master.gain.cancelScheduledValues(ctx.currentTime); master.gain.linearRampToValueAtTime(v ? 1 : 0, ctx.currentTime + .8);
  };
  return { set, toggle: () => set(!on), hover: () => blip(1700, .04, .022), click: () => blip(520, .12, .07, 'triangle'), tick: () => blip(2400, .015, .01), whoosh: () => blip(180, .5, .05, 'sawtooth'), get on() { return on; }, duck(v) { if (ctx && on) master.gain.linearRampToValueAtTime(v ? .15 : 1, ctx.currentTime + .4); } };
})();
const S = CS.Sound;
$('#sound') && $('#sound').addEventListener('click', () => { S.toggle(); S.click(); });

/* ---------------- TEXT SCRAMBLE ---------------- */
const GLYPHS = '!<>-_\\/[]{}—=+*^?#ABCDEFGHJKLMNPQRSTUVWXYZ0123456789';
CS.scramble = (el, to, dur = 700) => {
  if (REDUCE) { el.textContent = to; return; }
  const from = el.textContent, len = Math.max(from.length, to.length), start = performance.now();
  cancelAnimationFrame(el._sc);
  const step = now => {
    const p = clamp((now - start) / dur, 0, 1); let out = '';
    for (let i = 0; i < len; i++) { const r = p * len * 1.25 - i * .25; out += r >= 1 ? (to[i] || '') : (to[i] === ' ' ? ' ' : GLYPHS[(Math.random() * GLYPHS.length) | 0]); }
    el.textContent = out; if (p < 1) el._sc = requestAnimationFrame(step); else el.textContent = to;
  };
  el._sc = requestAnimationFrame(step);
};
$$('[data-scramble]').forEach(a => { const t = a.textContent; a.addEventListener('mouseenter', () => { CS.scramble(a, t, 420); S.hover(); }); });

/* ---------------- SMOOTH SCROLL (desktop wheel only; native touch scrolling on phones/tablets) ---------------- */
if (window.Lenis && !REDUCE) {
  const lenis = CS.lenis = new Lenis({ duration: 1.15, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smoothWheel: true, syncTouch: false });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add(t => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0);
  let vel = 0; lenis.on('scroll', e => { vel = clamp(e.velocity * .6, -14, 14); });
  gsap.ticker.add(() => { vel *= .9; document.documentElement.style.setProperty('--vel', vel.toFixed(2)); });
}
CS.vel = () => parseFloat(document.documentElement.style.getPropertyValue('--vel')) || 0;
CS.stopScroll = () => { CS.lenis && CS.lenis.stop(); document.body.classList.add('locked'); };
CS.startScroll = () => { CS.lenis && CS.lenis.start(); document.body.classList.remove('locked'); };
CS.scrollTo = target => { const el = typeof target === 'string' ? $(target) : target; if (!el) return; CS.lenis ? CS.lenis.scrollTo(el, { duration: 1.6, offset: 0 }) : el.scrollIntoView({ behavior: REDUCE ? 'auto' : 'smooth' }); };
$$('a[href^="#"]').forEach(a => a.addEventListener('click', e => { const h = a.getAttribute('href'); if (h.length > 1 && $(h)) { e.preventDefault(); closeMenu(); CS.scrollTo(h); } }));
gsap.to('.progress', { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: .3 } });

/* header: hide on scroll down, show on scroll up */
(() => {
  const hdr = $('.hdr'); if (!hdr) return; let last = 0;
  ScrollTrigger.create({ start: 0, end: 'max', onUpdate: self => {
    const y = self.scroll(); hdr.classList.toggle('solid', y > 60);
    if (document.body.classList.contains('menu-open')) return;
    hdr.classList.toggle('hide', y > 300 && y > last + 2); if (y < last - 2) hdr.classList.remove('hide'); last = y;
  } });
})();

/* ---------------- POINTER + CURSOR ---------------- */
const P = CS.pointer;
addEventListener('pointermove', e => { P.x = e.clientX; P.y = e.clientY; P.nx = e.clientX / innerWidth * 2 - 1; P.ny = -(e.clientY / innerHeight) * 2 + 1; }, { passive: true });
if (FINE && !REDUCE) {
  document.documentElement.classList.add('has-cursor');
  const dot = $('.c-dot'), ring = $('.c-ring'), lab = $('.c-ring span');
  const dx = gsap.quickTo(dot, 'x', { duration: .1, ease: 'power3.out' }), dy = gsap.quickTo(dot, 'y', { duration: .1, ease: 'power3.out' });
  const rx = gsap.quickTo(ring, 'x', { duration: .5, ease: 'power3.out' }), ry = gsap.quickTo(ring, 'y', { duration: .5, ease: 'power3.out' });
  addEventListener('pointermove', e => { dx(e.clientX); dy(e.clientY); rx(e.clientX); ry(e.clientY); }, { passive: true });
  document.addEventListener('pointerover', e => {
    const lbl = e.target.closest('[data-cursor]'), hov = e.target.closest('a,button,input,select,summary,.chip');
    if (lbl && (!hov || hov === lbl)) { lab.textContent = lbl.dataset.cursor; ring.classList.add('label'); ring.classList.remove('hover'); }
    else if (hov) { ring.classList.remove('label'); ring.classList.add('hover'); }
    else ring.classList.remove('label', 'hover');
    if (hov) S.hover();
  });
  document.addEventListener('pointerleave', () => gsap.to([dot, ring], { opacity: 0, duration: .3 }));
  document.addEventListener('pointerenter', () => gsap.to([dot, ring], { opacity: 1, duration: .3 }));
}
document.addEventListener('click', e => { if (e.target.closest('a,button,summary')) S.click(); });

/* ---------------- MENU (phones + tablets) ---------------- */
const menu = $('#menu'), burger = $('#burger');
let menuOpen = false, menuTl = null;
function closeMenu() { if (menuOpen) toggleMenu(false); }
function toggleMenu(v) {
  if (!menu) return; menuOpen = v; burger.setAttribute('aria-expanded', String(v)); document.body.classList.toggle('menu-open', v);
  menu.setAttribute('aria-hidden', String(!v));
  if (menuTl) menuTl.kill();
  const r = burger.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height / 2;
  if (v) {
    CS.stopScroll(); $('.hdr').classList.remove('hide');
    const vid = $('video', menu); vid && vid.play().catch(() => {});
    menuTl = gsap.timeline()
      .set(menu, { visibility: 'visible', clipPath: `circle(0px at ${cx}px ${cy}px)` })
      .to(menu, { clipPath: `circle(${Math.hypot(innerWidth, innerHeight)}px at ${cx}px ${cy}px)`, duration: .9, ease: 'expo.inOut' })
      .from($$('nav a span', menu), { yPercent: 110, duration: 1, stagger: .06, ease: 'expo.out' }, '-=.45')
      .from('.menu-foot', { autoAlpha: 0, y: 20, duration: .6 }, '-=.7');
    setTimeout(() => { const f = $('nav a', menu); f && f.focus(); }, 300);
  } else {
    menuTl = gsap.timeline({ onComplete: () => { gsap.set(menu, { visibility: 'hidden' }); const vid = $('video', menu); vid && vid.pause(); } })
      .to(menu, { clipPath: `circle(0px at ${cx}px ${cy}px)`, duration: .7, ease: 'expo.inOut' });
    CS.startScroll(); burger.focus();
  }
}
burger && burger.addEventListener('click', () => toggleMenu(!menuOpen));
menu && $$('a', menu).forEach(a => a.addEventListener('click', () => { if (!a.getAttribute('href').startsWith('#')) closeMenu(); }));
addEventListener('resize', () => { if (innerWidth > 1100) closeMenu(); });
CS.closeMenu = closeMenu;

/* ---------------- FILM MODAL ---------------- */
(() => {
  const film = $('#film'); if (!film) return; const vid = $('video', film), close = $('.film-close', film); let lastFocus;
  const open = () => {
    lastFocus = document.activeElement; CS.stopScroll(); S.duck(true);
    if (!vid.getAttribute('src')) vid.setAttribute('src', vid.dataset.src);
    gsap.timeline().set(film, { visibility: 'visible' }).to(film, { opacity: 1, duration: .4, ease: 'power2.out' })
      .from('.film-box', { scale: .85, y: 40, duration: .9, ease: 'expo.out' }, 0);
    vid.currentTime = 0; vid.muted = false; vid.play().catch(() => {}); close.focus();
  };
  const shut = () => {
    if (film.style.visibility !== 'visible') return; vid.pause(); S.duck(false);
    gsap.to(film, { opacity: 0, duration: .35, onComplete: () => { gsap.set(film, { visibility: 'hidden' }); CS.startScroll(); lastFocus && lastFocus.focus(); } });
  };
  $$('[data-film]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); closeMenu(); open(); }));
  close.addEventListener('click', shut);
  film.addEventListener('click', e => { if (e.target === film) shut(); });
  addEventListener('keydown', e => { if (e.key === 'Escape') { shut(); closeMenu(); } });
})();

/* ---------------- KINETIC TYPE ---------------- */
if (!REDUCE) {
  $$('.rv-lines').forEach(h => gsap.from($$('.ln > span', h), { yPercent: 115, rotate: 3, duration: 1.5, ease: 'expo.out', stagger: .1, scrollTrigger: { trigger: h, start: 'top 88%' } }));
  $$('[data-fade]').forEach(el => gsap.from(el, { y: 30, autoAlpha: 0, duration: 1.2, scrollTrigger: { trigger: el, start: 'top 90%' } }));
  $$('[data-stagger]').forEach(g => gsap.from(g.children, { y: 50, autoAlpha: 0, duration: 1.2, stagger: .08, scrollTrigger: { trigger: g, start: 'top 85%' } }));
  $$('[data-parallax]').forEach(el => gsap.fromTo(el, { yPercent: -(+el.dataset.parallax || 10) }, { yPercent: +el.dataset.parallax || 10, ease: 'none', scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } }));
}
/* counters */
$$('[data-count]').forEach(el => {
  const to = +el.dataset.count, suf = el.dataset.suffix || '', pre = el.dataset.prefix || '', o = { v: 0 };
  ScrollTrigger.create({ trigger: el, start: 'top bottom', once: true, onEnter: () => gsap.to(o, { v: to, duration: REDUCE ? 0 : 2, ease: 'expo.out', onUpdate: () => el.textContent = pre + Math.round(o.v) + suf }) });
});

/* marquee: follows scroll direction and speeds up with velocity */
$$('.marquee .track').forEach(track => {
  let x = 0, dir = -1; if (CS.lenis) CS.lenis.on('scroll', e => { if (e.direction) dir = e.direction > 0 ? -1 : 1; });
  let vis = false; new IntersectionObserver(([e]) => vis = e.isIntersecting).observe(track);
  gsap.ticker.add(() => { if (REDUCE || !vis) return; x += (.6 + Math.abs(CS.vel()) * .8) * dir; const w = track.scrollWidth / 2; if (x < -w) x += w; if (x > 0) x -= w; track.style.transform = `translate3d(${x}px,0,0)`; });
});

/* magnetic */
if (FINE && !REDUCE) {
  const magnet = (el, s) => { const xt = gsap.quickTo(el, 'x', { duration: .9, ease: 'elastic.out(1,.4)' }), yt = gsap.quickTo(el, 'y', { duration: .9, ease: 'elastic.out(1,.4)' });
    el.addEventListener('pointermove', e => { const r = el.getBoundingClientRect(); xt((e.clientX - r.left - r.width / 2) * s); yt((e.clientY - r.top - r.height / 2) * s); });
    el.addEventListener('pointerleave', () => { xt(0); yt(0); }); };
  $$('.btn.pri, .mag').forEach(el => magnet(el, .22));
}

/* FAQ: smooth open/close */
$$('.faq details').forEach(d => {
  const sum = $('summary', d), body = $('.a', d);
  sum.addEventListener('click', e => {
    if (REDUCE) return; e.preventDefault();
    if (d.open) gsap.to(body, { height: 0, opacity: 0, duration: .5, ease: 'power3.inOut', onComplete: () => { d.open = false; gsap.set(body, { clearProps: 'all' }); ScrollTrigger.refresh(); } });
    else { d.open = true; gsap.from(body, { height: 0, opacity: 0, duration: .6, ease: 'power3.out', onComplete: () => ScrollTrigger.refresh() }); }
  });
});

/* footer letters: scatter from the pointer (desktop), burst on tap/click (all devices) */
(() => {
  const word = $('#word'); if (!word) return; const letters = $$('span', word);
  const qs = letters.map(l => ({ x: gsap.quickTo(l, 'x', { duration: .8, ease: 'power3.out' }), y: gsap.quickTo(l, 'y', { duration: .8, ease: 'power3.out' }), r: gsap.quickTo(l, 'rotation', { duration: .8, ease: 'power3.out' }) }));
  if (FINE && !REDUCE) {
    word.addEventListener('pointermove', e => letters.forEach((l, i) => { const r = l.getBoundingClientRect(), dx = r.left + r.width / 2 - e.clientX, dy = r.top + r.height / 2 - e.clientY, d = Math.hypot(dx, dy), f = clamp(1 - d / 320, 0, 1);
      qs[i].x(dx / (d || 1) * f * 70); qs[i].y(dy / (d || 1) * f * 70); qs[i].r(dx / (d || 1) * f * 18); }));
    word.addEventListener('pointerleave', () => qs.forEach(q => { q.x(0); q.y(0); q.r(0); }));
  }
  word.addEventListener('click', () => {
    S.whoosh(); const k = innerWidth < 680 ? .45 : 1;
    gsap.timeline().to(letters, { x: () => gsap.utils.random(-260, 260) * k, y: () => gsap.utils.random(-320, 60) * k, rotation: () => gsap.utils.random(-120, 120), duration: .7, ease: 'expo.out', stagger: .02 })
      .to(letters, { x: 0, y: 0, rotation: 0, duration: 1.4, ease: 'elastic.out(1,.45)', stagger: .03 });
  });
  if (!REDUCE) gsap.from(letters, { yPercent: 100, autoAlpha: 0, stagger: .05, duration: 1.4, ease: 'expo.out', scrollTrigger: { trigger: word, start: 'top 98%' } });
})();

/* ---------------- LOADER ---------------- */
CS.runLoader = (onEnter) => {
  const loader = $('#loader');
  const finish = (withSound) => {
    if (withSound) S.set(true);
    const tl = gsap.timeline({ onComplete: () => { loader && loader.remove(); CS.startScroll(); ScrollTrigger.refresh(); } });
    if (loader) tl.to($('.loader-mid', loader), { y: -40, autoAlpha: 0, duration: .6, ease: 'power3.in' }).to(loader, { clipPath: 'inset(0 0 100% 0)', duration: 1.1, ease: 'expo.inOut' }, '-=.1');
    tl.add(() => { S.whoosh(); onEnter && onEnter(); }, loader ? '-=.9' : 0);
  };
  // returning visitors in the same session skip the long intro
  let seen = false; try { seen = sessionStorage.getItem('cs-intro') === '1'; sessionStorage.setItem('cs-intro', '1'); } catch (e) {}
  if (!loader) { CS.startScroll(); onEnter && onEnter(); return; }
  CS.stopScroll();
  const count = $('#count'), status = $('#status'), cubes = $$('.stackmark i', loader), o = { v: 0 };
  const statuses = ['Indexing Google Maps', 'Reading 4,300 reviews', 'Asking AI who to trust', 'Stacking the layers'];
  let si = 0; const stTimer = setInterval(() => { si = (si + 1) % statuses.length; CS.scramble(status, statuses[si], 500); }, 900);
  gsap.to(cubes, { opacity: 1, y: 0, startAt: { y: -60 }, stagger: .3, duration: 1, ease: 'bounce.out' });
  const minWait = REDUCE || seen ? 150 : 1700;
  const ready = Promise.all([new Promise(r => document.readyState === 'complete' ? r() : addEventListener('load', r, { once: true })), document.fonts ? document.fonts.ready : null, new Promise(r => setTimeout(r, minWait))]);
  const tw = gsap.to(o, { v: 92, duration: minWait / 1000 + .3, ease: 'power2.out', onUpdate: () => count.textContent = Math.round(o.v) });
  Promise.race([ready, new Promise(r => setTimeout(r, 5000))]).then(() => {
    tw.kill();
    gsap.to(o, { v: 100, duration: .4, onUpdate: () => count.textContent = Math.round(o.v), onComplete: () => {
      clearInterval(stTimer);
      if (seen) { finish(false); return; }
      CS.scramble(status, 'Ready. Sound makes it better.', 600);
      gsap.to($('.loader-enter', loader), { autoAlpha: 1, y: 0, startAt: { y: 16 }, duration: .8 });
    } });
  });
  $$('[data-enter]', loader).forEach(b => b.addEventListener('click', () => finish(b.dataset.enter === 'sound'), { once: true }));
};

document.fonts && document.fonts.ready.then(() => ScrollTrigger.refresh());

/* fallback menu when animation libraries fail */
function setupMenuBasic() {
  const m = $('#menu'), b = $('#burger'); if (!m || !b) return;
  b.addEventListener('click', () => { const v = b.getAttribute('aria-expanded') !== 'true'; b.setAttribute('aria-expanded', String(v)); m.style.visibility = v ? 'visible' : 'hidden'; m.style.clipPath = 'none'; });
}
})();
