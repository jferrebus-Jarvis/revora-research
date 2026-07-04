import urllib.parse
WHATSAPP_NUM = "18328441734"

def wa_link(msg):
    return f"https://wa.me/{WHATSAPP_NUM}?text={urllib.parse.quote(msg)}"

HERO_IMG = "https://media.base44.com/images/public/6a3581bb2a25b2dfe23bf70e/4efabffa7_generated_image.png"
IMG_ANILLOS = "https://media.base44.com/images/public/6a3581bb2a25b2dfe23bf70e/95842b2b7_generated_image.png"
IMG_CADENAS = "https://media.base44.com/images/public/6a3581bb2a25b2dfe23bf70e/51466ed86_generated_image.png"
IMG_PULSERAS = "https://media.base44.com/images/public/6a3581bb2a25b2dfe23bf70e/b7266fc79_generated_image.png"
IMG_ARETES = "https://media.base44.com/images/public/6a3581bb2a25b2dfe23bf70e/b35e48537_generated_image.png"
IMG_DIJES = "https://media.base44.com/images/public/6a3581bb2a25b2dfe23bf70e/06ae1bd34_generated_image.png"
IMG_NOVIA = "https://media.base44.com/images/public/6a3581bb2a25b2dfe23bf70e/a4e394ee0_generated_image.png"

PRODUCTS = [
    {"name": "Anillos", "img": IMG_ANILLOS, "desc": "Oro italiano 18k y 24k, diseños clásicos y contemporáneos", "price": "Desde $85"},
    {"name": "Cadenas y Collares", "img": IMG_CADENAS, "desc": "Piezas macizas en oro 18k y 24k, cierres reforzados", "price": "Desde $120"},
    {"name": "Pulseras", "img": IMG_PULSERAS, "desc": "Estilo cubano, tenis y charm — oro 18k y 24k", "price": "Desde $95"},
    {"name": "Aretes", "img": IMG_ARETES, "desc": "Argollas, dormilonas y broqueles en oro 18k y 24k", "price": "Desde $60"},
    {"name": "Dijes", "img": IMG_DIJES, "desc": "Religiosos, iniciales y piezas personalizadas en 18k y 24k", "price": "Desde $45"},
    {"name": "Sets de Novia", "img": IMG_NOVIA, "desc": "Conjuntos completos en oro 18k y 24k para bodas y quinceañeras", "price": "Cotización personalizada"},
]

TESTIMONIALS = [
    {"quote": "Compré una cadena de oro 24k y la calidad es impresionante. Se nota que es oro italiano real.", "name": "Maria G."},
    {"quote": "El servicio por WhatsApp fue rapidísimo y muy personal. Ya voy en mi tercera compra.", "name": "Carlos R."},
    {"quote": "El set de novia que me hicieron para mi boda quedó perfecto. Piezas hermosas y de excelente calidad.", "name": "Yesenia P."},
]

FAQS = [
    {"q": "¿El oro es garantizado 18k y 24k?", "a": "Sí, todas nuestras piezas son de oro italiano certificado, disponible exclusivamente en 18k y 24k."},
    {"q": "¿Cómo funciona el proceso de compra?", "a": "Nos escribes por WhatsApp, te mostramos fotos y videos de las piezas disponibles, y coordinamos el pago y envío o entrega."},
    {"q": "¿Hacen envíos?", "a": "Sí, hacemos envíos seguros y asegurados a todo el país. También ofrecemos entrega personal en área local."},
    {"q": "¿Tienen garantía las piezas?", "a": "Todas nuestras piezas cuentan con garantía de autenticidad y respaldo post-venta."},
]

def product_cards():
    html = ""
    for p in PRODUCTS:
        html += f'''
        <div class="product-card fade-in">
            <div class="product-img-wrap"><img src="{p['img']}" alt="{p['name']}" loading="lazy"></div>
            <div class="product-info">
                <h3>{p['name']}</h3>
                <p>{p['desc']}</p>
                <span class="product-price">{p['price']}</span>
                <a href="{wa_link(f"Hola! Me interesa la categoría de {p['name']} de Alba Di'Oro. ¿Me pueden dar más información?")}" class="product-btn">Preguntar por WhatsApp</a>
            </div>
        </div>'''
    return html

