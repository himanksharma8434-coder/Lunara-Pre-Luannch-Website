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
        <a href="https://discord.com" target="_blank" class="btn btn--glow" style="display: flex; align-items: center; gap: 10px;"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M20.317 4.37a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 00-5.487 0 12.64 12.64 0 00-.617-1.25.077.077 0 00-.079-.037A19.736 19.736 0 003.677 4.37a.07.07 0 00-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 00.031.057 19.9 19.9 0 005.993 3.03.078.078 0 00.084-.028 14.09 14.09 0 001.226-1.994.076.076 0 00-.041-.106 13.107 13.107 0 01-1.872-.892.077.077 0 01-.008-.128 10.2 10.2 0 00.372-.292.074.074 0 01.077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 01.078.01c.12.098.246.198.373.292a.077.077 0 01-.006.127 12.299 12.299 0 01-1.873.892.077.077 0 00-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 00.084.028 19.839 19.839 0 006.002-3.03.077.077 0 00.032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 00-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg> Join Discord</a>
        <a href="https://x.com/lunara_app" target="_blank" class="btn btn--outline" style="display: flex; align-items: center; gap: 10px; border-color: rgba(255,255,255,0.2);"><svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg> Follow on X</a>
        <a href="https://instagram.com/lunara_app" target="_blank" class="btn btn--outline" style="display: flex; align-items: center; gap: 10px; border-color: rgba(255,255,255,0.2);"><svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg> Follow on Instagram</a>
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

# Generate company.html
with open('company.html', 'w', encoding='utf-8') as p:
    p.write(head_part + chr(10) + chr(10) + mobile_nav_part + chr(10) + chr(10))
    p.write(get_placeholder('About Us') + chr(10) + chr(10))
    p.write(get_placeholder('Blog', padding_top="80px") + chr(10) + chr(10))
    p.write(get_placeholder('Contact', padding_top="80px") + chr(10) + chr(10))
    p.write(footer_part)

# Generate community.html
with open('community.html', 'w', encoding='utf-8') as p:
    p.write(head_part + chr(10) + chr(10) + mobile_nav_part + chr(10) + chr(10))
    p.write(community_content + chr(10) + chr(10))
    p.write(footer_part)

print("Pages created successfully: product.html, company.html, community.html")
