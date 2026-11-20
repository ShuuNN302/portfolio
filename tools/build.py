#!/usr/bin/env python3
"""Generates the static portfolio site into site/. Content lives here; edit and re-run."""
import os, sys

OUT = sys.argv[1]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Montserrat:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">')

EMAIL = "ducvo300898@gmail.com"
PHONE = "+84 369 123 272"
BEHANCE = "https://www.behance.net/cv69"
LINKEDIN = "https://www.linkedin.com/in/vo-dang-hong-duc/"
RESUME = "https://bit.ly/ducvo-resume"

ICON = {
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
 'be': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8.2 11.3c.9-.4 1.4-1.1 1.4-2.1C9.6 7.3 8.2 6.5 6.4 6.5H1.5v11h5c1.9 0 3.6-.9 3.6-3 0-1.3-.6-2.8-1.9-3.2zM3.7 8.3h2.1c.8 0 1.5.2 1.5 1.1 0 .8-.6 1.1-1.3 1.1H3.7V8.3zm2.4 7.4H3.7v-3.1h2.4c1 0 1.6.4 1.6 1.5 0 1.1-.8 1.6-1.6 1.6zM16.9 9c-2.5 0-4.2 1.9-4.2 4.3 0 2.5 1.6 4.3 4.2 4.3 1.9 0 3.2-.9 3.8-2.8h-1.9c-.2.7-1.1 1.1-1.8 1.1-1.4 0-2.1-.8-2.1-2.2h6c.1-2.6-1.4-4.7-4-4.7zm-2 3.4c.1-1.1.8-1.8 1.9-1.8 1.2 0 1.8.7 1.9 1.8h-3.8zM14.5 6.8h4.8v1.2h-4.8z"/></svg>',
 'in': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.2c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4z"/></svg>',
 'globe': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
}

def head(title, desc, prefix, body_class=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#d3222a">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23d3222a'/%3E%3Ctext x='32' y='44' font-family='Georgia,serif' font-size='36' fill='white' text-anchor='middle'%3ES%3C/text%3E%3C/svg%3E">
{FONTS}
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body class="{body_class}">
<header class="topbar"><div class="wrap">
  <a class="brand" href="{prefix}index.html">Shuu<b>.</b></a>
  <nav class="nav" aria-label="Main">
    <a href="{prefix}index.html#work" class="keep">Work</a>
    <a href="{prefix}index.html#about">About</a>
    <a href="{RESUME}" target="_blank" rel="noopener">Resume</a>
    <a href="{prefix}index.html#contact" class="cta">Contact</a>
  </nav>
</div></header>
'''

def footer():
    return f'''<footer class="footer" id="contact"><div class="wrap">
  <div class="footer-grid">
    <div>
      <h2>Let’s build something <em>clear</em> together.</h2>
      <p>Open to Senior UX/UI and Product Design roles. I usually reply within a day.</p>
      <p style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap">
        <a class="btn" href="mailto:{EMAIL}">Email me</a>
        <a class="btn ghost" href="{RESUME}" target="_blank" rel="noopener">View resume</a>
      </p>
    </div>
    <ul>
      <li><a href="mailto:{EMAIL}">{ICON['mail']}{EMAIL}</a></li>
      <li><a href="tel:+84369123272">{ICON['phone']}{PHONE}</a></li>
      <li><a href="{LINKEDIN}" target="_blank" rel="noopener">{ICON['in']}LinkedIn</a></li>
      <li><a href="{BEHANCE}" target="_blank" rel="noopener">{ICON['be']}Behance</a></li>
    </ul>
  </div>
  <div class="copyright"><span>© 2026 Vo Dang Hong Duc (Shuu)</span><span>Ho Chi Minh City, Viet Nam</span></div>
</div></footer>
<script>
(function(){{var els=document.querySelectorAll('.reveal');if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}});return}}
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{rootMargin:'0px 0px -8% 0px'}});els.forEach(function(e){{io.observe(e)}})}})();
</script>
</body>
</html>
'''

def img(name, alt, prefix, w, h, cls="figure", lazy=True, caption=None):
    """Responsive WebP: 800w for phones, full for larger screens."""
    l = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return (f'<figure class="{cls} reveal"><img src="{prefix}img/{name}.webp" '
            f'srcset="{prefix}img/{name}-sm.webp 800w, {prefix}img/{name}.webp {w}w" '
            f'sizes="(max-width: 1120px) 100vw, 1120px" width="{w}" height="{h}" alt="{alt}"{l}>{cap}</figure>')

PROJECTS = [
 dict(slug="tti-annual-review", title="TTI Annual Review 2022", group=1, kicker="Corporate website · 2022–2023",
      blurb="A slide-scrolling website that turns a dense annual report into an interactive story.", thumb="tti-circle"),
 dict(slug="signage-platform", title="Signage Manage Platform", group=1, kicker="Internal web platform · 2024–Now",
      blurb="Replaced an email-based ordering process for factories, cutting request cycles from ~1 month to under 1 week.", thumb="sig-hero"),
 dict(slug="conta-agency", title="CONTA Agency Website", group=2, kicker="Agency website · Healthcare",
      blurb="A bold, high-tech website for a creative agency serving the healthcare sector.", thumb="conta-hero"),
 dict(slug="design-system", title="Personal Design System", group=2, kicker="Design system · Figma",
      blurb="Color, typography, iconography and component library built for scale and consistency.", thumb="ds-hero"),
]
SIZES = {}

def next_link(slug, prefix):
    i = [p['slug'] for p in PROJECTS].index(slug)
    n = PROJECTS[(i + 1) % len(PROJECTS)]
    return f'''<div class="wrap next"><a href="{n['slug']}.html"><span><small>Next project</small><strong>{n['title']}</strong></span><span class="arrow">→</span></a></div>'''

def meta(items):
    return '<dl class="meta reveal">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items) + '</dl>'

def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(html)

# ---------------- Home ----------------
def card(p):
    w, h = SIZES[p['thumb']]
    return f'''<a class="card reveal" href="work/{p['slug']}.html">
  <div class="thumb"><img src="img/{p['thumb']}-sm.webp" width="800" height="{round(h*800/w)}" alt="{p['title']} preview" loading="lazy" decoding="async"></div>
  <div class="body"><span class="kicker">{p['kicker']}</span><h4>{p['title']}</h4><p>{p['blurb']}</p><span class="more">View case study <span>→</span></span></div>
