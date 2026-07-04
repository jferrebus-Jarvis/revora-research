import os

WHATSAPP_NUM = "18328441734"

def wa_link(msg):
    import urllib.parse
    return f"https://wa.me/{WHATSAPP_NUM}?text={urllib.parse.quote(msg)}"

PRODUCTS = [
    {"name": "Anillos", "emoji": "💍", "desc": "Oro italiano 18k, diseños clásicos y contemporáneos", "price": "Desde $85"},
    {"name": "Cadenas y Collares", "emoji": "📿", "desc": "Piezas macizas y laminadas, cierres reforzados", "price": "Desde $120"},
    {"name": "Pulseras", "emoji": "✨", "desc": "Estilo cubano, tenis y charm, para toda ocasión", "price": "Desde $95"},
    {"name": "Aretes", "emoji": "💎", "desc": "Argollas, dormilonas y broqueles en oro fino", "price": "Desde $60"},
    {"name": "Dijes", "emoji": "🔱", "desc": "Religiosos, iniciales y piezas personalizadas", "price": "Desde $45"},
    {"name": "Sets de Novia", "emoji": "👰", "desc": "Conjuntos completos para bodas y quinceañeras", "price": "Cotización personalizada"},
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

def build(filename, css, hero_extra="", font_import="", nav_class="", body_class="", extra_sections=""):
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Alba Di'Oro — Oro Italiano de Elegancia Atemporal</title>
{font_import}
<style>
{css}
</style>
</head>
<body class="{body_class}">

<nav class="{nav_class}">
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
        <p class="hero-eyebrow">ORO ITALIANO · 18K</p>
        <h1>Alba Di'Oro</h1>
        <p class="hero-tagline">Donde el amanecer se viste de oro. Piezas finas, elegancia atemporal.</p>
        <div class="hero-buttons">
            <a href="#coleccion" class="btn-primary">Ver Colección</a>
            <a href="{wa_link("Hola! Me gustaría una cotización gratis de Alba Di'Oro")}" class="btn-secondary">Cotización Gratis</a>
        </div>
    </div>
    {hero_extra}
</header>

<section class="trust-bar">
    <div class="trust-item"><span>✓</span> Oro Italiano Certificado</div>
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
        <p>Alba Di'Oro nace de la pasión por el oro fino italiano y el deseo de traer piezas auténticas y elegantes a nuestra comunidad. Cada pieza es seleccionada cuidadosamente por su calidad, diseño y durabilidad — para que brilles hoy y por generaciones.</p>
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

{extra_sections}

<section id="contacto" class="contact">
    <div class="contact-content">
        <p class="section-eyebrow">Contáctanos</p>
        <h2>Agenda tu Cotización Gratuita</h2>
        <p>Escríbenos por WhatsApp y con gusto te ayudamos a encontrar la pieza perfecta.</p>
        <a href="{wa_link("Hola! Quisiera agendar mi cotización gratuita con Alba Di'Oro")}" class="btn-primary btn-large">Escribir por WhatsApp</a>
    </div>
</section>

<footer>
    <p>Alba Di'Oro © 2026 · Oro Italiano de Elegancia Atemporal</p>
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

print("Generator ready")

FONT_PLAYFAIR = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">'
FONT_CORMORANT = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'

BASE_CSS = '''
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Montserrat', sans-serif; overflow-x: hidden; }
.nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 20px 24px; }
.logo { font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 700; }
.nav-links { display: flex; align-items: center; gap: 28px; }
.nav-links a { text-decoration: none; font-size: 14px; letter-spacing: 0.5px; }
.menu-toggle { display: none; background: none; border: none; font-size: 24px; cursor: pointer; }
.hero { min-height: 90vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 40px 24px; }
.hero-content { max-width: 700px; }
.hero-eyebrow { letter-spacing: 3px; font-size: 13px; margin-bottom: 16px; }
.hero h1 { font-family: 'Playfair Display', serif; font-size: 64px; margin-bottom: 20px; }
.hero-tagline { font-size: 18px; margin-bottom: 32px; line-height: 1.6; }
.hero-buttons { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.btn-primary, .btn-secondary { padding: 15px 32px; text-decoration: none; font-size: 14px; letter-spacing: 1px; border-radius: 2px; transition: 0.3s; display: inline-block; }
.btn-large { padding: 18px 44px; font-size: 15px; }
.trust-bar { display: flex; justify-content: center; gap: 40px; padding: 24px; flex-wrap: wrap; font-size: 13px; }
.section-header, .about-content, .referral-content, .contact-content { text-align: center; max-width: 700px; margin: 0 auto; padding: 0 24px; }
.section-eyebrow { letter-spacing: 3px; font-size: 12px; margin-bottom: 12px; }
.collection { padding: 100px 24px; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { font-family: 'Playfair Display', serif; font-size: 40px; margin-bottom: 20px; }
.products-grid { max-width: 1200px; margin: 60px auto 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
.product-card { padding: 40px 24px; text-align: center; border-radius: 4px; transition: transform 0.3s; }
.product-card:hover { transform: translateY(-6px); }
.product-icon { font-size: 40px; margin-bottom: 16px; }
.product-card h3 { font-family: 'Playfair Display', serif; font-size: 22px; margin-bottom: 10px; }
.product-card p { font-size: 14px; line-height: 1.5; margin-bottom: 16px; opacity: 0.85; }
.product-price { display: block; font-weight: 600; margin-bottom: 18px; letter-spacing: 0.5px; }
.product-btn { display: inline-block; padding: 10px 20px; text-decoration: none; font-size: 12px; letter-spacing: 0.5px; border-radius: 2px; }
.about { padding: 100px 24px; }
.about-content p { font-size: 16px; line-height: 1.8; margin-top: 20px; }
.referral { padding: 90px 24px; }
.referral-content p { font-size: 16px; line-height: 1.7; margin: 20px 0 30px; }
.contact { padding: 100px 24px; text-align: center; }
.contact-content p { font-size: 16px; margin: 20px 0 30px; }
footer { padding: 40px 24px; text-align: center; font-size: 13px; }
.whatsapp-float { position: fixed; bottom: 24px; right: 24px; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; text-decoration: none; box-shadow: 0 4px 20px rgba(0,0,0,0.3); z-index: 999; }
@media (max-width: 768px) {
  .menu-toggle { display: block; }
  .nav-links { position: fixed; top: 0; right: -100%; width: 75%; height: 100vh; flex-direction: column; justify-content: center; transition: right 0.3s; z-index: 1000; }
  .nav-links.open { right: 0; }
  .hero h1 { font-size: 42px; }
  .products-grid { grid-template-columns: 1fr; }
  .trust-bar { gap: 20px; }
}
'''
print("base css loaded")

# V1 - NOIR GOLD: black bg, gold serif, ornate luxury
v1_css = BASE_CSS + '''
body { background: #0a0908; color: #f0e6d2; }
nav { position: sticky; top: 0; background: rgba(10,9,8,0.95); border-bottom: 1px solid #d4af3733; z-index: 100; backdrop-filter: blur(8px); }
.logo span { color: #d4af37; }
.nav-links a { color: #f0e6d2; }
.nav-links a:hover { color: #d4af37; }
.nav-links.open { background: #0a0908; border-left: 1px solid #d4af37; }
.nav-cta { background: #d4af37; color: #0a0908 !important; padding: 10px 20px; border-radius: 2px; }
.hero { background: radial-gradient(ellipse at center, #1a1712 0%, #0a0908 70%); }
.hero-eyebrow { color: #d4af37; }
.hero h1 { color: #f5eddb; text-shadow: 0 0 40px rgba(212,175,55,0.3); }
.hero-tagline { color: #c9bfa8; }
.btn-primary { background: #d4af37; color: #0a0908; }
.btn-primary:hover { background: #e8c659; }
.btn-secondary { border: 1px solid #d4af37; color: #d4af37; }
.btn-secondary:hover { background: #d4af3722; }
.trust-bar { background: #14120e; color: #c9bfa8; border-top: 1px solid #d4af3722; border-bottom: 1px solid #d4af3722; }
.trust-item span { color: #d4af37; }
.collection { background: #0a0908; }
.section-eyebrow { color: #d4af37; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #f5eddb; }
.product-card { background: #14120e; border: 1px solid #d4af3733; color: #e8dfc9; }
.product-card:hover { border-color: #d4af37; box-shadow: 0 10px 30px rgba(212,175,55,0.15); }
.product-price { color: #d4af37; }
.product-btn { background: transparent; border: 1px solid #d4af37; color: #d4af37; }
.product-btn:hover { background: #d4af37; color: #0a0908; }
.about { background: #14120e; }
.about-content p { color: #c9bfa8; }
.referral { background: #0a0908; }
.referral-content p { color: #c9bfa8; }
.contact { background: #14120e; }
.contact-content p { color: #c9bfa8; }
footer { background: #0a0908; color: #8a8070; border-top: 1px solid #d4af3722; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v1_noir_gold.html", v1_css, font_import=FONT_PLAYFAIR)

# V2 - IVORY ELEGANCE: cream bg, gold accents, refined
v2_css = BASE_CSS + '''
body { background: #faf6ee; color: #2e2a22; }
nav { position: sticky; top: 0; background: rgba(250,246,238,0.95); border-bottom: 1px solid #d4af3744; z-index: 100; backdrop-filter: blur(8px); }
.logo span { color: #b8912f; }
.nav-links a { color: #2e2a22; }
.nav-links a:hover { color: #b8912f; }
.nav-links.open { background: #faf6ee; border-left: 1px solid #b8912f; }
.nav-cta { background: #b8912f; color: #faf6ee !important; padding: 10px 20px; border-radius: 2px; }
.hero { background: linear-gradient(180deg, #fdfbf6 0%, #f3ecdb 100%); }
.hero-eyebrow { color: #b8912f; }
.hero h1 { color: #2e2a22; }
.hero-tagline { color: #5c5646; }
.btn-primary { background: #b8912f; color: #fff; }
.btn-primary:hover { background: #a17f28; }
.btn-secondary { border: 1px solid #b8912f; color: #b8912f; }
.btn-secondary:hover { background: #b8912f11; }
.trust-bar { background: #f3ecdb; color: #5c5646; border-top: 1px solid #d4af3744; border-bottom: 1px solid #d4af3744; }
.trust-item span { color: #b8912f; }
.collection { background: #faf6ee; }
.section-eyebrow { color: #b8912f; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #2e2a22; }
.product-card { background: #fff; border: 1px solid #e5dcc3; color: #2e2a22; box-shadow: 0 2px 12px rgba(0,0,0,0.04); }
.product-card:hover { border-color: #b8912f; box-shadow: 0 10px 30px rgba(184,145,47,0.15); }
.product-price { color: #b8912f; }
.product-btn { background: transparent; border: 1px solid #b8912f; color: #b8912f; }
.product-btn:hover { background: #b8912f; color: #fff; }
.about { background: #f3ecdb; }
.about-content p { color: #5c5646; }
.referral { background: #faf6ee; }
.referral-content p { color: #5c5646; }
.contact { background: #f3ecdb; }
.contact-content p { color: #5c5646; }
footer { background: #faf6ee; color: #8a8370; border-top: 1px solid #d4af3744; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v2_ivory_elegance.html", v2_css, font_import=FONT_CORMORANT)
print("v1 v2 done")

# V3 - MIDNIGHT OPULENCE: deep navy/gold, royal feel
v3_css = BASE_CSS + '''
body { background: #0d1526; color: #e8e4d8; }
nav { position: sticky; top: 0; background: rgba(13,21,38,0.95); border-bottom: 1px solid #c9a64733; z-index: 100; backdrop-filter: blur(8px); }
.logo span { color: #c9a647; }
.nav-links a { color: #e8e4d8; }
.nav-links a:hover { color: #c9a647; }
.nav-links.open { background: #0d1526; border-left: 1px solid #c9a647; }
.nav-cta { background: #c9a647; color: #0d1526 !important; padding: 10px 20px; border-radius: 2px; }
.hero { background: radial-gradient(ellipse at top, #1a2740 0%, #0d1526 70%); }
.hero-eyebrow { color: #c9a647; }
.hero h1 { color: #f2eedc; }
.hero-tagline { color: #b6bcc9; }
.btn-primary { background: #c9a647; color: #0d1526; }
.btn-primary:hover { background: #ddb955; }
.btn-secondary { border: 1px solid #c9a647; color: #c9a647; }
.btn-secondary:hover { background: #c9a64722; }
.trust-bar { background: #131f38; color: #b6bcc9; border-top: 1px solid #c9a64722; border-bottom: 1px solid #c9a64722; }
.trust-item span { color: #c9a647; }
.collection { background: #0d1526; }
.section-eyebrow { color: #c9a647; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #f2eedc; }
.product-card { background: #131f38; border: 1px solid #c9a64733; color: #e8e4d8; }
.product-card:hover { border-color: #c9a647; box-shadow: 0 10px 30px rgba(201,166,71,0.15); }
.product-price { color: #c9a647; }
.product-btn { background: transparent; border: 1px solid #c9a647; color: #c9a647; }
.product-btn:hover { background: #c9a647; color: #0d1526; }
.about { background: #131f38; }
.about-content p { color: #b6bcc9; }
.referral { background: #0d1526; }
.referral-content p { color: #b6bcc9; }
.contact { background: #131f38; }
.contact-content p { color: #b6bcc9; }
footer { background: #0d1526; color: #6e7688; border-top: 1px solid #c9a64722; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v3_midnight_opulence.html", v3_css, font_import=FONT_PLAYFAIR)

# V4 - ROSA ORO: blush pink + rose gold, feminine elegant
v4_css = BASE_CSS + '''
body { background: #fdf3f0; color: #3d2c2a; }
nav { position: sticky; top: 0; background: rgba(253,243,240,0.95); border-bottom: 1px solid #d9998544; z-index: 100; backdrop-filter: blur(8px); }
.logo span { color: #b8755f; }
.nav-links a { color: #3d2c2a; }
.nav-links a:hover { color: #b8755f; }
.nav-links.open { background: #fdf3f0; border-left: 1px solid #b8755f; }
.nav-cta { background: #b8755f; color: #fdf3f0 !important; padding: 10px 20px; border-radius: 2px; }
.hero { background: linear-gradient(160deg, #fdf3f0 0%, #f6e3dc 100%); }
.hero-eyebrow { color: #b8755f; }
.hero h1 { color: #3d2c2a; }
.hero-tagline { color: #6b524d; }
.btn-primary { background: #b8755f; color: #fff; }
.btn-primary:hover { background: #a2634f; }
.btn-secondary { border: 1px solid #b8755f; color: #b8755f; }
.btn-secondary:hover { background: #b8755f11; }
.trust-bar { background: #f6e3dc; color: #6b524d; border-top: 1px solid #d9998544; border-bottom: 1px solid #d9998544; }
.trust-item span { color: #b8755f; }
.collection { background: #fdf3f0; }
.section-eyebrow { color: #b8755f; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #3d2c2a; }
.product-card { background: #fff; border: 1px solid #ecd5cb; color: #3d2c2a; box-shadow: 0 2px 12px rgba(184,117,95,0.06); }
.product-card:hover { border-color: #b8755f; box-shadow: 0 10px 30px rgba(184,117,95,0.18); }
.product-price { color: #b8755f; }
.product-btn { background: transparent; border: 1px solid #b8755f; color: #b8755f; }
.product-btn:hover { background: #b8755f; color: #fff; }
.about { background: #f6e3dc; }
.about-content p { color: #6b524d; }
.referral { background: #fdf3f0; }
.referral-content p { color: #6b524d; }
.contact { background: #f6e3dc; }
.contact-content p { color: #6b524d; }
footer { background: #fdf3f0; color: #9a8079; border-top: 1px solid #d9998544; }
.whatsapp-float { background: #25D366; color: white; }
'''
build("v4_rosa_oro.html", v4_css, font_import=FONT_CORMORANT)
print("v3 v4 done")

# V5 - BOLD EDITORIAL: magazine style, black/white/gold, huge type
v5_css = BASE_CSS + '''
body { background: #ffffff; color: #111111; }
nav { position: sticky; top: 0; background: #ffffff; border-bottom: 2px solid #111111; z-index: 100; }
.logo { text-transform: uppercase; letter-spacing: 2px; }
.logo span { color: #b8912f; }
.nav-links a { color: #111111; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; }
.nav-links a:hover { color: #b8912f; }
.nav-links.open { background: #ffffff; border-left: 2px solid #111111; }
.nav-cta { background: #111111; color: #fff !important; padding: 10px 20px; }
.hero { background: #ffffff; border-bottom: 2px solid #111111; }
.hero-eyebrow { color: #b8912f; font-weight: 600; }
.hero h1 { color: #111111; font-size: 84px; text-transform: uppercase; letter-spacing: -1px; }
.hero-tagline { color: #444444; text-transform: uppercase; font-size: 14px; letter-spacing: 1px; }
.btn-primary { background: #111111; color: #fff; border-radius: 0; text-transform: uppercase; }
.btn-primary:hover { background: #b8912f; }
.btn-secondary { border: 2px solid #111111; color: #111111; border-radius: 0; text-transform: uppercase; }
.btn-secondary:hover { background: #111111; color: #fff; }
.trust-bar { background: #111111; color: #fff; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; }
.trust-item span { color: #b8912f; }
.collection { background: #ffffff; }
.section-eyebrow { color: #b8912f; font-weight: 600; text-transform: uppercase; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { color: #111111; text-transform: uppercase; letter-spacing: -0.5px; }
.product-card { background: #fff; border: 2px solid #111111; color: #111111; border-radius: 0; }
.product-card:hover { background: #111111; color: #fff; }
.product-card:hover .product-price { color: #b8912f; }
.product-price { color: #b8912f; font-weight: 700; }
.product-btn { background: #111111; color: #fff; border-radius: 0; text-transform: uppercase; font-size: 11px; }
.product-card:hover .product-btn { background: #b8912f; color: #111; }
.about { background: #f7f7f7; border-top: 2px solid #111; border-bottom: 2px solid #111; }
.about-content p { color: #333333; }
.referral { background: #ffffff; }
.referral-content p { color: #333333; }
.contact { background: #111111; color: #fff; }
.contact-content h2 { color: #fff; }
.contact-content p { color: #ccc; }
footer { background: #111111; color: #999; }
.whatsapp-float { background: #25D366; color: white; border-radius: 50%; }
'''
build("v5_bold_editorial.html", v5_css, font_import=FONT_PLAYFAIR)
print("v5 done - all 5 variants built")
