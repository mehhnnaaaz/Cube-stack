/* CubeStack AI — home page */
(() => {
'use strict';
const CS = window.CS; if (!CS || !CS.ready) return;
const { REDUCE, FINE, $, $$, clamp, pointer: P } = CS, S = CS.Sound;
const IMG = id => 'https://framerusercontent.com/images/' + id;
const MOBILE = () => innerWidth < 768;

/* ============ HERO VIDEO: right size for the screen, paused when off-screen ============ */
(() => {
  const v = $('#heroVid'); if (!v) return;
  const saveData = navigator.connection && navigator.connection.saveData;
  if (REDUCE || saveData) { v.removeAttribute('autoplay'); v.preload = 'none'; return; } // poster only
  v.src = MOBILE() ? v.dataset.sm : v.dataset.lg;
  v.play().catch(() => {});
  new IntersectionObserver(([e]) => e.isIntersecting ? v.play().catch(() => {}) : v.pause(), { threshold: .05 }).observe(v);
  document.addEventListener('visibilitychange', () => document.hidden ? v.pause() : v.play().catch(() => {}));
  // subtle scroll parallax + fade as the hero leaves
  gsap.to('.vhero-bg', { yPercent: 18, ease: 'none', scrollTrigger: { trigger: '.vhero', start: 'top top', end: 'bottom top', scrub: true } });
})();

/* glass cube floats with the pointer (desktop) or gently on its own (touch) */
(() => {
  const cube = $('#heroCube'); if (!cube || REDUCE) return;
  if (FINE) {
    const xt = gsap.quickTo(cube, 'x', { duration: 1.2, ease: 'power3.out' }), yt = gsap.quickTo(cube, 'y', { duration: 1.2, ease: 'power3.out' }), rt = gsap.quickTo(cube, 'rotation', { duration: 1.2, ease: 'power3.out' });
    addEventListener('pointermove', () => { xt(P.nx * 26); yt(-P.ny * 20); rt(P.nx * 4); }, { passive: true });
  }
  gsap.to(cube, { yPercent: -4, duration: 3, ease: 'sine.inOut', yoyo: true, repeat: -1 });
  gsap.to('.vhero-cube', { yPercent: -30, ease: 'none', scrollTrigger: { trigger: '.vhero', start: 'top top', end: 'bottom top', scrub: true } });
})();

const heroIntro = () => {
  if (REDUCE) return;
  gsap.timeline()
    .from('.vhero h1 .w>span', { yPercent: 110, rotate: 4, duration: 1.6, ease: 'expo.out', stagger: .12 })
    .from('.vhero-copy .label, .vhero-sub, .ctas', { y: 30, autoAlpha: 0, duration: 1.2, stagger: .1 }, '-=1.2')
    .from('.vhero-cube', { scale: .7, autoAlpha: 0, rotate: -12, duration: 1.8, ease: 'expo.out' }, '-=1.4')
    .from('.hud, .vhero-foot > *', { y: 24, autoAlpha: 0, duration: 1, stagger: .06 }, '-=1.4')
    .from('.hdr .wrap > *', { y: -30, autoAlpha: 0, duration: 1, stagger: .08 }, '-=1.3');
};

/* ============ THE STACK: particles morph cube → pin → star → globe ============ */
const Particles = (() => {
  const canvas = $('#gl'), none = { setMorph() {}, intro() {} };
  if (!window.THREE || !canvas) return none;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: true, powerPreference: 'high-performance' }); } catch (e) { return none; }
  const mobile = MOBILE();
  renderer.setPixelRatio(Math.min(devicePixelRatio, mobile ? 1.5 : 2));
  const scene = new THREE.Scene(), camera = new THREE.PerspectiveCamera(38, 1, .1, 100); camera.position.z = 9;
  const N = mobile ? 4000 : 9000, rnd = Math.random;
  const cube = () => { const s = 1.45, u = rnd() * 2 - 1, v = rnd() * 2 - 1;
    if (rnd() < .35) { const e = [u, v, rnd() < .5 ? -1 : 1]; e[(rnd() * 2) | 0] = rnd() < .5 ? -1 : 1; return [e[0] * s, e[1] * s, e[2] * s]; }
    const p = [[1, u, v], [-1, u, v], [u, 1, v], [u, -1, v], [u, v, 1], [u, v, -1]][(rnd() * 6) | 0]; return [p[0] * s, p[1] * s, p[2] * s]; };
  const pin = () => { const r = rnd();
    if (r < .52) { let x, y, z; do { const th = rnd() * Math.PI * 2, ph = Math.acos(2 * rnd() - 1); x = Math.sin(ph) * Math.cos(th); y = Math.sin(ph) * Math.sin(th); z = Math.cos(ph); } while (Math.hypot(x, y) < .42 && Math.abs(z) > .6); return [x * 1.05, y * 1.05 + .75, z * 1.05]; }
    if (r < .9) { const t = rnd(), a = rnd() * Math.PI * 2, rad = Math.pow(1 - t, 1.15) * .98; return [Math.cos(a) * rad, .55 - t * 2.45, Math.sin(a) * rad]; }
    const a = rnd() * Math.PI * 2, rr = .55 + rnd() * .35; return [Math.cos(a) * rr, -2, Math.sin(a) * rr * .45]; };
  const sp = []; for (let i = 0; i < 10; i++) { const a = Math.PI / 2 + i * Math.PI / 5, R = i % 2 ? .72 : 1.85; sp.push([Math.cos(a) * R, Math.sin(a) * R]); }
  const inPoly = (x, y) => { let c = false; for (let i = 0, j = 9; i < 10; j = i++) { const [xi, yi] = sp[i], [xj, yj] = sp[j]; if (((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi)) c = !c; } return c; };
  const star = () => { if (rnd() < .45) { const i = (rnd() * 10) | 0, j = (i + 1) % 10, t = rnd(); const [a, b] = sp[i], [c, d] = sp[j]; return [a + (c - a) * t, b + (d - b) * t - .1, rnd() < .5 ? -.28 : .28]; }
    let x, y; do { x = rnd() * 3.8 - 1.9; y = rnd() * 3.8 - 1.9; } while (!inPoly(x, y)); return [x, y - .1, (rnd() * 2 - 1) * .28]; };
  const cities = [[28.61, 77.21], [43.65, -79.38], [25.2, 55.27]];
  const ll = (lat, lon, r) => { const p = (90 - lat) * Math.PI / 180, t = (lon + 180) * Math.PI / 180; return [-r * Math.sin(p) * Math.cos(t), r * Math.cos(p), r * Math.sin(p) * Math.sin(t)]; };
  const globe = () => { const R = 1.75, r = rnd();
    if (r < .12) { const c = cities[(rnd() * 3) | 0]; return ll(c[0] + (rnd() - .5) * 3, c[1] + (rnd() - .5) * 3, R + rnd() * .55); }
    if (r < .55) return ll(-80 + ((rnd() * 9) | 0) * 20, rnd() * 360 - 180, R);
    if (r < .9) return ll(rnd() * 180 - 90, -180 + ((rnd() * 12) | 0) * 30, R);
    const th = rnd() * Math.PI * 2, ph = Math.acos(2 * rnd() - 1); return [R * Math.sin(ph) * Math.cos(th), R * Math.cos(ph), R * Math.sin(ph) * Math.sin(th)]; };
  const A = new Float32Array(N * 3), B = new Float32Array(N * 3), C = new Float32Array(N * 3), D = new Float32Array(N * 3), Sd = new Float32Array(N * 4);
  for (let i = 0; i < N; i++) { A.set(cube(), i * 3); B.set(pin(), i * 3); C.set(star(), i * 3); D.set(globe(), i * 3); Sd.set([rnd(), rnd() * 2 - 1, rnd() * 2 - 1, rnd() * 2 - 1], i * 4); }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(A, 3)); geo.setAttribute('pB', new THREE.BufferAttribute(B, 3));
  geo.setAttribute('pC', new THREE.BufferAttribute(C, 3)); geo.setAttribute('pD', new THREE.BufferAttribute(D, 3)); geo.setAttribute('seed', new THREE.BufferAttribute(Sd, 4));
  const U = { uMorph: { value: 0 }, uTime: { value: 0 }, uMouse: { value: new THREE.Vector3(99, 99, 0) }, uPx: { value: renderer.getPixelRatio() }, uIntro: { value: REDUCE ? 1 : 0 } };
  const mat = new THREE.ShaderMaterial({ uniforms: U, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
    vertexShader: `attribute vec3 pB; attribute vec3 pC; attribute vec3 pD; attribute vec4 seed;
      uniform float uMorph, uTime, uPx, uIntro; uniform vec3 uMouse; varying float vGlow; varying float vSeed;
      float ease(float t){ t = clamp(t,0.,1.); return t<.5 ? 4.*t*t*t : 1.-pow(-2.*t+2.,3.)/2.; }
      void main(){ vSeed = seed.x;
        vec3 p = mix(position, pB, ease(uMorph)); p = mix(p, pC, ease(uMorph-1.)); p = mix(p, pD, ease(uMorph-2.));
        float mid = sin(fract(clamp(uMorph,0.,2.999)) * 3.14159); p += seed.yzw * mid * (.9 + seed.x);
        p = mix(seed.yzw * 9.0, p, smoothstep(0., 1., clamp(uIntro * 1.35 - seed.x * .35, 0., 1.)));
        p += seed.yzw * .03 * sin(uTime * 1.5 + seed.x * 30.);
        vec4 wp = modelMatrix * vec4(p, 1.0); vec2 d = wp.xy - uMouse.xy; float push = smoothstep(1.5, 0.0, length(d));
        wp.xy += normalize(d + 1e-4) * push * .9; wp.z += push * .6; vGlow = push;
        vec4 mv = viewMatrix * wp; gl_PointSize = (1.4 + seed.x * 2.2 + push * 3.) * uPx * (9.0 / -mv.z); gl_Position = projectionMatrix * mv; }`,
    fragmentShader: `varying float vGlow; varying float vSeed;
      void main(){ float d = length(gl_PointCoord - .5); float a = smoothstep(.5, .0, d);
        vec3 violet = vec3(.486,.227,.929), white = vec3(.96,.96,.95), green = vec3(.714,1.,0.);
        vec3 c = mix(white, violet, step(.55, vSeed)); c = mix(c, green, step(.9, vSeed)); c = mix(c, green, vGlow * .8);
        gl_FragColor = vec4(c, a * (.55 + vGlow * .45)); }` });
  const group = new THREE.Group(); group.add(new THREE.Points(geo, mat)); scene.add(group);
  const dn = mobile ? 400 : 1100, dp = new Float32Array(dn * 3);
  for (let i = 0; i < dn; i++) dp.set([(rnd() - .5) * 30, (rnd() - .5) * 18, -rnd() * 14 - 2], i * 3);
  const dg = new THREE.BufferGeometry(); dg.setAttribute('position', new THREE.BufferAttribute(dp, 3));
  const dust = new THREE.Points(dg, new THREE.PointsMaterial({ color: 0xa78bfa, size: .035, transparent: true, opacity: .35, depthWrite: false })); scene.add(dust);
  const halfH = () => Math.tan(THREE.MathUtils.degToRad(19)) * camera.position.z;
  function layout() {
    const w = canvas.clientWidth, h = canvas.clientHeight; if (!w || !h) return;
    renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix();
    const hh = halfH(), perPx = 2 * hh / h;
    if (w <= 1100) { group.position.set(0, hh - Math.min(h * .3, 260) * perPx, 0); group.scale.setScalar(clamp(Math.min(w * .6, h * .34) * perPx / 3.9, .35, .9)); }
    else { group.position.set(hh * camera.aspect * .45, 0, 0); group.scale.setScalar(.9); }
  }
  layout(); addEventListener('resize', layout);
  let visible = false; new IntersectionObserver(([e]) => visible = e.isIntersecting).observe(canvas);
  const clock = new THREE.Clock(), rot = { x: 0, y: 0 }, mw = new THREE.Vector3(), tmp = new THREE.Vector3(); let last = 0, introd = false;
  (function frame() {
    requestAnimationFrame(frame); if (!visible) return;
    if (!introd) { introd = true; gsap.to(U.uIntro, { value: 1, duration: 3, ease: 'expo.out' }); }
    const t = REDUCE ? 0 : clock.getElapsedTime(); U.uTime.value = t;
    rot.x += (P.ny * .3 - rot.x) * .05; rot.y += (P.nx * .5 - rot.y) * .05;
    group.rotation.y = t * .18 + rot.y; group.rotation.x = .25 - rot.x;
    if (FINE) { tmp.set(P.nx, P.ny, .5).unproject(camera).sub(camera.position).normalize(); mw.copy(camera.position).add(tmp.multiplyScalar(-camera.position.z / tmp.z)); U.uMouse.value.lerp(mw, .2); }
    dust.rotation.y = t * .01 + rot.y * .1; renderer.render(scene, camera);
  })();
  return { setMorph(v) { U.uMorph.value = v; const s = Math.round(v); if (s !== last) { last = s; S.whoosh(); } } };
})();

