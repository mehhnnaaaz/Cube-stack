/* CubeStack AI — shared site script */
(function () {
  document.documentElement.classList.add('js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* header turns solid on scroll */
  const hdr = $('.hdr');
  const access = $('.access');
  const onScroll = () => {
    if (hdr) hdr.classList.toggle('solid', scrollY > 30);
    if (access) access.classList.toggle('show', scrollY > innerHeight * .6);
  };
  onScroll(); addEventListener('scroll', onScroll, { passive: true });

  /* local time clocks: <span data-clock="Asia/Kolkata"> */
  const tick = () => $$('[data-clock]').forEach(el => {
    el.textContent = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: el.dataset.clock }).format(new Date());
  });
  tick(); setInterval(tick, 15000);
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  /* mobile menu */
  const menu = $('#menu'), openBtn = $('#menu-open');
  if (menu && openBtn) {
    const vid = $('video', menu);
    const set = open => {
      menu.classList.toggle('open', open);
      menu.setAttribute('aria-hidden', String(!open));
      openBtn.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
      if (vid) open ? vid.play().catch(() => {}) : vid.pause();
      (open ? $('#menu-close') : openBtn).focus();
    };
    openBtn.addEventListener('click', () => set(true));
    $('#menu-close').addEventListener('click', () => set(false));
    $$('a', menu).forEach(a => a.addEventListener('click', () => set(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape' && menu.classList.contains('open')) set(false); });
  }

  /* reveal: content is visible at rest; elements below the fold get a gentle lift */
  if (!reduce && 'IntersectionObserver' in window) {
    const els = $$('.rv').filter(el => el.getBoundingClientRect().top > innerHeight);
    els.forEach(el => el.classList.add('pre'));
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); }
    }), { rootMargin: '0px 0px -8% 0px' });
    els.forEach(el => io.observe(el));
  }

  /* pause background videos when off screen */
  if ('IntersectionObserver' in window) {
    const vio = new IntersectionObserver(es => es.forEach(e => {
      const v = e.target;
      if (e.isIntersecting && !reduce) v.play().catch(() => {}); else v.pause();
    }), { threshold: .05 });
    $$('video[data-bg]').forEach(v => vio.observe(v));
  }

  /* copy buttons */
  $$('.copy-btn').forEach(b => b.addEventListener('click', () => {
    const done = () => { const t = b.textContent; b.textContent = 'Copied'; setTimeout(() => b.textContent = t, 1400); };
    const fallback = () => { const r = document.createRange(); r.selectNodeContents(b.previousElementSibling); const s = getSelection(); s.removeAllRanges(); s.addRange(r); };
    navigator.clipboard ? navigator.clipboard.writeText(b.dataset.copy).then(done, fallback) : fallback();
  }));

  /* geo-grid rank scan (illustrative sample) */
  const grid = $('#grid');
  if (grid) {
    const avg = $('#avg'), dots = [];
    for (let i = 0; i < 49; i++) { const d = document.createElement('span'); d.className = 'dot'; grid.appendChild(d); dots.push(d); }
    const rankFor = (i, mode) => {
      const x = i % 7 - 3, y = Math.floor(i / 7) - 3, dist = Math.hypot(x, y), j = ((i * 37) % 5) - 2;
      if (mode === 'after') return Math.max(1, Math.round(dist < 2.3 ? 1 : dist * 1.1 - 1.3 + (j > 1 ? 1 : 0)));
      return Math.max(6, Math.round(9 + dist * 2.4 + j));
    };
    const cls = r => r === 1 ? 'r1' : r <= 3 ? 'r2' : r <= 7 ? 'r3' : r <= 12 ? 'r4' : 'r5';
    const paint = mode => {
      let sum = 0;
      dots.forEach((d, i) => {
        const r = rankFor(i, mode); sum += Math.min(r, 20);
        const delay = reduce ? 0 : (Math.abs(i % 7 - 3) + Math.abs(Math.floor(i / 7) - 3)) * 60;
        setTimeout(() => { d.className = 'dot ' + cls(r); d.textContent = r > 20 ? '20+' : r; }, delay);
      });
      avg.textContent = (sum / 49).toFixed(1);
      $$('.seg button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mode === mode)));
    };
    $$('.seg button').forEach(b => b.addEventListener('click', () => paint(b.dataset.mode)));
    paint('after');
  }

  /* testimonial tabs */
  const tabs = $$('.q-tabs button');
  if (tabs.length) {
    const show = i => {
      tabs.forEach((t, k) => t.setAttribute('aria-selected', String(k === i)));
      $$('.quotes .q').forEach((q, k) => q.hidden = k !== i);
    };
    tabs.forEach((t, i) => t.addEventListener('click', () => show(i)));
    show(0);
  }

  /* about: process steps swap the sticky image */
  const steps = $$('.step[data-step]');
  if (steps.length && 'IntersectionObserver' in window) {
    const imgs = $$('.process-media img');
    const label = $('.process-media .mono');
    const sio = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      const n = +e.target.dataset.step;
      steps.forEach((s, k) => s.classList.toggle('on', k === n));
      imgs.forEach((im, k) => im.classList.toggle('on', k === n));
      if (label) label.textContent = 'Step 0' + (n + 1) + ' / 04';
    }), { rootMargin: '-45% 0px -45% 0px' });
    steps.forEach(s => sio.observe(s));
  }

  /* forms: build a WhatsApp or email message; nothing is sent until the visitor sends it.
     To receive submissions directly, set data-endpoint on the form (e.g. a Formspree or Web3Forms URL). */
  $$('form[data-brief]').forEach(form => form.addEventListener('submit', async e => {
    e.preventDefault();
    const out = $('.form-out', form);
    const data = Object.fromEntries(new FormData(form));
    const missing = $$('[required]', form).find(f => !f.value.trim());
    out.hidden = false;
    if (missing) { out.innerHTML = '<span>Please fill in ' + (missing.dataset.label || 'the required fields') + '.</span>'; missing.focus(); return; }
    if (form.dataset.endpoint) {
      try {
        const r = await fetch(form.dataset.endpoint, { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) });
        if (r.ok) { out.innerHTML = '<strong>Thanks, your message reached us.</strong><span>We will reply at ' + (data.email || 'your email') + '.</span>'; form.reset(); return; }
      } catch (_) { /* fall through to WhatsApp */ }
    }
    const lines = Object.entries(data).filter(([, v]) => String(v).trim()).map(([k, v]) => k[0].toUpperCase() + k.slice(1) + ': ' + v);
    const text = "Hi CubeStack AI, I'd like to talk about growing my business.\n" + lines.join('\n');
    out.innerHTML = '<strong>Your message is ready.</strong><span>Send it on WhatsApp or by email, whichever you prefer.</span>';
    const row = document.createElement('div'); row.className = 'cta-row';
    const wa = document.createElement('a'); wa.className = 'btn lime sm'; wa.target = '_blank'; wa.rel = 'noopener';
    wa.href = 'https://wa.me/919577297297?text=' + encodeURIComponent(text); wa.textContent = 'Send on WhatsApp';
    const em = document.createElement('a'); em.className = 'btn sm';
    em.href = 'mailto:admin@cubestackai.com?subject=' + encodeURIComponent(data.subject || 'Website enquiry') + '&body=' + encodeURIComponent(text); em.textContent = 'Send by email';
    row.append(wa, em); out.appendChild(row);
  }));
})();
