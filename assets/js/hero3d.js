/* CubeStack AI — home hero: glossy stacked cubes (Three.js r128) */
(function () {
  const canvas = document.getElementById('gl');
  if (!window.THREE || !canvas) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true }); } catch (e) { return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.outputEncoding = THREE.sRGBEncoding;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(32, 1, .1, 100);
  camera.position.set(0, 0, 14);

  /* studio environment: soft white panels with lime and violet glows */
  const ec = document.createElement('canvas'); ec.width = 1024; ec.height = 512;
  const g = ec.getContext('2d');
  g.fillStyle = '#07070a'; g.fillRect(0, 0, 1024, 512);
  const blob = (x, y, r, c) => { const gr = g.createRadialGradient(x, y, 0, x, y, r); gr.addColorStop(0, c); gr.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = gr; g.fillRect(0, 0, 1024, 512); };
  blob(240, 130, 230, 'rgba(255,255,255,.95)');
  blob(760, 170, 260, 'rgba(211,255,60,.95)');
  blob(520, 430, 280, 'rgba(125,77,255,1)');
  blob(950, 400, 160, 'rgba(255,255,255,.55)');
  const envTex = new THREE.CanvasTexture(ec);
  envTex.mapping = THREE.EquirectangularReflectionMapping;
  envTex.encoding = THREE.sRGBEncoding;
  scene.environment = new THREE.PMREMGenerator(renderer).fromEquirectangular(envTex).texture;
  scene.add(new THREE.AmbientLight(0xffffff, .25));
  const key = new THREE.DirectionalLight(0xffffff, 1.3); key.position.set(4, 6, 6); scene.add(key);
  const rim = new THREE.PointLight(0x7d4dff, 30, 30); rim.position.set(-5, -2, 4); scene.add(rim);

  function roundedBox(size, r, bevel) {
    const s = size / 2 - r, sh = new THREE.Shape();
    sh.moveTo(-s, -s - r); sh.lineTo(s, -s - r); sh.quadraticCurveTo(s + r, -s - r, s + r, -s);
    sh.lineTo(s + r, s); sh.quadraticCurveTo(s + r, s + r, s, s + r); sh.lineTo(-s, s + r);
    sh.quadraticCurveTo(-s - r, s + r, -s - r, s); sh.lineTo(-s - r, -s); sh.quadraticCurveTo(-s - r, -s - r, -s, -s - r);
    const geo = new THREE.ExtrudeGeometry(sh, { depth: size - bevel * 2, bevelEnabled: true, bevelSize: bevel, bevelThickness: bevel, bevelSegments: 8, curveSegments: 12 });
    geo.center(); geo.computeVertexNormals(); return geo;
  }
  const chrome = new THREE.MeshPhysicalMaterial({ color: 0xf2f2ee, metalness: 1, roughness: .12, clearcoat: 1, clearcoatRoughness: .05 });
  const lime = new THREE.MeshPhysicalMaterial({ color: 0xd3ff3c, metalness: .2, roughness: .2, clearcoat: 1, clearcoatRoughness: .08, emissive: 0x1d2600 });
  const glass = new THREE.MeshPhysicalMaterial({ color: 0xb9a2ff, metalness: .1, roughness: .05, transmission: .9, clearcoat: 1, transparent: true, opacity: .95 });

  const group = new THREE.Group(); scene.add(group);
  const stack = [
    { size: 2.4, mat: chrome, y: -1.7, ry: .2 },
    { size: 1.8, mat: glass, y: .45, ry: .62 },
    { size: 1.25, mat: lime, y: 2.05, ry: 1.0 }
  ].map((c, i) => {
    const m = new THREE.Mesh(roundedBox(c.size, c.size * .14, c.size * .08), c.mat);
    m.position.y = c.y; m.rotation.y = c.ry; m.userData = { baseY: c.y, ry: c.ry, i };
    group.add(m); return m;
  });

  const props = [];
  const add = (geo, mat, x, y, z, s) => { const m = new THREE.Mesh(geo, mat); m.position.set(x, y, z); m.scale.setScalar(s); m.userData = { y, sp: .4 + Math.random() * .6, ph: Math.random() * 6 }; scene.add(m); props.push(m); };
  add(new THREE.TorusGeometry(1, .32, 32, 96), chrome, 2.4, 2.9, -2, .5);
  add(new THREE.SphereGeometry(1, 48, 48), lime, 6.2, -1.9, -1, .38);
  add(roundedBox(1, .16, .08), glass, 6.6, 2.7, -3, .5);
  add(new THREE.CylinderGeometry(.42, .42, 1.4, 48), chrome, 2.6, -3.1, -4, .6);

  let mx = 0, my = 0, tx = 0, ty = 0;
  addEventListener('pointermove', e => { tx = e.clientX / innerWidth - .5; ty = e.clientY / innerHeight - .5; }, { passive: true });

  function layout() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix();
    const narrow = w < 900;
    const halfH = Math.tan(THREE.MathUtils.degToRad(16)) * 14, perPx = 2 * halfH / h;
    if (narrow) {
      group.position.set(0, (h / 2 - 190) * perPx, 0);
      group.scale.setScalar(Math.min(.48, 220 * perPx / 5.6));
    } else {
      group.position.set(halfH * camera.aspect * .58, .5, 0);
      group.scale.setScalar(.6);
    }
    props.forEach((p, i) => p.visible = !narrow || i < 2);
    if (narrow) { props[0].position.x = -2.2; props[1].position.x = 2.4; }
  }
  layout(); addEventListener('resize', layout);

  let visible = true;
  new IntersectionObserver(([e]) => visible = e.isIntersecting).observe(canvas);
  const clock = new THREE.Clock();
  (function frame() {
    requestAnimationFrame(frame);
    if (!visible) return;
    const t = reduce ? 0 : clock.getElapsedTime();
    mx += (tx - mx) * .05; my += (ty - my) * .05;
    group.rotation.y = t * .18 + mx * .6;
    group.rotation.x = -.12 + my * .25;
    stack.forEach(m => { m.position.y = m.userData.baseY + Math.sin(t * 1.1 + m.userData.i * .9) * .12; m.rotation.y = m.userData.ry + Math.sin(t * .5 + m.userData.i) * .25; });
    props.forEach(p => { p.position.y = p.userData.y + Math.sin(t * p.userData.sp + p.userData.ph) * .3; p.rotation.x = t * p.userData.sp * .6; p.rotation.y = t * p.userData.sp * .8; });
    renderer.render(scene, camera);
  })();
})();
