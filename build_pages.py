import re

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

pages = [
    'pricing.html',
    'features.html',
    'roadmap.html',
    'about.html',
    'blog.html',
    'contact.html',
    'privacy.html',
    'terms.html',
    'cookies.html'
]

# We also need the pricing section content for pricing.html
pricing_content = """
  <!-- ═══════════════════════════════════════════
       PRICING / SUBSCRIPTION
  ═══════════════════════════════════════════ -->
  <section class="pricing" id="pricing" style="padding-top: 150px; min-height: 80vh;">
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
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>AI Wellness Plans:</strong> Receive fully personalized wellness routines tailored specifically to your unique cycle and logged symptoms.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>AI Predictive Trends:</strong> Get intelligent foresight into upcoming hormonal shifts, energy peaks, and mood dips.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Personalized Diet Plans:</strong> Receive dietary recommendations mapped precisely to your current cycle phase.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>PDF Health Reports:</strong> Export your health history and insights into clean, professional PDF reports—perfect for sharing with your doctor.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>SMS Notifications:</strong> Receive your most important reminders and insights directly via text message.</span></li>
          <li><svg viewBox="0 0 24 24" fill="var(--clr-pink)" width="20" height="20"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span><strong>Priority Support:</strong> Jump to the front of the queue whenever you need technical assistance.</span></li>
        </ul>
      </div>
    </div>
  </section>
"""

def get_placeholder(title):
    if title.lower() == 'roadmap':
        return '''
  <section class="generic-page roadmap-section" style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; text-align: center;">
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
    return f'''
  <section class="generic-page" style="padding-top: 150px; min-height: 60vh; text-align: center;">
    <div class="pricing__header">
      <p class="section-eyebrow">{title}</p>
      <h2 class="section-title" style="--delay:.1s">Coming <span class="text-gradient">Soon</span></h2>
      <p class="pricing__desc" style="--delay:.2s">We're working hard on this page. Stay tuned!</p>
    </div>
  </section>
'''

for page in pages:
    with open(page, 'w', encoding='utf-8') as p:
        p.write(head_part)
        p.write('\\n\\n')
        p.write(mobile_nav_part)
        p.write('\\n\\n')
        
        if page == 'pricing.html':
            p.write(pricing_content)
        elif page == 'features.html':
            # We don't remove it from index.html based on user's feedback, 
            # we just copy it to features.html as well
            feat_match = re.search(r'(<!-- ═══════════════════════════════════════════\s*FEATURES SHOWCASE[\s\S]*?</section>)', content)
            if feat_match:
                feat_str = feat_match.group(1).replace('<section class="features" id="features">', '<section class="features" id="features" style="padding-top: 150px; min-height: 80vh;">')
                p.write(feat_str)
            else:
                p.write(get_placeholder('Features'))
        else:
            p.write(get_placeholder(page.replace('.html', '').capitalize()))
            
        p.write('\\n\\n')
        p.write(footer_part)

print("Pages created successfully.")