(() => {
  const STAGES = [
    ['00 / The stack', 'One connected growth system.', 'We stack AI workflows, automations and creative strategies so every layer makes the next one stronger.'],
    ['01 / Lead', 'Get discovered through AI search.', 'Your Google profile, map pin and website become the answer when someone nearby searches or asks an assistant.'],
    ['02 / Support', 'Reputation that sells for you.', 'Review requests, brand-aligned replies within hours and a maintained digital presence that earns the five stars.'],
    ['03 / Proof', 'Recommended, from Delhi to Toronto.', 'Relevant audits, monthly ranking reports and verified client results, so you see exactly what the work delivered.']
  ];
  const dots = $$('.stage-dots i'), k = $('#stage-k'), t = $('#stage-t'), p = $('#stage-p'); let cur = 0;
  const set = s => { if (s === cur) return; cur = s; dots.forEach((d, i) => d.classList.toggle('on', i === s)); CS.scramble(k, STAGES[s][0], 450); CS.scramble(t, STAGES[s][1], 600); p.textContent = STAGES[s][2]; gsap.fromTo(p, { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0, duration: .6 }); };
  ScrollTrigger.create({ trigger: '#stack', start: 'top top', end: '+=240%', pin: true, scrub: 1, anticipatePin: 1,
    onUpdate: self => { const m = self.progress * 3.2; Particles.setMorph(Math.min(m, 3)); set(clamp(Math.round(m - .1), 0, 3)); } });
})();

