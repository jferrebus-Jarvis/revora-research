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

def product_cards():
    html = ""
    for p in PRODUCTS:
        html += f'''
        <div class="product-card">
            <div class="product-icon">{p['emoji']}</div>
            <h3>{p['name']}</h3>
            <p>{p['desc']}</p>
            <span class="product-price">{p['price']}</span>
            <a href="{wa_link(f"Hola! Me interesa la categoría de {p['name']} de Alba Di'Oro. ¿Me pueden dar más información?")}" class="product-btn">Preguntar por WhatsApp</a>
        </div>'''
    return html

def build(filename, css, font_import, headline_font_label):
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
        <p class="font-label">Tipografía: {headline_font_label}</p>
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
        <p>Alba Di'Oro nace de la pasión por el oro fino italiano en sus dos presentaciones más nobles: 18k y 24k. Cada pieza es seleccionada cuidadosamente por su calidad, diseño y durabilidad.</p>
    </div>
</section>

<section id="referidos" class="referral">
    <div class="referral-content">
        <p class="section-eyebrow">Programa de Referidos</p>
        <h2>Comparte y Gana</h2>
        <p>Refiere a un amigo o familiar y ambos reciben un descuento especial en su próxima compra.</p>
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

BASE_CSS = '''
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Montserrat', sans-serif; overflow-x: hidden; background: #051912; color: #ede4cf; }
nav { position: sticky; top: 0; background: rgba(5,25,18,0.95); border-bottom: 1px solid #c9a44733; z-index: 100; backdrop-filter: blur(10px); }
.nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 22px 24px; }
.logo { font-size: 26px; font-weight: 600; letter-spacing: 0.5px; color: #ede4cf; }
.logo span { color: #c9a447; }
.nav-links { display: flex; align-items: center; gap: 30px; }
.nav-links a { text-decoration: none; font-size: 13px; letter-spacing: 1px; text-transform: uppercase; color: #ede4cf; }
.nav-links a:hover { color: #c9a447; }
.nav-links.open { background: #051912; border-left: 1px solid #c9a447; }
.nav-cta { background: #c9a447; color: #051912 !important; padding: 11px 22px; }
.menu-toggle { display: none; background: none; border: none; font-size: 24px; cursor: pointer; color: #ede4cf; }
.hero { min-height: 92vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 40px 24px; background: radial-gradient(ellipse at center, #0b2a1d 0%, #051912 75%); }
.hero-content { max-width: 720px; }
.hero-eyebrow { letter-spacing: 4px; font-size: 12px; margin-bottom: 20px; color: #c9a447; }
.hero h1 { font-size: 70px; margin-bottom: 20px; color: #f5efd9; text-shadow: 0 0 50px rgba(201,164,71,0.25); }
.gold-divider { width: 80px; height: 1px; margin: 0 auto 28px; background: #c9a447; }
.hero-tagline { font-size: 17px; margin-bottom: 14px; line-height: 1.7; font-weight: 300; letter-spacing: 0.3px; color: #b9c4b6; }
.font-label { font-size: 12px; letter-spacing: 1px; color: #7d8f79; margin-bottom: 28px; font-style: italic; }
.hero-buttons { display: flex; gap: 18px; justify-content: center; flex-wrap: wrap; }
.btn-primary, .btn-secondary { padding: 16px 36px; text-decoration: none; font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase; transition: 0.35s; display: inline-block; }
.btn-large { padding: 18px 46px; font-size: 14px; }
.btn-primary { background: #c9a447; color: #051912; }
.btn-primary:hover { background: #ddb95c; }
.btn-secondary { border: 1px solid #c9a447; color: #c9a447; }
.btn-secondary:hover { background: #c9a44722; }
.trust-bar { display: flex; justify-content: center; gap: 44px; padding: 26px; flex-wrap: wrap; font-size: 12px; letter-spacing: 0.5px; background: #0a2318; color: #b9c4b6; border-top: 1px solid #c9a44722; border-bottom: 1px solid #c9a44722; }
.trust-item span { color: #c9a447; }
.section-header, .about-content, .referral-content, .contact-content { text-align: center; max-width: 720px; margin: 0 auto; padding: 0 24px; }
.section-eyebrow { letter-spacing: 4px; font-size: 12px; margin-bottom: 14px; color: #c9a447; }
.collection { padding: 110px 24px; background: #051912; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { font-size: 40px; margin-bottom: 20px; font-weight: 600; color: #f5efd9; }
.products-grid { max-width: 1200px; margin: 64px auto 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
.product-card { padding: 46px 26px; text-align: center; transition: transform 0.35s; background: #0a2318; border: 1px solid #c9a44733; color: #e5ddc4; }
.product-card:hover { transform: translateY(-6px); border-color: #c9a447; box-shadow: 0 12px 32px rgba(201,164,71,0.18); }
.product-icon { font-size: 38px; margin-bottom: 18px; }
.product-card h3 { font-size: 21px; margin-bottom: 12px; font-weight: 600; }
.product-card p { font-size: 13.5px; line-height: 1.6; margin-bottom: 18px; opacity: 0.85; }
.product-price { display: block; font-weight: 600; margin-bottom: 20px; letter-spacing: 0.6px; font-size: 14px; color: #c9a447; }
.product-btn { display: inline-block; padding: 11px 22px; text-decoration: none; font-size: 11.5px; letter-spacing: 0.8px; text-transform: uppercase; background: transparent; border: 1px solid #c9a447; color: #c9a447; }
.product-btn:hover { background: #c9a447; color: #051912; }
.about { padding: 110px 24px; background: #0a2318; }
.about-content p { font-size: 16px; line-height: 1.9; margin-top: 22px; font-weight: 300; color: #b9c4b6; }
.referral { padding: 100px 24px; background: #051912; }
.referral-content p { font-size: 16px; line-height: 1.8; margin: 22px 0 32px; font-weight: 300; color: #b9c4b6; }
.contact { padding: 110px 24px; text-align: center; background: #0a2318; }
.contact-content p { font-size: 16px; margin: 22px 0 32px; font-weight: 300; color: #b9c4b6; }
footer { padding: 44px 24px; text-align: center; font-size: 12.5px; letter-spacing: 0.3px; background: #051912; color: #6f8175; border-top: 1px solid #c9a44722; }
.whatsapp-float { position: fixed; bottom: 24px; right: 24px; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; text-decoration: none; box-shadow: 0 4px 20px rgba(0,0,0,0.3); z-index: 999; background: #25D366; color: white; }
@media (max-width: 768px) {
  .menu-toggle { display: block; }
  .nav-links { position: fixed; top: 0; right: -100%; width: 75%; height: 100vh; flex-direction: column; justify-content: center; transition: right 0.3s; z-index: 1000; }
  .nav-links.open { right: 0; }
  .hero h1 { font-size: 44px; }
  .products-grid { grid-template-columns: 1fr; }
  .trust-bar { gap: 20px; }
}
'''
print("base ready")

