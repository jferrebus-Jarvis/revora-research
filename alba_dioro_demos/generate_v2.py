import urllib.parse
WHATSAPP_NUM = "18328441734"

def wa_link(msg):
    return f"https://wa.me/{WHATSAPP_NUM}?text={urllib.parse.quote(msg)}"

PRODUCTS = [
    {"name": "Anillos", "emoji": "💍", "desc": "Oro italiano 18k y 24k, diseños clásicos y contemporáneos", "price": "Desde $85"},
    {"name": "Cadenas y Collares", "emoji": "📿", "desc": "Piezas macizas en oro 18k y 24k, cierres reforzados", "price": "Desde $120"},
    {"name": "Pulseras", "emoji": "✨", "desc": "Estilo cubano, tenis y charm — oro 18k y 24k", "price": "Desde $95"},
    {"name": "Aretes", "emoji": "💎", "desc": "Argollas, dormilonas y broqueles en oro 18k y 24k", "price": "Desde $60"},
    {"name": "Dijes", "emoji": "🔱", "desc": "Religiosos, iniciales y piezas personalizadas en 18k y 24k", "price": "Desde $45"},
    {"name": "Sets de Novia", "emoji": "👰", "desc": "Conjuntos completos en oro 18k y 24k para bodas y quinceañeras", "price": "Cotización personalizada"},
]

def product_cards(card_class="product-card"):
    html = ""
    for p in PRODUCTS:
        html += f'''
        <div class="{card_class}">
            <div class="product-icon">{p['emoji']}</div>
            <h3>{p['name']}</h3>
            <p>{p['desc']}</p>
            <span class="product-price">{p['price']}</span>
            <a href="{wa_link(f"Hola! Me interesa la categoría de {p['name']} de Alba Di'Oro. ¿Me pueden dar más información?")}" class="product-btn">Preguntar por WhatsApp</a>
        </div>'''
    return html

def build(filename, css, font_import=""):
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Alba Di'Oro — Oro Italiano 18K y 24K de Elegancia Atemporal</title>
{font_import}
<style>
{css}
</style>
</head>
<body>

<nav>
    <div class="nav-container">
        <div class="logo">Alba <span>Di'Oro</span></div>
        <button class="menu-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
        <div class="nav-links">
            <a href="#coleccion">Colección</a>
            <a href="#nosotros">Nosotros</a>
            <a href="#referidos">Referidos</a>
            <a href="#contacto">Contacto</a>
            <a href="{wa_link("Hola! Quisiera más información sobre Alba Di'Oro")}" class="nav-cta">WhatsApp</a>
        </div>
    </div>
</nav>

<header class="hero">
    <div class="hero-content">
        <p class="hero-eyebrow">ORO ITALIANO · 18K &amp; 24K</p>
        <h1>Alba Di'Oro</h1>
        <div class="gold-divider"></div>
        <p class="hero-tagline">Donde el amanecer se viste de oro. Piezas exclusivas en oro puro 18k y 24k, elegancia atemporal.</p>
        <div class="hero-buttons">
            <a href="#coleccion" class="btn-primary">Ver Colección</a>
            <a href="{wa_link("Hola! Me gustaría una cotización gratis de Alba Di'Oro")}" class="btn-secondary">Cotización Gratis</a>
        </div>
    </div>
</header>

<section class="trust-bar">
    <div class="trust-item"><span>✓</span> Oro 18K &amp; 24K Certificado</div>
    <div class="trust-item"><span>✓</span> Envíos Seguros</div>
    <div class="trust-item"><span>✓</span> Garantía de Autenticidad</div>
    <div class="trust-item"><span>✓</span> Pago Flexible</div>
</section>

<section id="coleccion" class="collection">
    <div class="section-header">
        <p class="section-eyebrow">Nuestra Colección</p>
        <h2>Piezas que Cuentan tu Historia</h2>
    </div>
    <div class="products-grid">
        {product_cards()}
    </div>
</section>

<section id="nosotros" class="about">
    <div class="about-content">
        <p class="section-eyebrow">Nuestra Historia</p>
        <h2>Tradición Italiana, Pasión Latina</h2>
        <p>Alba Di'Oro nace de la pasión por el oro fino italiano en sus dos presentaciones más nobles: 18k y 24k. Cada pieza es seleccionada cuidadosamente por su calidad, diseño y durabilidad — para que brilles hoy y por generaciones.</p>
    </div>
</section>