def testimonial_cards():
    html = ""
    for t in TESTIMONIALS:
        html += f'''
        <div class="testimonial-card fade-in">
            <p class="stars">★★★★★</p>
            <p class="testimonial-quote">"{t['quote']}"</p>
            <p class="testimonial-name">— {t['name']}</p>
        </div>'''
    return html

def faq_items():
    html = ""
    for i, f in enumerate(FAQS):
        html += f'''
        <div class="faq-item fade-in">
            <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
                <span>{f['q']}</span>
                <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><p>{f['a']}</p></div>
        </div>'''
    return html

with open("/app/alba_dioro_demos/final_site.py.html_body", "w") as f:
    pass

print("prep done")

CSS = '''
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { font-family: 'Montserrat', sans-serif; overflow-x: hidden; background: #051912; color: #ede4cf; }

/* NAV */
nav { position: sticky; top: 0; background: rgba(5,25,18,0.92); border-bottom: 1px solid #c9a44733; z-index: 1000; backdrop-filter: blur(12px); transition: 0.3s; }
.nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 20px 24px; }
.logo { font-family: 'Italiana', serif; font-size: 28px; letter-spacing: 1px; color: #ede4cf; }
.logo span { color: #c9a447; }
.nav-links { display: flex; align-items: center; gap: 32px; }
.nav-links a { text-decoration: none; font-size: 12.5px; letter-spacing: 1.2px; text-transform: uppercase; color: #ede4cf; transition: 0.25s; }
.nav-links a:hover { color: #c9a447; }
.nav-cta { background: #c9a447; color: #051912 !important; padding: 11px 24px; border-radius: 1px; }
.nav-cta:hover { background: #ddb95c !important; }
.menu-toggle { display: none; background: none; border: none; font-size: 26px; cursor: pointer; color: #ede4cf; }

/* HERO */
.hero { position: relative; min-height: 100vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 100px 24px 60px; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; background-image: url('__HERO_IMG__'); background-size: cover; background-position: center; opacity: 0.38; }
.hero-overlay { position: absolute; inset: 0; background: radial-gradient(ellipse at center, rgba(5,25,18,0.55) 0%, rgba(5,25,18,0.96) 85%); }
.hero-content { position: relative; z-index: 2; max-width: 760px; }
.hero-eyebrow { letter-spacing: 4px; font-size: 12px; margin-bottom: 22px; color: #c9a447; font-weight: 500; }
.hero h1 { font-family: 'Italiana', serif; font-size: 84px; margin-bottom: 22px; color: #f5efd9; text-shadow: 0 0 60px rgba(201,164,71,0.3); letter-spacing: 2px; }
.gold-divider { width: 90px; height: 1px; margin: 0 auto 30px; background: linear-gradient(90deg, transparent, #c9a447, transparent); }
.hero-tagline { font-size: 18px; margin-bottom: 40px; line-height: 1.8; font-weight: 300; letter-spacing: 0.3px; color: #c3cdbf; }
.hero-buttons { display: flex; gap: 18px; justify-content: center; flex-wrap: wrap; }
.btn-primary, .btn-secondary { padding: 17px 38px; text-decoration: none; font-size: 13px; letter-spacing: 1.8px; text-transform: uppercase; transition: 0.35s; display: inline-block; }
.btn-large { padding: 19px 48px; font-size: 14px; }
.btn-primary { background: #c9a447; color: #051912; }
.btn-primary:hover { background: #ddb95c; transform: translateY(-2px); }
.btn-secondary { border: 1px solid #c9a447; color: #c9a447; }
.btn-secondary:hover { background: #c9a44722; transform: translateY(-2px); }
.scroll-cue { position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); font-size: 11px; letter-spacing: 2px; color: #7d8f79; z-index: 2; animation: bounce 2.2s infinite; }
@keyframes bounce { 0%,100% { transform: translate(-50%,0);} 50% { transform: translate(-50%,8px);} }

/* TRUST BAR */
.trust-bar { display: flex; justify-content: center; gap: 48px; padding: 28px; flex-wrap: wrap; font-size: 12px; letter-spacing: 0.6px; background: #0a2318; color: #b9c4b6; border-top: 1px solid #c9a44722; border-bottom: 1px solid #c9a44722; }
.trust-item span { color: #c9a447; margin-right: 4px; }

/* SECTION HEADERS */
.section-header, .about-content, .referral-content, .contact-content { text-align: center; max-width: 760px; margin: 0 auto; padding: 0 24px; }
.section-eyebrow { letter-spacing: 4px; font-size: 12px; margin-bottom: 16px; color: #c9a447; font-weight: 500; }
.collection h2, .about-content h2, .referral-content h2, .contact-content h2, .testimonials h2, .faq h2 { font-family: 'Italiana', serif; font-size: 46px; margin-bottom: 22px; letter-spacing: 1px; color: #f5efd9; }

/* COLLECTION */
.collection { padding: 130px 24px; background: #051912; }
.products-grid { max-width: 1200px; margin: 70px auto 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 34px; }
.product-card { background: #0a2318; border: 1px solid #c9a44733; overflow: hidden; transition: transform 0.4s, box-shadow 0.4s; }
.product-card:hover { transform: translateY(-8px); border-color: #c9a447; box-shadow: 0 20px 45px rgba(201,164,71,0.2); }
.product-img-wrap { width: 100%; height: 240px; overflow: hidden; }
.product-img-wrap img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s; }
.product-card:hover .product-img-wrap img { transform: scale(1.08); }
.product-info { padding: 30px 26px; text-align: center; }
.product-card h3 { font-family: 'Italiana', serif; font-size: 23px; margin-bottom: 12px; letter-spacing: 0.5px; }
.product-card p { font-size: 13.5px; line-height: 1.6; margin-bottom: 18px; opacity: 0.85; }
.product-price { display: block; font-weight: 600; margin-bottom: 20px; letter-spacing: 0.6px; font-size: 14px; color: #c9a447; }
.product-btn { display: inline-block; padding: 11px 22px; text-decoration: none; font-size: 11px; letter-spacing: 1px; text-transform: uppercase; background: transparent; border: 1px solid #c9a447; color: #c9a447; transition: 0.3s; }
.product-btn:hover { background: #c9a447; color: #051912; }

/* ABOUT */
.about { padding: 130px 24px; background: #0a2318; }
.about-content p { font-size: 17px; line-height: 2; margin-top: 26px; font-weight: 300; color: #c3cdbf; }
.about-stats { display: flex; justify-content: center; gap: 60px; margin-top: 50px; flex-wrap: wrap; }
.stat { text-align: center; }
.stat-number { font-family: 'Italiana', serif; font-size: 42px; color: #c9a447; display: block; }
.stat-label { font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: #8a9a86; margin-top: 6px; }

/* TESTIMONIALS */
.testimonials { padding: 120px 24px; background: #051912; text-align: center; }
.testimonials-grid { max-width: 1100px; margin: 60px auto 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
.testimonial-card { background: #0a2318; border: 1px solid #c9a44733; padding: 40px 28px; }
.stars { color: #c9a447; margin-bottom: 18px; letter-spacing: 3px; }
.testimonial-quote { font-size: 14.5px; line-height: 1.8; font-style: italic; color: #d5dccb; margin-bottom: 20px; font-weight: 300; }
.testimonial-name { font-size: 13px; letter-spacing: 1px; color: #c9a447; }

/* FAQ */
.faq { padding: 120px 24px; background: #0a2318; }
.faq-list { max-width: 760px; margin: 60px auto 0; }
.faq-item { border-bottom: 1px solid #c9a44733; }
.faq-question { width: 100%; background: none; border: none; padding: 26px 4px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; text-align: left; font-size: 16px; color: #ede4cf; font-family: 'Montserrat', sans-serif; }
.faq-icon { color: #c9a447; font-size: 22px; transition: 0.3s; }
.faq-item.open .faq-icon { transform: rotate(45deg); }
.faq-answer { max-height: 0; overflow: hidden; transition: max-height 0.35s ease; }
.faq-item.open .faq-answer { max-height: 200px; }
.faq-answer p { padding: 0 4px 26px; font-size: 14.5px; line-height: 1.8; color: #b9c4b6; font-weight: 300; }

/* REFERRAL */
.referral { padding: 110px 24px; background: #051912; }
.referral-content p { font-size: 16px; line-height: 1.9; margin: 22px 0 34px; font-weight: 300; color: #b9c4b6; }

/* CONTACT */
.contact { padding: 130px 24px; text-align: center; background: linear-gradient(180deg, #0a2318 0%, #051912 100%); }
.contact-content p { font-size: 17px; margin: 22px 0 36px; font-weight: 300; color: #b9c4b6; }

footer { padding: 50px 24px 30px; text-align: center; font-size: 12.5px; letter-spacing: 0.3px; background: #051912; color: #6f8175; border-top: 1px solid #c9a44722; }
footer .footer-logo { font-family: 'Italiana', serif; font-size: 22px; color: #c9a447; margin-bottom: 14px; }

.whatsapp-float { position: fixed; bottom: 26px; right: 26px; width: 62px; height: 62px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 30px; text-decoration: none; box-shadow: 0 6px 24px rgba(0,0,0,0.4); z-index: 999; background: #25D366; color: white; animation: pulse 2.5s infinite; }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(37,211,102,0.5);} 70% { box-shadow: 0 0 0 14px rgba(37,211,102,0);} 100% { box-shadow: 0 0 0 0 rgba(37,211,102,0);} }

.fade-in { opacity: 0; transform: translateY(24px); transition: opacity 0.7s ease, transform 0.7s ease; }
.fade-in.visible { opacity: 1; transform: translateY(0); }

@media (max-width: 900px) {
  .products-grid, .testimonials-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
  .menu-toggle { display: block; }
  .nav-links { position: fixed; top: 0; right: -100%; width: 78%; height: 100vh; flex-direction: column; justify-content: center; gap: 26px; transition: right 0.35s; z-index: 1000; background: #051912; border-left: 1px solid #c9a447; }
  .nav-links.open { right: 0; }
  .hero h1 { font-size: 48px; }
  .products-grid, .testimonials-grid { grid-template-columns: 1fr; }
  .about-stats { gap: 30px; }
  .trust-bar { gap: 20px; }
}
'''.replace("__HERO_IMG__", HERO_IMG)

