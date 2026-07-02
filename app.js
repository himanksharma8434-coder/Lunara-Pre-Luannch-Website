/* ═══════════════════════════════════════════
   LUNARA — App JavaScript
   Three.js · GSAP/ScrollTrigger · Lenis
   ═══════════════════════════════════════════ */

(function () {
  'use strict';

  /* ─────────────────────────────────────────
     1. LENIS SMOOTH SCROLL
     ───────────────────────────────────────── */
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,
    touchMultiplier: 1.5,
  });

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  // Connect Lenis to GSAP ScrollTrigger
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((time) => lenis.raf(time * 1000));
  gsap.ticker.lagSmoothing(0);

  /* ─────────────────────────────────────────
     2. THREE.JS — Interactive 3D Moon / Icosahedron
     ───────────────────────────────────────── */
  const canvas = document.getElementById('heroCanvas');
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(
    50,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  camera.position.z = 5;

  const renderer = new THREE.WebGLRenderer({
    canvas,
    alpha: true,
    antialias: true,
  });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // ── Main Icosahedron (solid body) ──
  const icoGeo = new THREE.IcosahedronGeometry(1.5, 1);
  const icoMat = new THREE.MeshStandardMaterial({
    color: 0xff007f,
    emissive: 0x4a0028,
    roughness: 0.3,
    metalness: 0.7,
    flatShading: true,
  });
  const icoMesh = new THREE.Mesh(icoGeo, icoMat);
  scene.add(icoMesh);

  // ── Wireframe overlay ──
  const wireGeo = new THREE.IcosahedronGeometry(1.65, 1);
  const wireMat = new THREE.MeshBasicMaterial({
    color: 0xff5cad,
    wireframe: true,
    transparent: true,
    opacity: 0.18,
  });
  const wireMesh = new THREE.Mesh(wireGeo, wireMat);
  scene.add(wireMesh);

  // ── Outer glow ring ──
  const ringGeo = new THREE.TorusGeometry(2.2, 0.015, 16, 100);
  const ringMat = new THREE.MeshBasicMaterial({
    color: 0xff007f,
    transparent: true,
    opacity: 0.25,
  });
  const ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 2.5;
  scene.add(ringMesh);

  // ── Second ring ──
  const ring2Geo = new THREE.TorusGeometry(2.6, 0.008, 16, 120);
  const ring2Mat = new THREE.MeshBasicMaterial({
    color: 0xff5cad,
    transparent: true,
    opacity: 0.12,
  });
  const ring2Mesh = new THREE.Mesh(ring2Geo, ring2Mat);
  ring2Mesh.rotation.x = Math.PI / 1.8;
  ring2Mesh.rotation.y = Math.PI / 4;
  scene.add(ring2Mesh);

  // ── Floating particles ──
  const particleCount = 200;
  const particleGeo = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);
  for (let i = 0; i < particleCount * 3; i++) {
    positions[i] = (Math.random() - 0.5) * 12;
  }
  particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  const particleMat = new THREE.PointsMaterial({
    color: 0xff007f,
    size: 0.015,
    transparent: true,
    opacity: 0.6,
    sizeAttenuation: true,
  });
  const particles = new THREE.Points(particleGeo, particleMat);
  scene.add(particles);

  // ── Lights ──
  const ambientLight = new THREE.AmbientLight(0x1a0a2e, 0.5);
  scene.add(ambientLight);

  const pointLight = new THREE.PointLight(0xff007f, 2, 15);
  pointLight.position.set(3, 3, 4);
  scene.add(pointLight);

  const pointLight2 = new THREE.PointLight(0x6400c8, 1.5, 12);
  pointLight2.position.set(-3, -2, 3);
  scene.add(pointLight2);

  const rimLight = new THREE.PointLight(0xff5cad, 1, 10);
  rimLight.position.set(0, 4, -2);
  scene.add(rimLight);

  // ── Mouse tracking ──
  const mouse = { x: 0, y: 0 };
  const targetRotation = { x: 0, y: 0 };

  document.addEventListener('mousemove', (e) => {
    mouse.x = (e.clientX / window.innerWidth - 0.5) * 2;
    mouse.y = (e.clientY / window.innerHeight - 0.5) * 2;
  });

  // ── Responsive ──
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  // ── Render loop ──
  const clock = new THREE.Clock();
  function animate() {
    requestAnimationFrame(animate);
    const elapsed = clock.getElapsedTime();

    // Smooth mouse-tracking rotation
    targetRotation.x += (mouse.y * 0.3 - targetRotation.x) * 0.04;
    targetRotation.y += (mouse.x * 0.3 - targetRotation.y) * 0.04;

    // Icosahedron
    icoMesh.rotation.x = elapsed * 0.15 + targetRotation.x;
    icoMesh.rotation.y = elapsed * 0.2 + targetRotation.y;

    // Wireframe
    wireMesh.rotation.x = elapsed * 0.12 + targetRotation.x;
    wireMesh.rotation.y = elapsed * 0.18 + targetRotation.y;

    // Rings
    ringMesh.rotation.z = elapsed * 0.1;
    ring2Mesh.rotation.z = -elapsed * 0.08;

    // Particles drift
    particles.rotation.y = elapsed * 0.02;
    particles.rotation.x = elapsed * 0.01;

    // Pulsing emissive
    const pulse = Math.sin(elapsed * 1.5) * 0.5 + 0.5;
    icoMat.emissiveIntensity = 0.3 + pulse * 0.4;

    renderer.render(scene, camera);
  }
  animate();

  /* ─────────────────────────────────────────
     3. GSAP — Reveal Animations
     ───────────────────────────────────────── */
  gsap.registerPlugin(ScrollTrigger);

  // ── Staggered hero reveals ──
  const heroReveals = document.querySelectorAll('.hero .reveal-up');
  heroReveals.forEach((el) => {
    const delay = parseFloat(getComputedStyle(el).getPropertyValue('--delay') || 0);
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 1,
      delay: 0.3 + delay,
      ease: 'power3.out',
    });
  });

  // ── Scroll-triggered reveals for other sections ──
  const scrollReveals = document.querySelectorAll(
    '.features .reveal-up, .download .reveal-up'
  );
  scrollReveals.forEach((el) => {
    const delay = parseFloat(getComputedStyle(el).getPropertyValue('--delay') || 0);
    gsap.to(el, {
      scrollTrigger: {
        trigger: el,
        start: 'top 85%',
        toggleActions: 'play none none none',
      },
      opacity: 1,
      y: 0,
      duration: 0.9,
      delay,
      ease: 'power3.out',
    });
  });

  // ── Feature cards stagger on scroll ──
  const featureCards = gsap.utils.toArray('.feature-card');
  featureCards.forEach((card, i) => {
    gsap.to(card, {
      scrollTrigger: {
        trigger: card,
        start: 'top 88%',
        toggleActions: 'play none none none',
      },
      opacity: 1,
      y: 0,
      duration: 0.8,
      delay: i * 0.12,
      ease: 'power3.out',
    });
  });

  /* ─────────────────────────────────────────
     4. GSAP — Parallax Orbs
     ───────────────────────────────────────── */
  const orbs = document.querySelectorAll('.hero__orb');
  orbs.forEach((orb, i) => {
    const speed = 80 + i * 60;
    gsap.to(orb, {
      y: speed,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 1.5,
      },
    });
  });

  // ── 3D object fades/moves as user scrolls past hero ──
  gsap.to(canvas, {
    opacity: 0,
    y: -80,
    ease: 'none',
    scrollTrigger: {
      trigger: '.hero',
      start: '60% top',
      end: 'bottom top',
      scrub: 1,
    },
  });

  /* ─────────────────────────────────────────
     5. NAVBAR — Scroll State
     ───────────────────────────────────────── */
  const navbar = document.getElementById('navbar');
  ScrollTrigger.create({
    start: 80,
    onUpdate: (self) => {
      if (self.scroll() > 80) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    },
  });

  /* ─────────────────────────────────────────
     6. MOBILE NAV TOGGLE
     ───────────────────────────────────────── */
  const burger = document.getElementById('navBurger');
  const mobileNav = document.getElementById('mobileNav');

  burger.addEventListener('click', () => {
    burger.classList.toggle('active');
    mobileNav.classList.toggle('open');
    document.body.style.overflow = mobileNav.classList.contains('open')
      ? 'hidden'
      : '';
  });

  // Close mobile nav on link click
  mobileNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      burger.classList.remove('active');
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  /* ─────────────────────────────────────────
     7. SMOOTH SCROLL — Anchor Links
     ───────────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        lenis.scrollTo(target, { offset: -80 });
      }
    });
  });

})();