# TYPE A - BODONI MODA: high-fashion editorial serif (like Vogue/Cartier)
font_a = '<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,500;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">'
css_a = BASE_CSS + '''
.logo { font-family: 'Bodoni Moda', serif; }
.hero h1 { font-family: 'Bodoni Moda', serif; font-weight: 500; letter-spacing: 1px; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { font-family: 'Bodoni Moda', serif; }
.product-card h3 { font-family: 'Bodoni Moda', serif; }
'''
build("t1_bodoni_moda.html", css_a, font_a, "Bodoni Moda — editorial de alta costura")

# TYPE B - CINZEL + CORMORANT: regal, engraved, monogram feel
font_b = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Cormorant+Garamond:wght@400;500;600&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'
css_b = BASE_CSS + '''
.logo { font-family: 'Cinzel', serif; letter-spacing: 2px; }
.hero h1 { font-family: 'Cinzel', serif; font-weight: 600; letter-spacing: 3px; font-size: 58px; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { font-family: 'Cormorant Garamond', serif; font-size: 44px; font-weight: 600; }
.product-card h3 { font-family: 'Cormorant Garamond', serif; font-size: 24px; }
'''
build("t2_cinzel_regal.html", css_b, font_b, "Cinzel + Cormorant Garamond — grabado real")

# TYPE C - ITALIANA: ultra-thin luxury boutique serif
font_c = '<link href="https://fonts.googleapis.com/css2?family=Italiana&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">'
css_c = BASE_CSS + '''
.logo { font-family: 'Italiana', serif; letter-spacing: 1px; }
.hero h1 { font-family: 'Italiana', serif; font-weight: 400; letter-spacing: 2px; font-size: 66px; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2 { font-family: 'Italiana', serif; font-weight: 400; }
.product-card h3 { font-family: 'Italiana', serif; font-weight: 400; letter-spacing: 0.5px; }
'''
build("t3_italiana_boutique.html", css_c, font_c, "Italiana — boutique ultra fina")

print("3 font variants built")