print("css ready")

FONT_IMPORT = '<link href="https://fonts.googleapis.com/css2?family=Italiana&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">'

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Alba Di'Oro — Oro Italiano 18K y 24K de Elegancia Atemporal</title>
<meta name="description" content="Alba Di'Oro — joyería fina en oro italiano 18k y 24k. Anillos, cadenas, pulseras y más. Cotización gratis por WhatsApp.">
{FONT_IMPORT}
<style>
{CSS}
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
            <a href="#testimonios">Testimonios</a>
            <a href="#referidos">Referidos</a>
            <a href="#faq">Preguntas</a>
            <a href="{wa_link("Hola! Quisiera más información sobre Alba Di'Oro")}" class="nav-cta">WhatsApp</a>
        </div>
    </div>
</nav>

<header class="hero">
    <div class="hero-bg"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <p class="hero-eyebrow">ORO ITALIANO · 18K &amp; 24K</p>
        <h1>Alba Di'Oro</h1>
        <div class="gold-divider"></div>
        <p class="hero-tagline">Donde el amanecer se viste de oro. Piezas exclusivas en oro puro 18k y 24k, elegancia atemporal para quienes no se conforman con menos.</p>
        <div class="hero-buttons">
            <a href="#coleccion" class="btn-primary">Ver Colección</a>
            <a href="{wa_link("Hola! Me gustaría una cotización gratis de Alba Di'Oro")}" class="btn-secondary">Cotización Gratis</a>
        </div>
    </div>
    <div class="scroll-cue">DESLIZA ↓</div>
