import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract head and navbar (everything up to the end of <nav>)
head_match = re.search(r'([\s\S]*?</nav>)', content)
head_part = head_match.group(1) if head_match else ""

# Extract mobile nav
mobile_nav_match = re.search(r'(<div class="mobile-nav" id="mobileNav">[\s\S]*?</div>)', content)
mobile_nav_part = mobile_nav_match.group(1) if mobile_nav_match else ""

# Extract footer and scripts
footer_match = re.search(r'(<!-- ═══════════════════════════════════════════\s*FOOTER[\s\S]*)', content)
footer_part = footer_match.group(1) if footer_match else ""

pricing_content = """
  <!-- ═══════════════════════════════════════════
       PRICING / SUBSCRIPTION
  ═══════════════════════════════════════════ -->
  <section class="pricing" id="pricing" style="padding-top: 80px; min-height: 80vh;">
    <div class="hero__blob hero__blob--2" style="top: 20%; right: -5%; opacity: 0.3;"></div>
    <div class="pricing__header">
      <p class="section-eyebrow">Pricing</p>
      <h2 class="section-title" style="--delay:.1s">Choose your <span class="text-gradient">companion</span></h2>
      <p class="pricing__desc" style="--delay:.2s">Price will be revealed soon.</p>
    </div>
    
    <div class="pricing__grid">
      <!-- Free Tier -->
      <div class="pricing-card glass-card" style="--delay:.1s">
        <div class="pricing-card__header">
          <h3 class="pricing-card__title">🌟 Lunara</h3>
          <p class="pricing-card__subtitle">Free Tier</p>
          <div class="pricing-card__price">Free</div>
        </div>
        <p style="font-size: 0.95rem; color: var(--clr-text-muted); margin-bottom: 1.5rem; text-align: center;">The free version of Lunara provides all the essential tools you need to start tracking and understanding your health journey.</p>
        <ul class="pricing-card__features">
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Cycle Tracking:</strong> Log and track your menstrual cycle with ease.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Symptom Logging:</strong> Keep track of your daily physical and emotional symptoms.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Basic AI Chat:</strong> Access to the Lunara AI assistant (limited to <strong>10 messages per day</strong>).</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>7-Day Analytics:</strong> View charts and insights based on your logged data over the past week.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Community Support:</strong> Engage with and get help from the Lunara community.</span></li>
        </ul>
      </div>

      <!-- Premium Tier -->
      <div class="pricing-card pricing-card--premium glass-card" style="--delay:.2s">
        <div class="pricing-card__header">
          <div class="pricing-card__badge">Most Popular</div>
          <h3 class="pricing-card__title">💎 Lunara+</h3>
          <p class="pricing-card__subtitle">Premium Tier</p>
          <div class="pricing-card__price" style="font-size: 1.4rem; padding-top: 0.35rem;">Price will be revealed soon</div>
        </div>
        <p style="font-size: 0.95rem; color: var(--clr-text-muted); margin-bottom: 1.5rem; text-align: center;"><strong>Lunara+</strong> unlocks the full power of the platform, offering deep, personalized insights and unrestricted access to advanced AI features.</p>
        <ul class="pricing-card__features">
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Unlimited AI Chat:</strong> Never hit a message cap again. Chat with your AI assistant as much as you need.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Advanced AI Models:</strong> Gain access to more powerful AI reasoning models for deeper, more accurate health insights.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>90-Day Analytics:</strong> Spot long-term patterns with a comprehensive 90-day view of your health data.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>And many more features...</strong></span></li>
        </ul>
      </div>
    </div>
  </section>
"""

roadmap_content = '''
  <section class="generic-page roadmap-section" style="padding-top: 80px; padding-bottom: 80px; min-height: 80vh; text-align: center;">
    <div class="pricing__header">
      <p class="section-eyebrow">Lunara Roadmap</p>
      <h2 class="section-title" style="--delay:.1s">The Future of <span class="text-gradient">Wellness</span></h2>
      <p class="pricing__desc" style="--delay:.2s" style="margin-bottom: 3rem;">A glimpse into our upcoming features and long-term vision.</p>
    </div>
    
    <div class="roadmap-image-container" style="--delay:.3s; width: 100%; max-width: 1000px; margin: 2rem auto 0; padding: 0;">
      <img src="roadmap_hero.png" alt="Lunara Future Roadmap" style="
        width: 100%; 
        height: auto; 
        display: block; 
        -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%), linear-gradient(to right, transparent 0%, black 15%, black 85%, transparent 100%);
        -webkit-mask-composite: source-in;
        mask-image: linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%), linear-gradient(to right, transparent 0%, black 15%, black 85%, transparent 100%);
        mask-composite: intersect;
      ">
    </div>
  </section>
'''