/* ============ MANIFESTO: gooey blob reveals the colour image ============ */
(() => {
  const sec = $('#reveal'); if (!sec) return; const svg = $('svg', sec), g = $('#blobs'), NS = 'http://www.w3.org/2000/svg';
  const circles = [], pts = [];
  for (let i = 0; i < 14; i++) { const c = document.createElementNS(NS, 'circle'); c.setAttribute('r', String(Math.max(30, 150 - i * 8))); g.appendChild(c); circles.push(c); pts.push({ x: 800, y: 500 }); }
  const target = { x: 800, y: 500 }; let inside = false, idleT = 0;
  if (!FINE) $('#revealHint').textContent = 'Touch to reveal';
  const move = (cx, cy) => { const pt = svg.createSVGPoint(); pt.x = cx; pt.y = cy; const q = pt.matrixTransform(svg.getScreenCTM().inverse()); target.x = q.x; target.y = q.y; inside = true; };
  sec.addEventListener('pointermove', e => move(e.clientX, e.clientY));
  sec.addEventListener('pointerdown', e => move(e.clientX, e.clientY));
  sec.addEventListener('touchmove', e => { const t = e.touches[0]; t && move(t.clientX, t.clientY); }, { passive: true });
  sec.addEventListener('pointerleave', () => inside = false);
  sec.addEventListener('touchend', () => setTimeout(() => inside = false, 1200));
  let vis = false; new IntersectionObserver(([e]) => vis = e.isIntersecting).observe(sec);
  gsap.ticker.add(() => {
    if (!vis) return; idleT += .012;
    if (!inside) { target.x = 800 + Math.cos(idleT) * 420; target.y = 520 + Math.sin(idleT * 1.6) * 200; }
    pts.forEach((p, i) => { const lead = i ? pts[i - 1] : target, k = i ? .35 : .18; p.x += (lead.x - p.x) * k; p.y += (lead.y - p.y) * k; circles[i].setAttribute('cx', p.x.toFixed(1)); circles[i].setAttribute('cy', p.y.toFixed(1)); });
  });
})();