</header>

<section class="trust-bar">
    <div class="trust-item"><span>✓</span> Oro 18K &amp; 24K Certificado</div>
    <div class="trust-item"><span>✓</span> Envíos Seguros</div>
    <div class="trust-item"><span>✓</span> Garantía de Autenticidad</div>
    <div class="trust-item"><span>✓</span> Pago Flexible</div>
</section>

<section id="coleccion" class="collection">
    <div class="section-header fade-in">
        <p class="section-eyebrow">Nuestra Colección</p>
        <h2>Piezas que Cuentan tu Historia</h2>
    </div>
    <div class="products-grid">
        {product_cards()}
    </div>
</section>

<section id="nosotros" class="about">
    <div class="about-content fade-in">
        <p class="section-eyebrow">Nuestra Historia</p>
        <h2>Tradición Italiana, Pasión Latina</h2>
        <p>Alba Di'Oro nace de la pasión por el oro fino italiano en sus dos presentaciones más nobles: 18k y 24k. Cada pieza es seleccionada cuidadosamente por su calidad, diseño y durabilidad — para que brilles hoy y por generaciones.</p>
        <div class="about-stats">
            <div class="stat"><span class="stat-number">100%</span><span class="stat-label">Oro Italiano</span></div>
            <div class="stat"><span class="stat-number">18K/24K</span><span class="stat-label">Únicamente</span></div>
            <div class="stat"><span class="stat-number">5★</span><span class="stat-label">Clientas Felices</span></div>
        </div>
    </div>