</a>'''

def home():
    g1 = ''.join(card(p) for p in PROJECTS if p['group'] == 1)
    g2 = ''.join(card(p) for p in PROJECTS if p['group'] == 2)
    tools = [("F", "Figma"), ("Xd", "Adobe XD"), ("Ps", "Photoshop"), ("Ai", "Illustrator"),
             ("Pr", "Premiere Pro"), ("Ae", "After Effects"), ("<small>FR</small>", "Framer"), ("<small>WF</small>", "Webflow")]
    tools_html = ''.join(f'<span class="tool" title="{n}" aria-label="{n}">{a}</span>' for a, n in tools)
    return head("Shuu — Senior UX/UI Designer Portfolio",
                "Portfolio of Vo Dang Hong Duc (Shuu), Senior UX/UI Designer in Ho Chi Minh City. Case studies in product, web and design systems.", "") + f'''
<main>
<section class="hero">
  <span class="rail l"></span><span class="rail r"></span>
  <div class="wrap">
    <div class="hero-meta"><span>Portfolio</span><span>2026</span><span>VĐHĐ</span></div>
    <div class="hero-title">
      <span class="shuu">SHUU</span>
      <h1>Portfolio</h1>
      <span class="pill" aria-hidden="true"><span class="diamond"></span>UX / UI DESIGNER<span class="diamond"></span></span>
      <span class="sr-only">Senior UX/UI Designer</span>
    </div>
    <div class="links">
      <a href="{BEHANCE}" target="_blank" rel="noopener">{ICON['be']}behance.net/cv69</a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener">{ICON['in']}linkedin.com/in/vo-dang-hong-duc</a>
      <a href="{RESUME}" target="_blank" rel="noopener">{ICON['globe']}bit.ly/ducvo-resume</a>
    </div>
  </div>
</section>

