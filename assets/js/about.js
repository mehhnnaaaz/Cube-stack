/* CubeStack AI — about page */
(() => {
'use strict';
const CS = window.CS; if (!CS || !CS.ready) return;
const { REDUCE, FINE, $, $$, clamp, pointer: P } = CS;

const intro = () => {
  if (REDUCE) return;
  gsap.timeline()
    .from('.ahero h1 .ln>span', { yPercent: 115, rotate: 4, duration: 1.6, ease: 'expo.out', stagger: .1 })
    .from('.ahero .label, .ahero .lede, .ahero-meta, .ahero .ctas', { y: 30, autoAlpha: 0, duration: 1.2, stagger: .08 }, '-=1.2')
    .from('.ahero-art', { y: 80, autoAlpha: 0, scale: .9, duration: 1.8, ease: 'expo.out' }, '-=1.5')
    .from('.hdr .wrap > *', { y: -30, autoAlpha: 0, duration: 1, stagger: .08 }, '-=1.4');
};

/* hero render: pointer tilt + idle float + scroll drift */
(() => {
  const img = $('#aCube'); if (!img || REDUCE) return;
  if (FINE) { const xt = gsap.quickTo(img, 'x', { duration: 1.2, ease: 'power3.out' }), yt = gsap.quickTo(img, 'y', { duration: 1.2, ease: 'power3.out' });
    addEventListener('pointermove', () => { xt(P.nx * 24); yt(-P.ny * 18); }, { passive: true }); }
  gsap.to(img, { yPercent: -3, duration: 3.2, ease: 'sine.inOut', yoyo: true, repeat: -1 });
  gsap.to('.ahero-art', { yPercent: -18, ease: 'none', scrollTrigger: { trigger: '.ahero', start: 'top top', end: 'bottom top', scrub: true } });
})();

/* feature renders drift slightly against the scroll */
if (!REDUCE) $$('.feature-art img').forEach(img => gsap.fromTo(img, { yPercent: 6 }, { yPercent: -6, ease: 'none', scrollTrigger: { trigger: img, start: 'top bottom', end: 'bottom top', scrub: true } }));

/* values cube: turns as you scroll through */
if (!REDUCE) gsap.fromTo('#valCube', { rotate: -14, scale: .9 }, { rotate: 14, scale: 1.05, ease: 'none', scrollTrigger: { trigger: '.values', start: 'top bottom', end: 'bottom top', scrub: true } });

/* industries: image preview follows the pointer (desktop); inline thumbnails on touch (CSS) */
(() => {
  const peek = $('#peek'), list = $('#ind'); if (!peek || !list || !FINE || REDUCE) return;
  const imgs = $$('img', peek), xt = gsap.quickTo(peek, 'x', { duration: .6, ease: 'power3.out' }), yt = gsap.quickTo(peek, 'y', { duration: .6, ease: 'power3.out' }), rt = gsap.quickTo(peek, 'rotation', { duration: .8, ease: 'power3.out' });
  let lastX = 0;
  list.addEventListener('pointermove', e => { xt(e.clientX - 150); yt(e.clientY - 190); rt(clamp((e.clientX - lastX) * .4, -10, 10)); lastX = e.clientX; });
  $$('.ind-row', list).forEach(row => row.addEventListener('pointerenter', () => { imgs.forEach((im, i) => im.classList.toggle('on', i === +row.dataset.img)); CS.Sound.hover(); }));
  list.addEventListener('pointerenter', e => { gsap.set(peek, { x: e.clientX - 150, y: e.clientY - 190 }); gsap.to(peek, { opacity: 1, scale: 1, duration: .5, ease: 'expo.out' }); });
  list.addEventListener('pointerleave', () => gsap.to(peek, { opacity: 0, scale: .6, duration: .4, ease: 'power3.in' }));
})();
if (!REDUCE) gsap.from('.ind-row', { y: 40, autoAlpha: 0, stagger: .08, duration: 1.2, scrollTrigger: { trigger: '#ind', start: 'top 85%' } });

/* team cards: 3D tilt + violet spotlight (desktop) */
if (FINE && !REDUCE) $$('[data-tilt]').forEach(card => {
  const rx = gsap.quickTo(card, 'rotationX', { duration: .8, ease: 'power3.out' }), ry = gsap.quickTo(card, 'rotationY', { duration: .8, ease: 'power3.out' });
  gsap.set(card, { transformPerspective: 1200 });
  card.addEventListener('pointermove', e => { const r = card.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
    rx((.5 - y) * 8); ry((x - .5) * 10); card.style.setProperty('--mx', x * 100 + '%'); card.style.setProperty('--my', y * 100 + '%'); });
  card.addEventListener('pointerleave', () => { rx(0); ry(0); });
});
if (!REDUCE) gsap.from('.member', { y: 100, autoAlpha: 0, stagger: .15, duration: 1.4, scrollTrigger: { trigger: '.team', start: 'top 85%' } });

/* process: earlier cards recede as the next one stacks on top */
if (!REDUCE) {
  const cards = $$('.pcard');
  cards.forEach((c, i) => { if (i === cards.length - 1) return;
    gsap.to(c, { scale: .92 + i * .015, filter: 'brightness(.72)', ease: 'none', scrollTrigger: { trigger: cards[i + 1], start: 'top bottom', end: 'top 30%', scrub: true } }); });
}

CS.runLoader(intro);
})();