community_content = '''
  <section class="generic-page" style="padding-top: 150px; min-height: 80vh; text-align: center;">
    <div class="pricing__header">
      <p class="section-eyebrow">Community</p>
      <h2 class="section-title" style="--delay:.1s">Join the <span class="text-gradient">Movement</span></h2>
      <p class="pricing__desc" style="--delay:.2s" style="margin-bottom: 3rem;">Connect with us on our social platforms to stay updated, share your journey, and get early access announcements.</p>
    </div>
    
    <div style="display: flex; gap: 2rem; justify-content: center; flex-wrap: wrap; margin-top: 3rem;">
        <a href="https://x.com/Lunara_Harmone" target="_blank" class="btn btn--glow" style="display: flex; align-items: center; gap: 10px;"><svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg> Follow on X</a>
        <a href="https://www.instagram.com/lunarahealthtracker/" target="_blank" class="btn btn--outline" style="display: flex; align-items: center; gap: 10px; border-color: rgba(255,255,255,0.2);"><svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg> Follow on Instagram</a>
        <a href="https://github.com/himanksharma8434-coder/Lunara" target="_blank" class="btn btn--outline" style="display: flex; align-items: center; gap: 10px; border-color: rgba(255,255,255,0.2);"><svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg> View on GitHub</a>
    </div>
  </section>
'''

def get_placeholder(title, padding_top="150px"):
    return f'''
  <section class="generic-page" style="padding-top: {padding_top}; min-height: 60vh; text-align: center;">
    <div class="pricing__header">
      <p class="section-eyebrow">{title}</p>
      <h2 class="section-title" style="--delay:.1s">Coming <span class="text-gradient">Soon</span></h2>
      <p class="pricing__desc" style="--delay:.2s">We're working hard on this section. Stay tuned!</p>
    </div>
  </section>
'''

# Extract features section from index.html
feat_match = re.search(r'(<!-- ═══════════════════════════════════════════\s*FEATURES SHOWCASE[\s\S]*?</section>)', content)
feat_content = ""
if feat_match:
    feat_content = feat_match.group(1).replace('<section class="features" id="features">', '<section class="features" id="features" style="padding-top: 150px;">')


# Generate product.html
with open('product.html', 'w', encoding='utf-8') as p:
    p.write(head_part + chr(10) + chr(10) + mobile_nav_part + chr(10) + chr(10))
    if feat_content:
        p.write(feat_content + chr(10) + chr(10))
    else:
        p.write(get_placeholder('Features') + chr(10) + chr(10))
    p.write(pricing_content + chr(10) + chr(10))
    p.write(roadmap_content + chr(10) + chr(10))
    p.write(footer_part)