<section id="referidos" class="referral">
    <div class="referral-content">
        <p class="section-eyebrow">Programa de Referidos</p>
        <h2>Comparte y Gana</h2>
        <p>Refiere a un amigo o familiar y ambos reciben un descuento especial en su próxima compra. Entre más compartas, más ganas.</p>
        <a href="{wa_link("Hola! Quiero más información sobre el programa de referidos de Alba Di'Oro")}" class="btn-primary">Conocer el Programa</a>
    </div>
</section>

<section id="contacto" class="contact">
    <div class="contact-content">
        <p class="section-eyebrow">Contáctanos</p>
        <h2>Agenda tu Cotización Gratuita</h2>
        <p>Escríbenos por WhatsApp y con gusto te ayudamos a encontrar la pieza perfecta en oro 18k o 24k.</p>
        <a href="{wa_link("Hola! Quisiera agendar mi cotización gratuita con Alba Di'Oro")}" class="btn-primary btn-large">Escribir por WhatsApp</a>
    </div>
</section>

<footer>
    <p>Alba Di'Oro © 2026 · Oro Italiano 18K &amp; 24K de Elegancia Atemporal</p>
</footer>

<a href="{wa_link("Hola! Vengo de la página web de Alba Di'Oro")}" class="whatsapp-float">
    <span>💬</span>
</a>

<script>
document.querySelectorAll('.nav-links a').forEach(a => {{
    a.addEventListener('click', () => document.querySelector('.nav-links').classList.remove('open'));
}});
</script>