/* ============ SERVICES: CSS 3D photo cube unfolds into six cards ============ */
(() => {
  const FACES = [
    ['01', 'Local Search Dominance', 'GBP audit, competitor gap map and keyword opportunity report, then a roadmap to rank where it counts.', 'HewGZDb4kitchTonXqZWVOG0I.jpeg'],
    ['02', 'GBP & Reputation', 'Weekly posts, photo strategy, Q&A, categories and booking links, managed every week.', '5Gdyi1OlIgjEZyOUJvgHTtiZTY.jpeg'],
    ['03', 'AI Review Engine', 'QR and WhatsApp review requests, private feedback for unhappy guests and a brand-aligned reply within hours.', 'VmKdVtoi6iwJGNQYKMEQo3J0.jpeg'],
    ['04', 'Local SEO Engine', 'Keyword clustering, geo-tagging, citations and a monthly ranking report.', 'MvMpg2CuNUCw6I6d320mlFW2QmY.jpeg'],
    ['05', 'Generative Engine Optimisation', 'LocalBusiness schema and entity signals so ChatGPT, Gemini and Maps can recommend you by name.', 'Nhg3CzeifKzMzUNXiaWpzJQfbE.jpeg'],
    ['06', 'Conversion Funnels', 'Landing pages, digital booklets and feedback intelligence that turn views into bookings.', 'IUEGTr5CussTQxtdgQ8zMQTd0BA.jpeg']
  ];
  const ORI = [[0, 0], [0, 90], [0, 180], [0, -90], [90, 0], [-90, 0]];
  const cubeEl = $('#cube'); if (!cubeEl) return; const wraps = [], inners = [];
  FACES.forEach(([n, t, d, img]) => {
    const w = document.createElement('div'); w.className = 'face-w';
    w.innerHTML = `<div class="face"><img src="${IMG(img)}?width=700" alt="" loading="lazy"><div class="fc"><span class="fn">${n} / 06</span><h3>${t}</h3><p class="fd">${d}</p></div></div>`;
    cubeEl.appendChild(w); wraps.push(w); inners.push($('.face', w));
  });
  const sec = $('#services'), head = $('.unfold-head'), headP = $('.unfold-head p'); let S_ = 300;
  const wide = () => innerWidth > 1100;
  const sizes = () => { const vw = innerWidth, vh = innerHeight; S_ = vw < 680 ? Math.min(vw * .42, vh * .2) : vw <= 1100 ? Math.min(vw * .26, vh * .2) : Math.min(vw * .2, vh * .3, 320); $('#scene').style.setProperty('--s', S_ + 'px'); };
  sizes();
  const area = () => {
    const W = innerWidth, H = sec.offsetHeight;
    if (wide()) { const l = head.offsetLeft + head.offsetWidth + 40; return { x: l, y: 100, w: W - l - 40, h: H - 140, cols: 3 }; }
    const h2 = $('h2', head), top = head.offsetTop + h2.offsetTop + h2.offsetHeight + 24;
    return { x: 14, y: top, w: W - 28, h: H - top - 24, cols: W < 680 ? 2 : 3 };
  };
  const flatPos = i => { const a = area(), cols = a.cols, rows = 6 / cols, g = S_ * .08, c = i % cols, r = (i / cols) | 0; return [(c - (cols - 1) / 2) * (S_ + g), (r - (rows - 1) / 2) * (S_ + g)]; };
  const flatScale = () => { const a = area(), rows = 6 / a.cols; return Math.min(1.05, a.w / (a.cols * S_ * 1.08), a.h / (rows * S_ * 1.08)); };
  const flatShift = () => { const a = area(), sc = $('#scene'); return [a.x + a.w / 2 - sc.offsetLeft, a.y + a.h / 2 - sc.offsetTop]; };
  wraps.forEach((w, i) => { gsap.set(w, { x: 0, y: 0, rotationX: ORI[i][0], rotationY: ORI[i][1] }); gsap.set(inners[i], { z: () => S_ / 2 }); });
  gsap.set(cubeEl, { rotationX: -22, rotationY: 35 });
  const idle = REDUCE ? null : gsap.to(cubeEl, { rotationY: '+=360', duration: 24, ease: 'none', repeat: -1 });
  gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: sec, start: 'top top', end: '+=220%', pin: true, scrub: 1, invalidateOnRefresh: true,
      onEnter: () => idle && idle.pause(), onLeaveBack: () => idle && idle.resume(), onRefreshInit: sizes } })
    .to(cubeEl, { rotationY: () => '+=' + (360 - (gsap.getProperty(cubeEl, 'rotationY') % 360) + 360), rotationX: 340, duration: 1, ease: 'power1.inOut' })
    .to(headP, { autoAlpha: () => wide() ? 1 : 0, duration: .4 }, .9)
    .to(cubeEl, { rotationX: 0, rotationY: () => Math.ceil(gsap.getProperty(cubeEl, 'rotationY') / 360) * 360 + 720, scale: () => flatScale(), x: () => flatShift()[0], y: () => flatShift()[1], duration: 1, ease: 'power2.inOut' }, 1)
    .to(wraps, { x: i => flatPos(i)[0], y: i => flatPos(i)[1], rotationX: 0, rotationY: 0, duration: 1, ease: 'expo.inOut', stagger: .04 }, '<.2')
    .to(inners, { z: 0, duration: 1, ease: 'expo.inOut', stagger: .04 }, '<')
    .to($$('.fd', cubeEl), { opacity: 1, duration: .4, stagger: .05 }, '-=.3')
    .to({}, { duration: .5 });
})();