<section class="about" id="about"><div class="wrap">
  <div class="about-grid">
    <div class="photo reveal"><img src="img/me.webp" width="660" height="960" alt="Portrait of Vo Dang Hong Duc holding a camera" fetchpriority="high"></div>
    <div class="reveal">
      <p class="role-label">Senior UX/UI Designer</p>
      <h2 class="name">Vo Dang<br>Hong Duc</h2>
      <h3 class="label">About me</h3>
      <p>I’m a Senior UX/UI Designer with 5 years of experience simplifying complex workflows into intuitive products, contributing from structure to execution.</p>
      <p>Short term, I aim to take greater ownership in end-to-end product design. Long term, I’m working toward becoming a design lead, shaping product direction and scalable experiences.</p>
    </div>
  </div>
  <div class="facts">
    <div class="reveal"><h3 class="label">Contact</h3><ul>
      <li>{ICON['phone']}<a href="tel:+84369123272">{PHONE}</a></li>
      <li>{ICON['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{ICON['pin']}Ho Chi Minh City, Viet Nam</li></ul></div>
    <div class="reveal"><h3 class="label">Skills</h3><ul class="dot">
      <li>User-Centered Design</li><li>Wireframing &amp; Prototyping</li><li>Design Systems</li><li>Social Media Design</li></ul></div>
    <div class="reveal"><h3 class="label">Tools</h3><div class="tools">{tools_html}</div></div>
  </div>
</div></section>

<section class="work" id="work"><div class="wrap">
  <div class="section-head"><h2>Selected Work</h2></div>
  <div class="group">
    <div class="group-title reveal"><span class="num">01.</span><h3>Work-Related Projects</h3></div>
    <div class="cards">{g1}</div>
  </div>
  <div class="group">
    <div class="group-title reveal"><span class="num">02.</span><h3>Personal Projects</h3></div>
    <div class="cards">{g2}</div>
  </div>
</div></section>
</main>
''' + footer()

# ---------------- Case studies ----------------
P = "../"

def tti():
    s = SIZES
    return head("TTI Annual Review 2022 — Shuu Portfolio", "Case study: a slide-scrolling annual review website for Techtronic Industries.", P) + f'''
<main>
<div class="cs-hero"><img src="../img/tti-hero.webp" srcset="../img/tti-hero-sm.webp 800w, ../img/tti-hero.webp 1600w" sizes="100vw" width="{s['tti-hero'][0]}" height="{s['tti-hero'][1]}" alt="TTI Annual Review 2022 website on a laptop" fetchpriority="high"></div>
<div class="wrap cs-head">
  <a class="back" href="../index.html#work">← All work</a>
  <h1>TTI Annual Review 2022</h1>
  <p class="lede">Designed as a slide-scrolling website, the 2022 Annual Review showcases the company’s key accomplishments over the year.</p>
  <a class="live" href="https://2022review.ttigroup.com" target="_blank" rel="noopener">2022review.ttigroup.com ↗</a>
  {meta([("Output Type","Website · UI Design"),("Timeline","Oct 2022 – Mar 2023"),("My Role","UX/UI Designer"),("Tool Used","Figma")])}
</div>
<div class="wrap">{img('tti-circle','Annual review navigation wheel shown on a laptop',P,*s['tti-circle'])}</div>

<section class="cs-section"><div class="wrap">
  <h2>Layout &amp; Interaction</h2>
  <p>A slide-scrolling interaction was applied to create a sense of progression across sections.</p>
  <p>Modular layouts allowed flexibility when presenting different types of content, from statistics to brand showcases. Transitions were kept subtle to support the content rather than distract from it.</p>
  {img('tti-layout','Overview of modular slide layouts',P,*s['tti-layout'],cls="figure flat")}
</div></section>

<section class="cs-section"><div class="wrap split rev">
  <div>{img('tti-content','Powerful Brands section on a laptop',P,*s['tti-content'],cls="figure flat")}</div>
  <div class="reveal"><h2>Content &amp; Data</h2>
  <p>Content hierarchy was structured so key messages stand out within a dense amount of information. Visual direction stayed close to the brand identity while improving readability and the digital experience.</p>
  <p>Multiple layout explorations were tested to find the right balance between corporate tone and modern interaction.</p></div>
</div></section>

<section class="cs-section"><div class="wrap split">
  <div class="reveal"><h2>Refinement &amp; Impact</h2>
  <p>Attention to detail was applied across components to ensure consistency and usability. Each screen was refined to stay clear across resolutions, and micro-adjustments in spacing and typography improved overall readability.</p>
  <p>The final design communicates corporate performance in a more engaging way, turning static reporting into an interactive storytelling journey.</p></div>
  <div>{img('tti-refine','Brand pages for Milwaukee shown in perspective',P,*s['tti-refine'],cls="figure flat")}</div>
</div></section>

<div class="wrap" style="margin-top:clamp(40px,6vw,72px)">{img('tti-sustain','Sustainability section with circular navigation over a forest',P,*s['tti-sustain'])}</div>
{next_link('tti-annual-review', P)}
</main>
''' + footer()

def signage():
    s = SIZES
    return head("Signage Manage Platform — Shuu Portfolio", "Case study: an internal web platform that simplifies signage ordering for factories.", P) + f'''
<main>
<div class="cs-hero"><img src="../img/sig-hero.webp" srcset="../img/sig-hero-sm.webp 800w, ../img/sig-hero.webp 1600w" sizes="100vw" width="{s['sig-hero'][0]}" height="{s['sig-hero'][1]}" alt="Signage Manage Platform cover" fetchpriority="high"></div>
<div class="wrap cs-head">
  <a class="back" href="../index.html#work">← All work</a>
  <h1>Signage Manage Platform</h1>
  <p class="lede">A web platform that simplifies the signage ordering process for factories.</p>
  {meta([("Output Type","Internal Platform"),("Timeline","Jun 2024 – Now"),("My Role","UX/UI Designer"),("Tool Used","Figma")])}
  <div class="impact reveal">
    <div><strong>~1 month → &lt;1 week</strong>Request cycle time</div>
    <div><strong>Fewer errors</strong>Less miscommunication between factories and branding</div>
    <div><strong>On-time delivery</strong>Higher rate of signage delivered on schedule</div>
  </div>
</div>

<section class="cs-section"><span class="ghost" aria-hidden="true">01</span><div class="wrap split">
  <div><h2>Project Overview</h2>
  <p>The Internal Signage Ordering Platform replaces the manual email process factory managers used to request signage. It streamlines request submission, design collaboration and task tracking.</p>
  <p>It supports both template-based and custom signage, giving factories more control while helping the branding team stay organized. The result is a better cross-department workflow and consistent branding across all locations.</p></div>
  <div>{img('sig-signs','Example exit and no-smoking signs',P,*s['sig-signs'],cls="figure flat")}</div>
</div></section>

<section class="cs-section"><span class="ghost" aria-hidden="true">02</span><div class="wrap">
  <h2>Problem Statement</h2>
  <p>Factory managers submitted signage requests via email, which led to long communication loops and poor tracking. The branding team, responsible for visual consistency, struggled to manage requests, monitor design delivery and coordinate with multiple printing vendors.</p>
  {img('sig-process','Current 8-step email-based signage process',P,*s['sig-process'],cls="figure flat")}
  {img('sig-pain','Five pain points: lack of visibility, delayed timelines, inefficient vendor management, inconsistent branding, difficulty prioritizing',P,*s['sig-pain'],cls="figure flat")}
</div></section>

<section class="cs-section"><span class="ghost" aria-hidden="true">03</span><div class="wrap">
  <h2>Proposed Solution</h2>
  <p>Direct user research wasn’t feasible due to internal limitations, so I worked with indirect feedback from stakeholders and recurring issues reported to management. I prioritized key pain points, mapped success metrics, and proposed features for both factory managers and the branding team.</p>
  {img('sig-goals','Goals and success metrics',P,*s['sig-goals'],cls="figure flat")}
  <h3>Key features</h3>
  <ul class="features">
    <li><b>Signage Templates:</b> pre-approved designs ready for quick ordering</li>
    <li><b>Custom Design Tool:</b> managers can propose layouts online</li>
    <li><b>Auto Task Creation:</b> tasks sync to the PM tool for tracking</li>
    <li><b>Admin Dashboard:</b> branding team can filter, review and assign requests</li>
    <li><b>Cart:</b> multiple signage requests, reviewed and edited before placing</li>
    <li><b>Order Management:</b> track progress and details of each request in real time</li>
    <li><b>Vendor Pool Management:</b> choose from a curated list of trusted vendors</li>
  </ul>
</div></section>

<section class="cs-section"><span class="ghost" aria-hidden="true">04</span><div class="wrap">
  <h2>Design Process</h2>
  <p>I mapped core user flows from stakeholder input, then built low-fidelity wireframes for quick internal validation. Once flows were aligned, I moved to high-fidelity UI using our internal design system, iterating in weekly reviews with the branding team and product stakeholders.</p>
  {img('sig-wire','Low-fidelity wireframes',P,*s['sig-wire'],cls="figure flat")}
  {img('sig-style','Style guide: Trade Gothic Next and Barlow typefaces, brand and neutral colors',P,*s['sig-style'],cls="figure flat")}
  {img('sig-hifi','High-fidelity mockups: homepage, create signage flow, cart and order placement',P,*s['sig-hifi'],cls="figure flat")}
</div></section>
{next_link('signage-platform', P)}
</main>
''' + footer()

def conta():
    s = SIZES
    return head("CONTA Agency Website — Shuu Portfolio", "Case study: a bold, high-tech website for CONTA, a creative agency serving the healthcare sector.", P, "theme-dark") + f'''
<main>
<div class="wrap cs-head">
  <a class="back" href="../index.html#work">← All work</a>
  <h1>CONTA <span>Agency</span></h1>
  <p class="lede">A high-tech, visually impactful website for CONTA, a creative agency serving the healthcare sector.</p>
  <a class="live" href="https://contamedia.vn/" target="_blank" rel="noopener">contamedia.vn ↗</a>
  {meta([("Output Type","Website · UI Design"),("Client","CONTA Media"),("My Role","UX/UI Designer"),("Tool Used","Figma")])}
</div>
<div class="wrap">{img('conta-hero','CONTA website pages overview',P,*s['conta-hero'],cls="figure dark")}</div>
<section class="cs-section"><div class="wrap">
  <h2>Bold yet clear</h2>
  <p>As the designer, I focused on a bold yet clear layout that reflects the agency’s innovative and professional identity: dark surfaces, strong type and a single green accent to guide attention.</p>
  {img('conta-a','Homepage and About page designs',P,*s['conta-a'],cls="figure dark")}
  {img('conta-b','Projects page and footer designs',P,*s['conta-b'],cls="figure dark")}
</div></section>
{next_link('conta-agency', P)}
</main>
''' + footer()

def ds():
    s = SIZES
    return head("Personal Design System — Shuu Portfolio", "Case study: a personal design system covering color, typography, iconography, buttons and input fields.", P, "theme-teal") + f'''
<main>
<div class="cs-hero"><img src="../img/ds-hero.webp" srcset="../img/ds-hero-sm.webp 800w, ../img/ds-hero.webp 1600w" sizes="100vw" width="{s['ds-hero'][0]}" height="{s['ds-hero'][1]}" alt="Personal Design System cover" fetchpriority="high"></div>
<div class="wrap cs-head">
  <a class="back" href="../index.html#work">← All work</a>
  <h1>Personal Design System</h1>
  <p class="lede">A design system, pattern library and style guide built in Figma for consistent, scalable interfaces.</p>
  {meta([("Output Type","Design System"),("Scope","Foundations + Components"),("My Role","Designer"),("Tool Used","Figma")])}
</div>
<section class="cs-section"><span class="ghost" aria-hidden="true">01</span><div class="wrap">
  <h2>Color</h2>
  <p>Color schemes are treated as a cohesive group of relative tones rather than fixed values, so the palette adapts as inputs change while keeping its tonal relationships.</p>
  {img('ds-color','Primary teal, secondary deep purple, accent amber, neutrals and semantic colors',P,*s['ds-color'],cls="figure flat")}
</div></section>
<section class="cs-section"><span class="ghost" aria-hidden="true">02</span><div class="wrap">
  <h2>Typography</h2>
  <p>A scale of 15 styles, each with a clear role, grouped into categories from display to small text. Montserrat and Averta in light, regular, semibold and bold.</p>
  {img('ds-type','Montserrat and Averta typefaces',P,*s['ds-type'],cls="figure flat")}
</div></section>
<section class="cs-section"><span class="ghost" aria-hidden="true">03</span><div class="wrap">
  <h2>Iconography</h2>
  <p>Icons are simple, friendly and built on a 24px grid with 2px padding, so they stay legible at small sizes.</p>
  {img('ds-icon','Icon grid and icon set',P,*s['ds-icon'],cls="figure flat")}
</div></section>
<section class="cs-section"><span class="ghost" aria-hidden="true">04</span><div class="wrap">
  <h2>Buttons</h2>
  <p>Contained and icon buttons in primary, secondary and link styles, each with default, hover, pressed and disabled states.</p>
  {img('ds-button','Button anatomy and states',P,*s['ds-button'],cls="figure flat")}
</div></section>
<section class="cs-section"><span class="ghost" aria-hidden="true">05</span><div class="wrap">
  <h2>Input Fields</h2>
  <p>Text fields with default, active, filled, disabled, success and error states, with consistent spacing and helper messages.</p>
  {img('ds-input','Input field anatomy and states',P,*s['ds-input'],cls="figure flat")}
</div></section>
{next_link('design-system', P)}
</main>
''' + footer()

if __name__ == "__main__":
    from PIL import Image
    for f in os.listdir(os.path.join(OUT, 'img')):
        if f.endswith('.webp') and not f.endswith('-sm.webp'):
            SIZES[f[:-5]] = Image.open(os.path.join(OUT, 'img', f)).size
    write('index.html', home())
    write('work/tti-annual-review.html', tti())
    write('work/signage-platform.html', signage())
    write('work/conta-agency.html', conta())
    write('work/design-system.html', ds())
    print("built")