company_content = '''
  <!-- ═══════════════════════════════════════════
       PAGE HERO
  ═══════════════════════════════════════════ -->
  <section class="page-hero">
    <div class="hero__blob hero__blob--1" style="top: -5%; left: -8%;"></div>
    <div class="hero__blob hero__blob--2" style="bottom: 5%; right: -5%;"></div>
    <div class="hero__blob hero__blob--3" style="top: 35%; left: 30%;"></div>

    <div class="page-hero__watermark" aria-hidden="true">LUNARA</div>

    <div class="hero__particles" aria-hidden="true">
      <span class="particle" style="--x:15%;--y:30%;--s:5px;--d:10s;--del:0s"></span>
      <span class="particle" style="--x:75%;--y:15%;--s:4px;--d:13s;--del:2s"></span>
      <span class="particle" style="--x:50%;--y:65%;--s:6px;--d:11s;--del:1.5s"></span>
      <span class="particle" style="--x:85%;--y:45%;--s:3px;--d:15s;--del:4s"></span>
    </div>

    <div class="page-hero__content">
      <p class="page-hero__eyebrow">About Lunara</p>
      <h1 class="page-hero__title">
        Your Personal
        <span class="accent text-gradient">Cycle &amp; Wellness</span>
        Companion
      </h1>
      <p class="page-hero__sub">
        Understanding your body should be intuitive, empowering, and completely private. That's the promise we built Lunara on.
      </p>
    </div>
  </section>


  <!-- ═══════════════════════════════════════════
       ABOUT — MISSION + WHAT SETS US APART
  ═══════════════════════════════════════════ -->
  <section class="features" style="padding-bottom: 4rem;">
    <div class="hero__blob hero__blob--1" style="top: 10%; right: -8%; opacity: 0.4;"></div>
    <div class="features__header">
      <p class="section-eyebrow sr-fade-up">Our Story</p>
      <h2 class="section-title sr-fade-up sr-delay-1">Built with care,<br/><span class="text-gradient">driven by purpose</span></h2>
      <p class="pricing__desc sr-fade-up sr-delay-2" style="margin-top: 1rem;">
        At Lunara, we believe that understanding your body should be intuitive, empowering, and completely private. We are a modern, privacy-focused menstrual cycle tracking and wellness app designed to give you deep insights into your health without compromising your security.
      </p>
    </div>

    <!-- Mission & Values as icon cards -->
    <div class="about-icon-grid">
      <div class="about-icon-card sr-fade-up sr-delay-1">
        <div class="about-icon-card__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
        </div>
        <div class="about-icon-card__text">
          <h4>AI-Powered Insights</h4>
          <p>Integrated with Google Gemini AI, our smart health chat provides thoughtful, context-aware answers to your cycle-related questions.</p>
        </div>
      </div>

      <div class="about-icon-card sr-fade-up sr-delay-2">
        <div class="about-icon-card__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
        </div>
        <div class="about-icon-card__text">
          <h4>Holistic Wellness</h4>
          <p>We don't just track periods. Beautiful, interactive charts for your mood, sleep, steps, and symptoms — syncing with HealthKit and Health Connect.</p>
        </div>
      </div>

      <div class="about-icon-card sr-fade-up sr-delay-3">
        <div class="about-icon-card__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
        </div>
        <div class="about-icon-card__text">
          <h4>Built for Connection</h4>
          <p>With our unique Partner Sync feature, share your cycle data with a partner in real-time to foster better understanding and support.</p>
        </div>
      </div>

      <div class="about-icon-card sr-fade-up sr-delay-4">
        <div class="about-icon-card__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
        </div>
        <div class="about-icon-card__text">
          <h4>Privacy First, Always</h4>
          <p>Your health data is your business. Lunara is built with robust encryption and a strict no-data-selling policy.</p>
        </div>
      </div>
    </div>

    <!-- Mission Statement Card -->
    <div style="max-width: 800px; margin: 3rem auto 0; padding: 0 1.5rem;">
      <div class="glass-card sr-scale-in sr-delay-2" style="padding: 2.5rem; text-align: center; border: 2px solid var(--clr-pink-light); background: linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(255,240,245,0.6) 100%);">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: var(--clr-text); margin-bottom: 1rem;">Our Mission</h3>
        <p style="font-size: 1rem; color: var(--clr-text-muted); line-height: 1.7;">
          Our mission is to empower individuals by providing intelligent cycle predictions, comprehensive symptom tracking, and personalized health insights. We aim to take the guesswork out of wellness, helping you sync with your body's natural rhythm.
        </p>
      </div>
    </div>
  </section>

  <!-- Section Divider -->
  <div class="section-divider sr-fade-up" style="margin: 2rem auto;"></div>

  <!-- ═══════════════════════════════════════════
       BLOG
  ═══════════════════════════════════════════ -->
  <section class="pricing" style="background: var(--clr-bg-warm);">
    <div class="hero__blob hero__blob--2" style="top: 15%; left: -5%; opacity: 0.3;"></div>
    <div class="pricing__header" style="max-width: 800px; margin: 0 auto 3rem;">
      <p class="section-eyebrow sr-fade-up">Blog</p>
      <h2 class="section-title sr-fade-up sr-delay-1">Meet Lunara: Your Cycle, <span class="text-gradient">Decoded</span></h2>
      <p class="pricing__desc sr-fade-up sr-delay-2" style="text-align: left; margin-top: 1.5rem; font-size: 1.05rem; line-height: 1.7;">
        Your menstrual cycle is more than just a date on the calendar — it affects your sleep, mood, and daily energy. That's why we built Lunara, a privacy-first cycle and wellness companion designed to help you sync with your body's natural rhythm.
      </p>
    </div>

    <div style="max-width: 800px; margin: 0 auto; padding: 0 1.5rem;">
      <div class="pricing-card glass-card sr-fade-up sr-delay-3" style="text-align: left; width: 100%;">
        <div class="pricing-card__header">
          <h3 class="pricing-card__title">Here's what you can do with Lunara:</h3>
        </div>
        <ul class="pricing-card__features" style="margin-top: 1rem;">
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Chat with AI:</strong> Got a symptom question? Our Google Gemini AI assistant provides smart, context-aware answers instantly.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Track the Big Picture:</strong> Log your periods, moods, sleep, and steps. See how they all connect through beautiful, interactive charts.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Partner Sync:</strong> Securely share your cycle phase with your partner in real-time, bridging the communication gap.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Keep It Private:</strong> Your health data is yours. We use strict encryption and promise to never sell your data.</span></li>
        </ul>
        <p style="margin-top: 2rem; font-size: 1.05rem; font-weight: 500; color: var(--clr-text);">
          Stop fighting your cycle and start working with it. Lunara is launching soon on Google Play!
        </p>
        <div style="margin-top: 2rem; text-align: center;">
          <a href="#download" class="btn btn--glow">Get Early Access Here</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section Divider -->
  <div class="section-divider sr-fade-up" style="margin: 2rem auto;"></div>

  <!-- ═══════════════════════════════════════════
       CONTACT
  ═══════════════════════════════════════════ -->
  <section class="generic-page" style="padding: 80px 0; text-align: center;">
    <div class="hero__blob hero__blob--3" style="top: 20%; right: -5%; opacity: 0.3;"></div>
    <div class="pricing__header">
      <p class="section-eyebrow sr-fade-up">Contact</p>
      <h2 class="section-title sr-fade-up sr-delay-1">Get in <span class="text-gradient">Touch</span></h2>
      <p class="pricing__desc sr-fade-up sr-delay-2">We'd love to hear from you. Reach out to us via email.</p>
      
      <div class="contact-cards sr-fade-up sr-delay-3">
        <a href="mailto:lunarahealthtracker@gmail.com" class="btn btn--glow" style="display: inline-flex; align-items: center; gap: 0.5rem; justify-content: center; min-width: 320px;">
          <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          lunarahealthtracker@gmail.com
        </a>
        <div style="margin-top: 0.5rem; text-align: center;">
          <p style="font-size: 0.85rem; color: var(--clr-text-muted); margin-bottom: 0.5rem;">Developer Contact</p>
          <a href="mailto:himanksharma8434@gmail.com" class="btn btn--outline" style="display: inline-flex; align-items: center; gap: 0.5rem; justify-content: center; min-width: 320px; background: var(--glass-bg); border: 1px solid var(--glass-border); padding: 0.5rem 1rem; font-size: 0.9rem;">
            <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
            himanksharma8434@gmail.com
          </a>
        </div>
      </div>

      <!-- Contact Form -->
      <div class="contact-form-wrapper sr-fade-up sr-delay-4">
        <p style="font-size: 0.95rem; color: var(--clr-text-muted); margin-bottom: 1.5rem;">Or send us a message directly:</p>
        <form class="contact-form glass-card" id="contactForm">
          <div class="contact-form__row">
            <div class="contact-form__group">
              <label for="contact-name" class="contact-form__label">Name</label>
              <input type="text" id="contact-name" name="name" class="contact-form__input" placeholder="Your name" required />
            </div>
            <div class="contact-form__group">
              <label for="contact-email" class="contact-form__label">Email</label>
              <input type="email" id="contact-email" name="email" class="contact-form__input" placeholder="you@example.com" required />
            </div>
          </div>
          <div class="contact-form__group">
            <label for="contact-subject" class="contact-form__label">Subject</label>
            <select id="contact-subject" name="subject" class="contact-form__input contact-form__select" required>
              <option value="" disabled selected>Choose a topic...</option>
              <option value="General Inquiry">General Inquiry</option>
              <option value="Feature Request">Feature Request</option>
              <option value="Beta Testing">Beta Testing</option>
              <option value="Bug Report">Bug Report</option>
              <option value="Partnership">Partnership</option>
              <option value="Other">Other</option>
            </select>
          </div>
          <div class="contact-form__group">
            <label for="contact-message" class="contact-form__label">Message</label>
            <textarea id="contact-message" name="message" class="contact-form__input contact-form__textarea" placeholder="Tell us what's on your mind..." rows="5" required></textarea>
          </div>
          <button type="submit" class="btn btn--glow contact-form__submit">
            <svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
            Send Message
          </button>
        </form>
      </div>

    </div>
  </section>
'''

# Generate company.html
with open('company.html', 'w', encoding='utf-8') as p:
    p.write(head_part + chr(10) + chr(10) + mobile_nav_part + chr(10) + chr(10))
    p.write(company_content + chr(10) + chr(10))
    p.write(footer_part)

# Generate community.html
with open('community.html', 'w', encoding='utf-8') as p:
    p.write(head_part + chr(10) + chr(10) + mobile_nav_part + chr(10) + chr(10))
    p.write(community_content + chr(10) + chr(10))
    p.write(footer_part)

print("Pages created successfully: product.html, company.html, community.html")