/* ============ AI SEARCH DEMO ============ */
(() => {
  const log = $('#log'), form = $('#askform'), input = $('#askq'); if (!log) return;
  const ANSWERS = [
    { q: 'Best skin clinic in Punjabi Bagh?', a: 'For skin, hair and dental care in Punjabi Bagh, a strong option is <b>Zenith Skin, Hair & Dental Clinic</b>. It appears in the West Delhi local pack for dermatology, PRP hair treatment and Invisalign, and replies to patient reviews within hours.', src: ['Google Maps · Zenith', 'Top 3 locally', 'Reviews answered < 2h'] },
    { q: 'Health checkups in Pitampura', a: 'Near Rani Bagh in Pitampura, <b>BHC Wellness</b> lists over 30 health packages from Rs. 599, including thyroid, cardiac and women\'s health checkups, with physiotherapy and pathology under one roof.', src: ['Google Maps · BHC Wellness', '30+ packages', 'Open Mon–Sat'] },
    { q: 'Best Indian restaurant in North York', a: 'In North York, <b>Shahi Manjil</b> on Victoria Park Ave stands out: 4.8 stars from 4,300+ reviews, regional chefs with no MSG or artificial colours, and online table booking through OpenTable.', src: ['Google Maps · Shahi Manjil', '4.8★ · 4,300+', 'Book via OpenTable'] }
  ];
  let busy = false;
  const bubble = (cls, html) => { const d = document.createElement('div'); d.className = 'msg ' + cls; d.innerHTML = html; log.appendChild(d); gsap.from(d, { y: 16, autoAlpha: 0, duration: .6 }); return d; };
  const esc = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  async function run(q, answer, src) {
    if (busy) return; busy = true;
    while (log.children.length > 3) log.removeChild(log.firstChild);
    bubble('me', esc(q)); const ai = bubble('ai', '<span class="caret"></span>'), span = ai.firstChild;
    await new Promise(r => setTimeout(r, 600));
    const tokens = answer.match(/<b>.*?<\/b>|\S+\s*/g) || []; let html = '';
    for (const tk of tokens) { html += tk.startsWith('<b>') ? tk + ' ' : tk; span.innerHTML = html; S.tick(); await new Promise(r => setTimeout(r, REDUCE ? 0 : 34 + Math.random() * 36)); }
    span.classList.remove('caret');
    if (src) { const s = document.createElement('div'); s.className = 'src'; s.innerHTML = src.map(x => `<span>◎ ${x}</span>`).join(''); ai.appendChild(s); gsap.from(s.children, { y: 10, autoAlpha: 0, stagger: .08, duration: .5 }); }
    busy = false;
  }
  $$('.chip').forEach(c => c.addEventListener('click', () => { const a = ANSWERS[+c.dataset.q]; run(a.q, a.a, a.src); }));
  form.addEventListener('submit', e => { e.preventDefault(); const q = input.value.trim(); if (!q) return; input.value = ''; input.blur();
    run(q, `For “${esc(q)}”, AI assistants favour businesses with a complete Google profile, a steady flow of fresh reviews with owner replies, and structured data on their website. <b>That's exactly what CubeStack builds</b>, so the answer can be your business.`, ['How AI picks local answers']); });
  ScrollTrigger.create({ trigger: '#ask', start: 'top 60%', once: true, onEnter: () => { const a = ANSWERS[0]; run(a.q, a.a, a.src); } });
})();