</body>
</html>'''
    with open(f"/app/alba_dioro_demos/{filename}", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {filename}")

FONT_PLAYFAIR = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;900&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">'
FONT_CORMORANT = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'
FONT_MARCELLUS = '<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Cormorant+Garamond:wght@400;500;600&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'

BASE_CSS = '''
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Montserrat', sans-serif; overflow-x: hidden; }
.nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 22px 24px; }
.logo { font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 600; letter-spacing: 0.5px; }
.nav-links { display: flex; align-items: center; gap: 30px; }
.nav-links a { text-decoration: none; font-size: 13px; letter-spacing: 1px; text-transform: uppercase; }
.menu-toggle { display: none; background: none; border: none; font-size: 24px; cursor: pointer; }
.hero { min-height: 92vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 40px 24px; }
.hero-content { max-width: 720px; }
.hero-eyebrow { letter-spacing: 4px; font-size: 12px; margin-bottom: 20px; }
.hero h1 { font-family: 'Playfair Display', serif; font-size: 68px; margin-bottom: 20px; font-weight: 600; }
.gold-divider { width: 80px; height: 1px; margin: 0 auto 28px; }
.hero-tagline { font-size: 17px; margin-bottom: 36px; line-height: 1.7; font-weight: 300; letter-spacing: 0.3px; }
.hero-buttons { display: flex; gap: 18px; justify-content: center; flex-wrap: wrap; }
.btn-primary, .btn-secondary { padding: 16px 36px; text-decoration: none; font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase; transition: 0.35s; display: inline-block; }
.btn-large { padding: 18px 46px; font-size: 14px; }
.trust-bar { display: flex; justify-content: center; gap: 44px; padding: 26px; flex-wrap: wrap; font-size: 12px; letter-spacing: 0.5px; }
.section-header, .about-content, .referral-content, .contact-content { text-align: center; max-width: 720px; margin: 0 auto; padding: 0 24px; }
.section-eyebrow { letter-spacing: 4px; font-size: 12px; margin-bottom: 14px; }
.collection { padding: 110px 24px; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { font-family: 'Playfair Display', serif; font-size: 40px; margin-bottom: 20px; font-weight: 600; }
.products-grid { max-width: 1200px; margin: 64px auto 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
.product-card { padding: 46px 26px; text-align: center; transition: transform 0.35s; }
.product-card:hover { transform: translateY(-6px); }
.product-icon { font-size: 38px; margin-bottom: 18px; }
.product-card h3 { font-family: 'Playfair Display', serif; font-size: 21px; margin-bottom: 12px; font-weight: 600; }
.product-card p { font-size: 13.5px; line-height: 1.6; margin-bottom: 18px; opacity: 0.85; }
.product-price { display: block; font-weight: 600; margin-bottom: 20px; letter-spacing: 0.6px; font-size: 14px; }
.product-btn { display: inline-block; padding: 11px 22px; text-decoration: none; font-size: 11.5px; letter-spacing: 0.8px; text-transform: uppercase; }
.about { padding: 110px 24px; }
.about-content p { font-size: 16px; line-height: 1.9; margin-top: 22px; font-weight: 300; }
.referral { padding: 100px 24px; }
.referral-content p { font-size: 16px; line-height: 1.8; margin: 22px 0 32px; font-weight: 300; }
.contact { padding: 110px 24px; text-align: center; }
.contact-content p { font-size: 16px; margin: 22px 0 32px; font-weight: 300; }
footer { padding: 44px 24px; text-align: center; font-size: 12.5px; letter-spacing: 0.3px; }
.whatsapp-float { position: fixed; bottom: 24px; right: 24px; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; text-decoration: none; box-shadow: 0 4px 20px rgba(0,0,0,0.3); z-index: 999; }
@media (max-width: 768px) {
  .menu-toggle { display: block; }
  .nav-links { position: fixed; top: 0; right: -100%; width: 75%; height: 100vh; flex-direction: column; justify-content: center; transition: right 0.3s; z-index: 1000; }
  .nav-links.open { right: 0; }
  .hero h1 { font-size: 44px; }
  .products-grid { grid-template-columns: 1fr; }
  .trust-bar { gap: 20px; }
}
'''
print("v2 base ready")

# V6 - EMERALD NOIR & GOLD: deep emerald-black, gold serif, ultra elegant
v6_css = BASE_CSS + '''
body { background: #051912; color: #ede4cf; }
nav { position: sticky; top: 0; background: rgba(5,25,18,0.95); border-bottom: 1px solid #c9a44733; z-index: 100; backdrop-filter: blur(10px); }
.logo { color: #ede4cf; } .logo span { color: #c9a447; }
.nav-links a { color: #ede4cf; } .nav-links a:hover { color: #c9a447; }
.nav-links.open { background: #051912; border-left: 1px solid #c9a447; }
.nav-cta { background: #c9a447; color: #051912 !important; padding: 11px 22px; }
.hero { background: radial-gradient(ellipse at center, #0b2a1d 0%, #051912 75%); }
.hero-eyebrow { color: #c9a447; }
.hero h1 { color: #f5efd9; text-shadow: 0 0 50px rgba(201,164,71,0.25); }
.gold-divider { background: #c9a447; }
.hero-tagline { color: #b9c4b6; }
.btn-primary { background: #c9a447; color: #051912; }
.btn-primary:hover { background: #ddb95c; }
.btn-secondary { border: 1px solid #c9a447; color: #c9a447; }
.btn-secondary:hover { background: #c9a44722; }
.trust-bar { background: #0a2318; color: #b9c4b6; border-top: 1px solid #c9a44722; border-bottom: 1px solid #c9a44722; }
.trust-item span { color: #c9a447; }
.collection { background: #051912; }
.section-eyebrow { color: #c9a447; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #f5efd9; }
.product-card { background: #0a2318; border: 1px solid #c9a44733; color: #e5ddc4; }
.product-card:hover { border-color: #c9a447; box-shadow: 0 12px 32px rgba(201,164,71,0.18); }
.product-price { color: #c9a447; }
.product-btn { background: transparent; border: 1px solid #c9a447; color: #c9a447; }
.product-btn:hover { background: #c9a447; color: #051912; }
.about { background: #0a2318; }
.about-content p { color: #b9c4b6; }
.referral { background: #051912; }
.referral-content p { color: #b9c4b6; }
.contact { background: #0a2318; }
.contact-content p { color: #b9c4b6; }
footer { background: #051912; color: #6f8175; border-top: 1px solid #c9a44722; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v6_emerald_noir_gold.html", v6_css, font_import=FONT_PLAYFAIR)

# V7 - FOREST & CHAMPAGNE GOLD: dark forest, champagne gold
v7_css = BASE_CSS + '''
body { background: #142a1c; color: #f0ead9; }
nav { position: sticky; top: 0; background: rgba(20,42,28,0.95); border-bottom: 1px solid #d9c07a44; z-index: 100; backdrop-filter: blur(10px); }
.logo { color: #f0ead9; } .logo span { color: #d9c07a; }
.nav-links a { color: #f0ead9; } .nav-links a:hover { color: #d9c07a; }
.nav-links.open { background: #142a1c; border-left: 1px solid #d9c07a; }
.nav-cta { background: #d9c07a; color: #142a1c !important; padding: 11px 22px; }
.hero { background: linear-gradient(180deg, #1c3a26 0%, #142a1c 100%); }
.hero-eyebrow { color: #d9c07a; }
.hero h1 { color: #f5f0e0; }
.gold-divider { background: #d9c07a; }
.hero-tagline { color: #c8d2c3; }
.btn-primary { background: #d9c07a; color: #142a1c; }
.btn-primary:hover { background: #e6d193; }
.btn-secondary { border: 1px solid #d9c07a; color: #d9c07a; }
.btn-secondary:hover { background: #d9c07a22; }
.trust-bar { background: #1a331f; color: #c8d2c3; border-top: 1px solid #d9c07a33; border-bottom: 1px solid #d9c07a33; }
.trust-item span { color: #d9c07a; }
.collection { background: #142a1c; }
.section-eyebrow { color: #d9c07a; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #f5f0e0; }
.product-card { background: #1a331f; border: 1px solid #d9c07a33; color: #e8e2ce; }
.product-card:hover { border-color: #d9c07a; box-shadow: 0 12px 32px rgba(217,192,122,0.18); }
.product-price { color: #d9c07a; }
.product-btn { background: transparent; border: 1px solid #d9c07a; color: #d9c07a; }
.product-btn:hover { background: #d9c07a; color: #142a1c; }
.about { background: #1a331f; }
.about-content p { color: #c8d2c3; }
.referral { background: #142a1c; }
.referral-content p { color: #c8d2c3; }
.contact { background: #1a331f; }
.contact-content p { color: #c8d2c3; }
footer { background: #142a1c; color: #7c8c78; border-top: 1px solid #d9c07a33; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v7_forest_champagne_gold.html", v7_css, font_import=FONT_MARCELLUS)

# V8 - SAGE IVORY & GOLD: light sage/ivory, airy elegant
v8_css = BASE_CSS + '''
body { background: #f5f5ec; color: #2c3327; }
nav { position: sticky; top: 0; background: rgba(245,245,236,0.95); border-bottom: 1px solid #a99a5744; z-index: 100; backdrop-filter: blur(10px); }
.logo { color: #2c3327; } .logo span { color: #a99a57; }
.nav-links a { color: #2c3327; } .nav-links a:hover { color: #a99a57; }
.nav-links.open { background: #f5f5ec; border-left: 1px solid #a99a57; }
.nav-cta { background: #a99a57; color: #f5f5ec !important; padding: 11px 22px; }
.hero { background: linear-gradient(180deg, #f9f9f1 0%, #ebe9d5 100%); }
.hero-eyebrow { color: #8a7d3f; }
.hero h1 { color: #2c3327; }
.gold-divider { background: #a99a57; }
.hero-tagline { color: #52594a; }
.btn-primary { background: #556349; color: #f5f5ec; }
.btn-primary:hover { background: #445039; }
.btn-secondary { border: 1px solid #a99a57; color: #8a7d3f; }
.btn-secondary:hover { background: #a99a5711; }
.trust-bar { background: #ebe9d5; color: #52594a; border-top: 1px solid #a99a5744; border-bottom: 1px solid #a99a5744; }
.trust-item span { color: #a99a57; }
.collection { background: #f5f5ec; }
.section-eyebrow { color: #8a7d3f; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #2c3327; }
.product-card { background: #ffffff; border: 1px solid #ded9b8; color: #2c3327; box-shadow: 0 2px 14px rgba(85,99,73,0.06); }
.product-card:hover { border-color: #a99a57; box-shadow: 0 12px 32px rgba(169,154,87,0.18); }
.product-price { color: #8a7d3f; }
.product-btn { background: transparent; border: 1px solid #556349; color: #556349; }
.product-btn:hover { background: #556349; color: #fff; }
.about { background: #ebe9d5; }
.about-content p { color: #52594a; }
.referral { background: #f5f5ec; }
.referral-content p { color: #52594a; }
.contact { background: #ebe9d5; }
.contact-content p { color: #52594a; }
footer { background: #f5f5ec; color: #8a8a70; border-top: 1px solid #a99a5744; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v8_sage_ivory_gold.html", v8_css, font_import=FONT_CORMORANT)

print("v6 v7 v8 done")

# V9 - HUNTER GREEN & ANTIQUE GOLD: rich hunter green, muted antique gold, editorial luxury
v9_css = BASE_CSS + '''
body { background: #1b2e20; color: #ece6d3; }
nav { position: sticky; top: 0; background: rgba(27,46,32,0.96); border-bottom: 1px solid #b8975144; z-index: 100; backdrop-filter: blur(10px); }
.logo { color: #ece6d3; text-transform: uppercase; letter-spacing: 2px; } .logo span { color: #b89751; }
.nav-links a { color: #ece6d3; } .nav-links a:hover { color: #b89751; }
.nav-links.open { background: #1b2e20; border-left: 1px solid #b89751; }
.nav-cta { background: #b89751; color: #1b2e20 !important; padding: 11px 22px; }
.hero { background: radial-gradient(ellipse at bottom, #24402b 0%, #1b2e20 75%); }
.hero-eyebrow { color: #b89751; font-weight: 600; }
.hero h1 { color: #f0ead6; font-size: 72px; }
.gold-divider { background: #b89751; height: 2px; }
.hero-tagline { color: #c3c9b8; }
.btn-primary { background: #b89751; color: #1b2e20; font-weight: 600; }
.btn-primary:hover { background: #cbab68; }
.btn-secondary { border: 1.5px solid #b89751; color: #b89751; }
.btn-secondary:hover { background: #b8975122; }
.trust-bar { background: #223a29; color: #c3c9b8; border-top: 1px solid #b8975133; border-bottom: 1px solid #b8975133; }
.trust-item span { color: #b89751; }
.collection { background: #1b2e20; }
.section-eyebrow { color: #b89751; font-weight: 600; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #f0ead6; }
.product-card { background: #223a29; border: 1px solid #b8975133; color: #e5dfc9; }
.product-card:hover { border-color: #b89751; box-shadow: 0 14px 34px rgba(184,151,81,0.2); }
.product-price { color: #b89751; font-weight: 700; }
.product-btn { background: transparent; border: 1px solid #b89751; color: #b89751; }
.product-btn:hover { background: #b89751; color: #1b2e20; }
.about { background: #223a29; }
.about-content p { color: #c3c9b8; }
.referral { background: #1b2e20; }
.referral-content p { color: #c3c9b8; }
.contact { background: #223a29; }
.contact-content p { color: #c3c9b8; }
footer { background: #1b2e20; color: #7c8975; border-top: 1px solid #b8975133; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v9_hunter_antique_gold.html", v9_css, font_import=FONT_PLAYFAIR)

# V10 - JADE TWO-TONE: jade green + ivory alternating, gold hairlines, refined two-tone elegance
v10_css = BASE_CSS + '''
body { background: #fbfaf4; color: #1f3327; }
nav { position: sticky; top: 0; background: rgba(15,58,42,0.97); border-bottom: 1px solid #cdb26a44; z-index: 100; }
.logo { color: #fbfaf4; } .logo span { color: #cdb26a; }
.nav-links a { color: #fbfaf4; } .nav-links a:hover { color: #cdb26a; }
.nav-links.open { background: #0f3a2a; border-left: 1px solid #cdb26a; }
.nav-cta { background: #cdb26a; color: #0f3a2a !important; padding: 11px 22px; }
.hero { background: linear-gradient(160deg, #0f3a2a 0%, #175038 100%); color: #fbfaf4; }
.hero-eyebrow { color: #cdb26a; }
.hero h1 { color: #fbfaf4; }
.gold-divider { background: #cdb26a; }
.hero-tagline { color: #d5ddd3; }
.btn-primary { background: #cdb26a; color: #0f3a2a; }
.btn-primary:hover { background: #ddc584; }
.btn-secondary { border: 1px solid #cdb26a; color: #cdb26a; }
.btn-secondary:hover { background: #cdb26a22; }
.trust-bar { background: #0f3a2a; color: #d5ddd3; }
.trust-item span { color: #cdb26a; }
.collection { background: #fbfaf4; }
.section-eyebrow { color: #8a763f; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #1f3327; }
.product-card { background: #ffffff; border: 1px solid #dcd4b3; color: #1f3327; box-shadow: 0 2px 14px rgba(15,58,42,0.06); }
.product-card:hover { border-color: #cdb26a; box-shadow: 0 12px 32px rgba(205,178,106,0.2); }
.product-price { color: #8a763f; }
.product-btn { background: transparent; border: 1px solid #0f3a2a; color: #0f3a2a; }
.product-btn:hover { background: #0f3a2a; color: #fff; }
.about { background: #eef0e4; }
.about-content p { color: #3c4a3f; }
.referral { background: #0f3a2a; color: #fbfaf4; }
.referral-content h2 { color: #fbfaf4; }
.referral-content p { color: #d5ddd3; }
.contact { background: #eef0e4; }
.contact-content p { color: #3c4a3f; }
footer { background: #0f3a2a; color: #a9b8ab; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v10_jade_two_tone.html", v10_css, font_import=FONT_CORMORANT)

print("v9 v10 done — all 5 new variants built")
