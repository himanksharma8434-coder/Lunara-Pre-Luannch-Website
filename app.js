/* ═══════════════════════════════════════════
   LUNARA — App JavaScript
   GSAP/ScrollTrigger + Lenis + Watermark Animation
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
     2. GSAP — Register Plugin
     ───────────────────────────────────────── */
  gsap.registerPlugin(ScrollTrigger);

  /* ─────────────────────────────────────────
     3. WATERMARK — Massive "LUNARA" Text Animation
     ───────────────────────────────────────── */
  const wmLetters = gsap.utils.toArray('.wm-letter');

  // ── Initial stagger-in animation ──
  gsap.to(wmLetters, {
    opacity: 1,
    y: 0,
    duration: 1.4,
    stagger: 0.08,
    ease: 'power3.out',
    delay: 0.1,
  });

  // ── Scroll: letters spread apart, drift, and fade ──
  wmLetters.forEach((letter, i) => {
    const centerIndex = (wmLetters.length - 1) / 2;
    const offsetFromCenter = i - centerIndex;

    gsap.to(letter, {
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 1.2,
      },
      x: offsetFromCenter * 60,
      y: -120 + Math.abs(offsetFromCenter) * 20,
      opacity: 0,
      scale: 1.15,
      rotateZ: offsetFromCenter * 2,
      ease: 'none',
    });
  });

  /* ─────────────────────────────────────────
     4. GSAP — Hero Reveal Animations
     ───────────────────────────────────────── */
  const heroReveals = document.querySelectorAll('.hero .reveal-up');
  heroReveals.forEach((el) => {
    const delay = parseFloat(getComputedStyle(el).getPropertyValue('--delay') || 0);
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 1,
      delay: 0.4 + delay,
      ease: 'power3.out',
    });
  });

  /* ─────────────────────────────────────────
     5. GSAP — Scroll-Triggered Reveals
     ───────────────────────────────────────── */
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

  /* ─────────────────────────────────────────
     6. GSAP — Feature Cards Stagger
     ───────────────────────────────────────── */
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
     7. GSAP — Parallax Blobs
     ───────────────────────────────────────── */
  const blobs = document.querySelectorAll('.hero__blob');
  blobs.forEach((blob, i) => {
    const speed = 60 + i * 50;
    gsap.to(blob, {
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

  /* ─────────────────────────────────────────
     8. GSAP — Hero Logo Parallax
     ───────────────────────────────────────── */
  const heroLogo = document.querySelector('.hero__logo-img');
  if (heroLogo) {
    gsap.to(heroLogo, {
      y: -40,
      scale: 0.9,
      opacity: 0.5,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero',
        start: '30% top',
        end: 'bottom top',
        scrub: 1,
      },
    });
  }

  /* ─────────────────────────────────────────
     9. GSAP — Download Watermark Parallax
     ───────────────────────────────────────── */
  const dlWatermark = document.querySelector('.download__watermark');
  if (dlWatermark) {
    gsap.fromTo(dlWatermark,
      { x: '5%' },
      {
        x: '-5%',
        ease: 'none',
        scrollTrigger: {
          trigger: '.download',
          start: 'top bottom',
          end: 'bottom top',
          scrub: 2,
        },
      }
    );
  }

  /* ─────────────────────────────────────────
     10. NAVBAR — Scroll State
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
     11. MOBILE NAV TOGGLE
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

  // Close on link click
  mobileNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      burger.classList.remove('active');
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  /* ─────────────────────────────────────────
     12. SMOOTH SCROLL — Anchor Links
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