/* ============ AI VISIBILITY SCORE ============ */
(() => {
  const rv = $('#s-reviews'); if (!rv) return;
  const st = { cat: 'restaurant', reply: 1, posts: 0, schema: 0 }, rr = $('#s-rating'), oRv = $('#o-reviews'), oRr = $('#o-rating');
  const arc = $('#arc'), num = $('#scoreN'), verdict = $('#verdict'), bk = $('#bk'), cta = $('#scoreCta');
  const ticks = $('#ticks'); for (let i = 0; i <= 20; i++) { const a = Math.PI - i / 20 * Math.PI, r1 = 104, r2 = i % 5 ? 112 : 118, l = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    l.setAttribute('x1', 150 + Math.cos(a) * r1); l.setAttribute('y1', 160 - Math.sin(a) * r1); l.setAttribute('x2', 150 + Math.cos(a) * r2); l.setAttribute('y2', 160 - Math.sin(a) * r2); l.setAttribute('stroke', 'rgba(255,255,255,.22)'); l.setAttribute('stroke-width', '1.5'); ticks.appendChild(l); }
  bk.innerHTML = ['Review volume', 'Rating strength', 'Owner engagement', 'Profile activity', 'AI readiness'].map(r => `<div class="bk"><span>${r}</span><em>0</em><span class="bar"><i></i></span></div>`).join('');
  const shown = { v: 0 };
  function compute() {
    const reviews = +rv.value, rating = +rr.value;
    const parts = [Math.min(1, Math.log10(1 + reviews) / Math.log10(301)), clamp((rating - 3.5) / 1.4, 0, 1), st.reply / 2, st.posts / 2, st.schema ? 1 : (st.posts ? .35 : .15)];
    const score = Math.round(parts.reduce((s, p, i) => s + p * [22, 18, 20, 20, 20][i], 0));
    oRv.textContent = reviews; oRr.textContent = rating.toFixed(1);
    gsap.to(shown, { v: score, duration: 1.1, ease: 'expo.out', onUpdate: () => { num.textContent = Math.round(shown.v); arc.setAttribute('stroke-dasharray', `${shown.v} 100`); } });
    $$('.bk', bk).forEach((row, i) => { const pct = Math.round(parts[i] * 100); $('em', row).textContent = pct; gsap.to($('i', row), { width: pct + '%', duration: 1, ease: 'expo.out' }); });
    const v = score < 40 ? ['Invisible to AI', '#ff6b5b'] : score < 65 ? ['Losing customers', '#ffc940'] : score < 85 ? ['Close to the top', '#b6ff00'] : ['Map-pack ready', '#b6ff00'];
    if (verdict.textContent !== v[0]) CS.scramble(verdict, v[0], 500); verdict.style.color = v[1];
    const name = $('#s-name').value.trim() || 'my business', city = $('#s-city').value;
    cta.href = 'https://wa.me/919577297297?text=' + encodeURIComponent(`Hi CubeStack AI, I did the AI visibility self-check.\nBusiness: ${name} (${st.cat}, ${city})\nScore: ${score}/100\nReviews: ${reviews} · Rating: ${rating.toFixed(1)}\nI'd like the full free audit.`);
  }
  $$('.seg[data-key]').forEach(seg => seg.addEventListener('click', e => { const b = e.target.closest('button'); if (!b) return;
    $$('button', seg).forEach(x => x.setAttribute('aria-pressed', String(x === b))); const k = seg.dataset.key; st[k] = k === 'cat' ? b.dataset.v : +b.dataset.v; compute(); }));
  [rv, rr].forEach(r => r.addEventListener('input', () => { compute(); S.tick(); }));
  $('#s-name').addEventListener('input', compute); $('#s-city').addEventListener('change', compute);
  ScrollTrigger.create({ trigger: '#score', start: 'top 70%', once: true, onEnter: compute }); compute();
})();

/* ============ CITIES: horizontal scroll; grids light up ============ */
(() => {
  const track = $('#ctrack'); if (!track) return; const grids = $$('.grid9');
  grids.forEach(g => { for (let i = 0; i < 81; i++) { const d = document.createElement('i'); if (i === 40) d.classList.add('home'); g.appendChild(d); } });
  const paint = (g, p) => $$('i', g).forEach((d, i) => { const x = i % 9 - 4, y = ((i / 9) | 0) - 4, dist = Math.hypot(x, y), lit = p > dist / 5.7, rank = lit ? (dist < 2.2 ? 1 : dist < 3.6 ? 2 : 3) : 0;
    d.className = (i === 40 ? 'home ' : '') + (rank ? 'r' + rank : ''); d.textContent = rank || ''; });
  const dist = () => track.scrollWidth - innerWidth;
  gsap.to(track, { x: () => -dist(), ease: 'none', scrollTrigger: { trigger: '#cities', start: 'top top', end: () => '+=' + dist(), pin: true, scrub: 1, invalidateOnRefresh: true,
    onUpdate: self => { const n = grids.length; grids.forEach((g, i) => paint(g, clamp(self.progress * (n + .6) - i - .2, 0, 1))); } } });
})();

