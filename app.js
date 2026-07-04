/* ═══════════════════════════════════════════
   LUNARA — App JavaScript
   GSAP Animations + Lenis Smooth Scroll
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

  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((time) => lenis.raf(time * 1000));
  gsap.ticker.lagSmoothing(0);

  /* ─────────────────────────────────────────
     2. GSAP REGISTER
  if (typeof gsap !== 'undefined') {
       ───────────────────────────────────────── */
    gsap.registerPlugin(ScrollTrigger);

    /* ─────────────────────────────────────────
       3. HERO — Character-by-character headline
       ───────────────────────────────────────── */
    const allChars = gsap.utils.toArray('.char');

    gsap.to(allChars, {
      opacity: 1,
      y: '0%',
      duration: 0.8,
      stagger: 0.03,
      ease: 'power3.out',
      delay: 0.3,
    });

    // Scroll-out: characters slide back down
    gsap.to(allChars, {
      scrollTrigger: {
        trigger: '.hero',
        start: '40% top',
        end: 'bottom top',
        scrub: 1,
      },
      y: '-80%',
      opacity: 0,
      stagger: 0.01,
      ease: 'none',
      immediateRender: false
    });

    /* ─────────────────────────────────────────
       4. HERO — Watermark "LUNARA" Animation
       ───────────────────────────────────────── */
    const wmLetters = gsap.utils.toArray('.wm-letter');

    // Stagger-in on load
    gsap.to(wmLetters, {
      opacity: 1,
      y: 0,
      duration: 1.6,
      stagger: 0.08,
      ease: 'power3.out',
      delay: 0.1,
    });

    // Scroll: letters spread apart, rotate, and fade
    wmLetters.forEach((letter, i) => {
      const center = (wmLetters.length - 1) / 2;
      const offset = i - center;

      gsap.to(letter, {
        scrollTrigger: {
          trigger: '.hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 1.2,
        },
        x: offset * 70,
        y: -150 + Math.abs(offset) * 25,
        opacity: 0,
        scale: 1.2,
        rotateZ: offset * 3,
        ease: 'none',
        immediateRender: false
      });
    });

    /* ─────────────────────────────────────────
       5. HERO — General reveal-up elements
       ───────────────────────────────────────── */
    const heroReveals = document.querySelectorAll('.hero .reveal-up');
    heroReveals.forEach((el) => {
      const delay = parseFloat(getComputedStyle(el).getPropertyValue('--delay') || 0);
      gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 1,
        delay: 0.5 + delay,
        ease: 'power3.out',
      });
    });

    /* ─────────────────────────────────────────
       6. PARALLAX — Blobs
       ───────────────────────────────────────── */
    document.querySelectorAll('.hero__blob').forEach((blob, i) => {
      gsap.to(blob, {
        y: 60 + i * 50,
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
       7. SCROLL REVEALS — Sections
       ───────────────────────────────────────── */
    document.querySelectorAll('.features .reveal-up, .download .reveal-up, .stats .reveal-up, .pricing .reveal-up, .generic-page .reveal-up').forEach((el) => {
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
       8. FEATURE CARDS — Staggered with scale
       ───────────────────────────────────────── */
    const featureCards = gsap.utils.toArray('.feature-card');
    featureCards.forEach((card, i) => {
      gsap.to(card, {
        scrollTrigger: {
          trigger: card,
          start: 'top 90%',
          toggleActions: 'play none none none',
        },
        opacity: 1,
        y: 0,
        scale: 1,
        duration: 0.7,
        delay: (i % 3) * 0.1, // stagger per row
        ease: 'power3.out',
      });
    });

    // Subtle tilt on hover (GSAP-powered)
    featureCards.forEach((card) => {
      card.addEventListener('mouseenter', () => {
        gsap.to(card, {
          rotateX: -2,
          rotateY: 3,
          duration: 0.4,
          ease: 'power2.out',
          transformPerspective: 800,
        });
      });
      card.addEventListener('mouseleave', () => {
        gsap.to(card, {
          rotateX: 0,
          rotateY: 0,
          duration: 0.5,
          ease: 'power2.out',
        });
      });
    });

    /* ─────────────────────────────────────────
       9. STAT COUNTERS — Animated numbers
       ───────────────────────────────────────── */
    const statNumbers = document.querySelectorAll('.stat-card__number');
    statNumbers.forEach((el) => {
      const target = parseInt(el.dataset.target, 10);
      const suffix = el.dataset.suffix || '';

      ScrollTrigger.create({
        trigger: el,
        start: 'top 85%',
        once: true,
        onEnter: () => {
          const obj = { val: 0 };
          gsap.to(obj, {
            val: target,
            duration: 2,
            ease: 'power2.out',
            onUpdate: () => {
              el.textContent = Math.round(obj.val) + suffix;
            },
          });
        },
      });
    });

    /* ─────────────────────────────────────────
       10. DOWNLOAD — Watermark drift
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
       11. MARQUEE — Speed on scroll (GSAP)
       ───────────────────────────────────────── */
    const marqueeTrack = document.querySelector('.marquee__track');
    if (marqueeTrack) {
      gsap.to(marqueeTrack, {
        scrollTrigger: {
          trigger: '.marquee',
          start: 'top bottom',
          end: 'bottom top',
          scrub: 0.5,
        },
        x: '-200px',
        ease: 'none',
      });
    }

    /* ─────────────────────────────────────────
       12. NAVBAR — Scroll state
       ───────────────────────────────────────── */
    const navbar = document.getElementById('navbar');
    ScrollTrigger.create({
      start: 80,
      onUpdate: (self) => {
        navbar.classList.toggle('scrolled', self.scroll() > 80);
      },
    });

    /* ─────────────────────────────────────────
       13. MOBILE NAV TOGGLE
       ───────────────────────────────────────── */
    const burger = document.getElementById('navBurger');
    const mobileNav = document.getElementById('mobileNav');

    burger.addEventListener('click', () => {
      burger.classList.toggle('active');
      mobileNav.classList.toggle('open');
      document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
    });
    mobileNav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        burger.classList.remove('active');
        mobileNav.classList.remove('open');
        document.body.style.overflow = '';
      });
    });

    /* ─────────────────────────────────────────
       14. SMOOTH ANCHOR LINKS
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

    /* ─────────────────────────────────────────
       15. COUNTDOWN TIMER
       ───────────────────────────────────────── */
    const launchDate = new Date();
    launchDate.setDate(launchDate.getDate() + 14); // 14 days from now

    const timerDays = document.getElementById('timer-days');
    const timerHours = document.getElementById('timer-hours');
    const timerMins = document.getElementById('timer-mins');
    const timerSecs = document.getElementById('timer-secs');

    if (timerDays && timerHours && timerMins && timerSecs) {
      function updateTimer() {
        const now = new Date();
        const diff = Math.max(0, launchDate - now);

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const mins = Math.floor((diff / 1000 / 60) % 60);
        const secs = Math.floor((diff / 1000) % 60);

        timerDays.textContent = days.toString().padStart(2, '0');
        timerHours.textContent = hours.toString().padStart(2, '0');
        timerMins.textContent = mins.toString().padStart(2, '0');
        timerSecs.textContent = secs.toString().padStart(2, '0');
      }

      updateTimer();
      setInterval(updateTimer, 1000);
    }

    /* ─────────────────────────────────────────
       16. APPLE LIQUID GLASS (GSAP)
       ───────────────────────────────────────── */
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    document.querySelectorAll('.liquid-glass').forEach(el => {
      // Inject sheen element
      const sheen = document.createElement('div');
      sheen.classList.add('glass-sheen');
      el.appendChild(sheen);

      // Magnetic Hover & Sheen Sweep
      if (!prefersReducedMotion) {
        el.addEventListener('mousemove', (e) => {
          const rect = el.getBoundingClientRect();
          const x = e.clientX - rect.left - rect.width / 2;
          const y = e.clientY - rect.top - rect.height / 2;

          gsap.to(el, {
            x: x * 0.15,
            y: y * 0.15,
            duration: 0.6,
            ease: 'power3.out'
          });
        });

        el.addEventListener('mouseenter', () => {
          gsap.fromTo(sheen, 
            { x: -el.offsetWidth - 100 },
            { x: el.offsetWidth + 100, duration: 0.7, ease: 'power2.inOut' }
          );
        });

        el.addEventListener('mouseleave', () => {
          gsap.to(el, {
            x: 0,
            y: 0,
            duration: 0.8,
            ease: 'elastic.out(1, 0.3)'
          });
        });
      }

      // Press Scale
      el.addEventListener('mousedown', () => {
        gsap.to(el, {
          scale: prefersReducedMotion ? 0.98 : 0.95,
          duration: 0.3,
          ease: 'power2.out'
        });
      });

      el.addEventListener('mouseup', () => {
        gsap.to(el, {
          scale: 1,
          duration: 0.5,
          ease: prefersReducedMotion ? 'power2.out' : 'back.out(1.5)'
        });
      });

      el.addEventListener('mouseleave', () => {
        gsap.to(el, {
          scale: 1,
          duration: 0.5,
          ease: prefersReducedMotion ? 'power2.out' : 'back.out(1.5)'
        });
      });

      // Ripple Effect on click
      el.addEventListener('mousedown', (e) => {
        const rect = el.getBoundingClientRect();
        const rippleX = e.clientX - rect.left;
        const rippleY = e.clientY - rect.top;

        const ripple = document.createElement('div');
        ripple.classList.add('glass-ripple');
        ripple.style.left = `${rippleX}px`;
        ripple.style.top = `${rippleY}px`;
        ripple.style.width = ripple.style.height = `${Math.max(rect.width, rect.height) * 2}px`;
        el.appendChild(ripple);

        gsap.fromTo(ripple,
          { scale: 0, opacity: 0.6 },
          { scale: 1, opacity: 0, duration: 0.6, ease: 'power2.out', onComplete: () => ripple.remove() }
        );
      });
    });

    /* ─────────────────────────────────────────
       18. PAGE HERO ANIMATIONS (Product/Company)
       ───────────────────────────────────────── */
    const pageHeroWatermark = document.querySelector('.page-hero__watermark');
    if (pageHeroWatermark) {
      gsap.to(pageHeroWatermark, {
        opacity: 1,
        duration: 2,
        delay: 0.2,
        ease: 'power2.out',
      });

      // Scroll parallax for watermark
      gsap.to(pageHeroWatermark, {
        scrollTrigger: {
          trigger: '.page-hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 1.5,
        },
        y: -100,
        opacity: 0,
        ease: 'none',
        immediateRender: false,
      });
    }

    const pageHeroEyebrow = document.querySelector('.page-hero__eyebrow');
    if (pageHeroEyebrow) {
      gsap.to(pageHeroEyebrow, {
        opacity: 1,
        y: 0,
        duration: 0.8,
        delay: 0.3,
        ease: 'power3.out',
      });
    }

    const pageHeroTitle = document.querySelector('.page-hero__title');
    if (pageHeroTitle) {
      gsap.to(pageHeroTitle, {
        opacity: 1,
        y: 0,
        duration: 1,
        delay: 0.5,
        ease: 'power3.out',
      });
    }

    const pageHeroSub = document.querySelector('.page-hero__sub');
    if (pageHeroSub) {
      gsap.to(pageHeroSub, {
        opacity: 1,
        y: 0,
        duration: 0.9,
        delay: 0.7,
        ease: 'power3.out',
      });
    }

    // Scroll-out for page hero content
    const pageHero = document.querySelector('.page-hero');
    if (pageHero) {
      gsap.to('.page-hero__content', {
        scrollTrigger: {
          trigger: '.page-hero',
          start: '30% top',
          end: 'bottom top',
          scrub: 1,
        },
        y: -80,
        opacity: 0,
        ease: 'none',
      });
    }

    /* ─────────────────────────────────────────
       19. SCROLL REVEAL OBSERVER (sr-* classes)
       ───────────────────────────────────────── */
    const srElements = document.querySelectorAll('.sr-fade-up, .sr-fade-left, .sr-fade-right, .sr-scale-in');
    if (srElements.length > 0) {
      const srObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('sr-visible');
            srObserver.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px',
      });

      srElements.forEach((el) => srObserver.observe(el));
    }

    /* ─────────────────────────────────────────
       20. BLOB PARALLAX (all pages)
       ───────────────────────────────────────── */
    document.querySelectorAll('.page-hero .hero__blob, .features .hero__blob, .pricing .hero__blob, .generic-page .hero__blob').forEach((blob, i) => {
      gsap.to(blob, {
        y: 40 + i * 30,
        ease: 'none',
        scrollTrigger: {
          trigger: blob.closest('section') || blob.parentElement,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1.5,
        },
      });
    });

    /* ─────────────────────────────────────────
       21. TOAST NOTIFICATIONS
       ───────────────────────────────────────── */
    const toast = document.getElementById('toast');
    let toastTimeout;

    document.querySelectorAll('a[href="#coming-soon"]').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        
        if (toast) {
          clearTimeout(toastTimeout);
          toast.classList.add('show');
          
          toastTimeout = setTimeout(() => {
            toast.classList.remove('show');
          }, 3000);
        }
      });
    });

    /* ─────────────────────────────────────────
       22. CONTACT FORM HANDLER
       ───────────────────────────────────────── */
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
      contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('contact-name').value.trim();
        const email = document.getElementById('contact-email').value.trim();
        const subject = document.getElementById('contact-subject').value;
        const message = document.getElementById('contact-message').value.trim();

        // Build mailto link
        const mailTo = 'lunarahealthtracker@gmail.com';
        const mailSubject = encodeURIComponent(`[${subject}] from ${name}`);
        const mailBody = encodeURIComponent(`Name: ${name}\nEmail: ${email}\nSubject: ${subject}\n\nMessage:\n${message}`);
        
        window.location.href = `mailto:${mailTo}?subject=${mailSubject}&body=${mailBody}`;

        // Show success state
        contactForm.innerHTML = `
          <div class="contact-form__success show">
            <div class="contact-form__success-icon">
              <svg viewBox="0 0 24 24" fill="#fff" width="28" height="28"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
            </div>
            <h4>Message Ready!</h4>
            <p>Your email client should open with the message. If it doesn't, you can email us directly at <strong>lunarahealthtracker@gmail.com</strong></p>
          </div>
        `;
      });
    }

})();