</section>

<section id="testimonios" class="testimonials">
    <div class="section-header fade-in">
        <p class="section-eyebrow">Lo Que Dicen</p>
        <h2>Clientas Que Confían en Nosotros</h2>
    </div>
    <div class="testimonials-grid">
        {testimonial_cards()}
    </div>
</section>

<section id="referidos" class="referral">
    <div class="referral-content fade-in">
        <p class="section-eyebrow">Programa de Referidos</p>
        <h2>Comparte y Gana</h2>
        <p>Refiere a un amigo o familiar y ambos reciben un descuento especial en su próxima compra. Entre más compartas, más ganas.</p>
        <a href="{wa_link("Hola! Quiero más información sobre el programa de referidos de Alba Di'Oro")}" class="btn-primary">Conocer el Programa</a>
    </div>
</section>

<section id="faq" class="faq">
    <div class="section-header fade-in">
        <p class="section-eyebrow">Preguntas Frecuentes</p>
        <h2>Todo lo que Necesitas Saber</h2>
    </div>
    <div class="faq-list">
        {faq_items()}
    </div>
</section>

<section id="contacto" class="contact">
    <div class="contact-content fade-in">
        <p class="section-eyebrow">Contáctanos</p>
        <h2>Agenda tu Cotización Gratuita</h2>
        <p>Escríbenos por WhatsApp y con gusto te ayudamos a encontrar la pieza perfecta en oro 18k o 24k.</p>
        <a href="{wa_link("Hola! Quisiera agendar mi cotización gratuita con Alba Di'Oro")}" class="btn-primary btn-large">Escribir por WhatsApp</a>
    </div>
</section>

<footer>
    <div class="footer-logo">Alba Di'Oro</div>
    <p>Oro Italiano 18K &amp; 24K de Elegancia Atemporal</p>
    <p style="margin-top:14px;">© 2026 Alba Di'Oro. Todos los derechos reservados.</p>
</footer>

<a href="{wa_link("Hola! Vengo de la página web de Alba Di'Oro")}" class="whatsapp-float">
    <span>💬</span>
</a>

<script>
document.querySelectorAll('.nav-links a').forEach(a => {{
    a.addEventListener('click', () => document.querySelector('.nav-links').classList.remove('open'));
}});

const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
        if (entry.isIntersecting) {{
            entry.target.classList.add('visible');
        }}
    }});
}}, {{ threshold: 0.15 }});
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
</script>

</body>
</html>'''

with open("/app/alba_dioro_demos/ALBA_DIORO_FINAL.html", "w", encoding="utf-8") as f:
    f.write(html)
print("FINAL SITE BUILT")