/* ============ BEFORE / AFTER ============ */
(() => {
  const box = $('#baBox'); if (!box) return; const handle = $('.ba-handle button', box); let drag = false; const cur = { v: 50 };
  const set = v => { v = clamp(v, 0, 100); box.style.setProperty('--cut', v + '%'); handle.setAttribute('aria-valuenow', Math.round(v)); };
  const fromX = x => (x - box.getBoundingClientRect().left) / box.offsetWidth * 100;
  // drag anywhere on desktop; on touch, drag the handle so vertical page scrolling still works
  const start = e => { drag = true; try { e.target.setPointerCapture(e.pointerId); } catch (_) {} gsap.to(cur, { v: fromX(e.clientX), duration: .4, onUpdate: () => set(cur.v) }); };
  (FINE ? box : handle).addEventListener('pointerdown', start);
  if (!FINE) box.addEventListener('click', e => { if (e.target === handle) return; gsap.to(cur, { v: fromX(e.clientX), duration: .5, onUpdate: () => set(cur.v) }); });
  addEventListener('pointermove', e => { if (!drag) return; cur.v = fromX(e.clientX); set(cur.v); });
  addEventListener('pointerup', () => drag = false); addEventListener('pointercancel', () => drag = false);
  handle.addEventListener('keydown', e => { if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') { e.preventDefault(); cur.v = clamp(cur.v + (e.key === 'ArrowLeft' ? -5 : 5), 0, 100); set(cur.v); } });
  if (!REDUCE) ScrollTrigger.create({ trigger: box, start: 'top 65%', once: true, onEnter: () => gsap.timeline().to(cur, { v: 82, duration: 1, ease: 'expo.inOut', onUpdate: () => set(cur.v) }).to(cur, { v: 22, duration: 1.2, ease: 'expo.inOut', onUpdate: () => set(cur.v) }).to(cur, { v: 50, duration: .9, ease: 'expo.out', onUpdate: () => set(cur.v) }) });
  set(50);
})();

/* ============ CASES: full-screen expanding overlay ============ */
(() => {
  const CASES = [
    { name: 'Zenith Skin, Hair & Dental', place: 'Punjabi Bagh, West Delhi', tags: 'AEO · Google Business Profile Management · 2026',
      gap: 'The profile was built for skin alone. Hair and dental were invisible on Google, with no service entries, keyword targeting or categories.',
      steps: ['5-pillar GBP audit and a prioritised fix list', 'Primary category reset plus 8 secondary categories across all three specialties', '45-entry service catalogue: 15 each for skin, hair and dental, geo-targeted to West Delhi', 'QR review programme, WhatsApp requests and AI-assisted replies within 2 hours', 'Google Posts twice a week and a monthly ranking report'],
      stats: [['Top 3', 'Target skin, hair & dental keywords in West Delhi'], ['3×', 'Verticals reaching the local pack'], ['4.8★', 'Rating sustained with managed review replies']],
      quote: 'Within 45 days, we were ranking in the top 3 for key hair and dental terms we\'d never appeared for before.', who: 'Dr Vijay Singhal, Founder & Lead Consultant',
      live: 'https://share.google/SeVrcPgV9BWMqnE9k', gal: ['n8ifxhG02KH7qGMhLHEi60Q54.png', 'XvYWouKw5d9zsg97WQNo7PkVCOI.jpeg', 'Skd2Tlj5KyBRuGhsQk6MbFXrNE.jpeg', 'cNK3MPGUoTTg6S0qD1x6VmzWfc.png'] },
    { name: 'BHC Wellness', place: 'Pitampura, North Delhi', tags: 'Google Business Profile Management · AEO · 2026',
      gap: 'A broad diagnostic and wellness offering, from Rs. 599 to Rs. 4,299, with a generic category, no catalogue and near-zero review velocity.',
      steps: ['Primary category fixed with 6 secondary specialisms', 'NAP made consistent across Justdial, Practo, Sulekha and IndiaMart', '30+ entry wellness and diagnostics catalogue, geo-tagged across North Delhi', 'QR review funnel routing happy patients to Google and others to private feedback', 'Replies to every review within 2 hours'],
      stats: [['Top 3', 'Wellness and diagnostic searches across Pitampura'], ['30D', 'To first measurable ranking movement'], ['4.8★', 'Target rating with managed replies']],
      quote: 'Within 30 days we were appearing in the local pack for wellness and diagnostic searches across Pitampura, Rani Bagh, Rohini and Shalimar Bagh.', who: 'Tanuj Kalra, Founder, Bhritii Health Care',
      live: 'https://maps.app.goo.gl/9hzHceDTD9AexiPh6', gal: ['vepFr5QsbXo0kRe2FI1t9jwFFaQ.png', '0n669yno8w4SG2UEetaD4WsJcbs.png', '9fP0g3STWATCSjZ8yxTPXdaaxIE.png', 'pjYmpCykTPWTac9obzNo0EezCNk.png'] },
    { name: 'Shahi Manjil', place: 'North York, Toronto', tags: 'AEO · Google Business Profile Management · GEO · 2026',
      gap: 'An elite 4.8-star restaurant with a keyword-stuffed name that risked suspension, zero posts, empty services and no booking link. Profile score: 58/100.',
      steps: ['Business name trimmed to the compliant storefront name', 'OpenTable booking and ordering links added to the profile', 'Primary category locked with 4 rich secondary categories', '15-entry service grid and 5 seeded Q&A pairs', 'LocalBusiness JSON-LD schema so ChatGPT, Gemini and Apple Maps can cite it'],
      stats: [['Top 3', 'Projected local pack placement within 60 days'], ['58→80+', 'Google Business Profile health score (target)'], ['4.8★', 'Across 4,300+ community reviews']],
      quote: 'Within weeks, our visibility signals fundamentally changed, establishing Shahi Manjil as a trusted entity that AI search tools and maps systems seamlessly recommend.', who: 'Dr Ghanim, Owner',
      live: 'https://share.google/7WkOqRz33Pkv0VK53', gal: ['iSAL2IX7QAaZxnIbt4YTYHLJfk.png', 'lKXUr9GOcwpbGahSO7m9FqDA3s.png', 'cVC6MfYWslCkniTStuGHCn3dg.png', 'YOFnO9zNH3A16SqNYcNV2aHxB4.png'] }
  ];
  const ov = $('#ov'); if (!ov) return; const inner = $('#ovIn'), vid = $('video', ov); let lastCard = null, isOpen = false;
  const insetFrom = el => { const r = el.getBoundingClientRect(); return `inset(${r.top}px ${innerWidth - r.right}px ${innerHeight - r.bottom}px ${r.left}px round 26px)`; };
  function open(i, card) {
    const c = CASES[i]; lastCard = card; isOpen = true;
    inner.innerHTML = `<span class="label"><span class="g">Case 0${i + 1}</span> · ${c.place}</span>
      <h2 id="ov-title" class="chroma">${c.name}</h2><span class="mono">${c.tags}</span>
      <div class="ov-stats">${c.stats.map(s => `<div><b>${s[0]}</b><span>${s[1]}</span></div>`).join('')}</div>
      <div class="ov-grid"><div style="display:grid;gap:18px;align-content:start"><span class="label">The gap</span><p style="font-size:20px;color:var(--paper)">${c.gap}</p>
        <blockquote>“${c.quote}”<span class="mono" style="display:block;margin-top:12px">${c.who}</span></blockquote></div>
        <div style="display:grid;gap:14px;align-content:start"><span class="label">What we did</span><ol class="ov-steps">${c.steps.map(s => `<li>${s}</li>`).join('')}</ol>
        <a class="btn pri" href="${c.live}" target="_blank" rel="noopener" style="justify-self:start;margin-top:10px">View live Google profile ↗</a></div></div>
      <div class="ov-gal">${c.gal.map(g => `<img src="${IMG(g)}?width=600" alt="${c.name} project work" loading="lazy">`).join('')}</div>`;
    $('.ov-scroll', ov).scrollTop = 0; CS.stopScroll(); vid.play().catch(() => {});
    gsap.timeline().set(ov, { visibility: 'visible', clipPath: insetFrom(card) })
      .to(ov, { clipPath: 'inset(0px 0px 0px 0px round 0px)', duration: 1.1, ease: 'expo.inOut' })
      .from($$('.ov-in > *', ov), { y: 40, autoAlpha: 0, stagger: .06, duration: 1 }, '-=.4');
    S.whoosh(); $('#ovClose').focus();
  }
  function close() {
    if (!isOpen) return; isOpen = false;
    gsap.to(ov, { clipPath: insetFrom(lastCard), duration: .9, ease: 'expo.inOut', onComplete: () => { gsap.set(ov, { visibility: 'hidden' }); vid.pause(); CS.startScroll(); lastCard.focus(); } });
  }
  $$('.case').forEach(c => c.addEventListener('click', () => open(+c.dataset.case, c)));
  $('#ovClose').addEventListener('click', close);
  addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  if (!REDUCE) gsap.from('.case', { y: 90, autoAlpha: 0, stagger: .12, duration: 1.4, scrollTrigger: { trigger: '.cases', start: 'top 80%' } });
})();

/* ============ TESTIMONIALS: drag (mouse), swipe (touch), arrows ============ */
(() => {
  const q = $('#quotes'); if (!q) return;
  const step = () => ($('.quote', q).offsetWidth + 20);
  $('#qPrev').addEventListener('click', () => q.scrollBy({ left: -step(), behavior: 'smooth' }));
  $('#qNext').addEventListener('click', () => q.scrollBy({ left: step(), behavior: 'smooth' }));
  if (FINE) { let down = false, sx = 0, sl = 0, moved = 0;
    q.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; moved = 0; sx = e.clientX; sl = q.scrollLeft; q.classList.add('drag'); });
    addEventListener('pointermove', e => { if (!down) return; const dx = e.clientX - sx; moved = Math.abs(dx); q.scrollLeft = sl - dx; });
    addEventListener('pointerup', () => { if (!down) return; down = false; q.classList.remove('drag'); }); }
  if (!REDUCE) gsap.from($$('.quote', q), { x: 120, autoAlpha: 0, stagger: .1, duration: 1.4, scrollTrigger: { trigger: q, start: 'top 85%' } });
})();

CS.runLoader(heroIntro);
})();
