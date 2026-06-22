from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 2200
img = Image.new("RGB", (W, H), color="#07070F")
draw = ImageDraw.Draw(img)

gold = "#C9A84C"
gold_light = "#E8C76A"
white = "#FFFFFF"
light_gray = "#B0B0C0"
dark_card = "#10101C"
divider = "#1E1E30"
green = "#4CAF82"
purple = "#9B8EFF"
blue = "#6EC6FF"
orange = "#FF8C42"
pink = "#FF6EB4"
red_soft = "#FF6B6B"

try:
    bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    font_title = ImageFont.truetype(bold, 44)
    font_sub = ImageFont.truetype(regular, 24)
    font_label = ImageFont.truetype(bold, 28)
    font_value = ImageFont.truetype(bold, 26)
    font_small = ImageFont.truetype(regular, 21)
    font_tiny = ImageFont.truetype(regular, 18)
    font_tag = ImageFont.truetype(bold, 19)
    font_section = ImageFont.truetype(bold, 22)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_label = font_title
    font_value = font_title
    font_small = font_title
    font_tiny = font_title
    font_tag = font_title
    font_section = font_title

def rrect(draw, xy, r, fill, outline=None, w=0):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=w)

# Background gradient
for row in range(H):
    ratio = row / H
    r = int(7 + ratio * 4)
    g = int(7 + ratio * 4)
    b = int(15 + ratio * 10)
    draw.line([(0, row), (W, row)], fill=(r, g, b))

# Header
rrect(draw, [25, 25, W-25, 200], 22, "#0D0D1A", outline=gold, w=2)
rrect(draw, [25, 25, 52, 200], 10, gold)
draw.text((75, 38), "PAPA — PROTOCOLO SEMANAL", font=font_title, fill=gold)
draw.text((75, 98), "Plan completo: suplementos + péptidos", font=font_sub, fill=light_gray)
draw.text((75, 132), "Referencia personal  —  Semana 1  •  2026", font=font_tiny, fill="#444460")

# SECTION: MORNING
y = 220
rrect(draw, [25, y, W-25, y+38], 10, "#0D1A12", outline=green, w=1)
draw.text((50, y+8), "☀️  MAÑANA — Al despertar (estómago vacío)", font=font_section, fill=green)
y += 48

morning_items = [
    ("Garden of Life Probiotic", "1 cápsula con agua", "80B CFU · 15 cepas", blue, "INMUNIDAD"),
    ("Retatrutide", "60 unidades SubQ", "Solo los LUNES · 5mg vial", gold, "LUNES SOLO"),
    ("Selank", "18 unidades SubQ", "Diario · 5mg vial", blue, "DIARIO"),
    ("MOTS-C", "10 unidades SubQ", "Diario · 5mg vial", orange, "DIARIO"),
    ("Kisspeptin", "5 unidades SubQ", "Diario · 10mg vial", pink, "DIARIO"),
    ("Instant Hydration", "1 sobre en 500ml agua", "500mg sodio · 470mg potasio · 100mg magnesio", green, "ELECTROLITOS"),
]

for name, dose, note, color, tag in morning_items:
    rrect(draw, [25, y, W-25, y+88], 14, dark_card, outline=divider, w=1)
    rrect(draw, [25, y, 31, y+88], 4, color)
    draw.text((50, y+10), name, font=font_label, fill=white)
    draw.text((50, y+46), dose, font=font_value, fill=gold_light)
    draw.text((50, y+68), note, font=font_tiny, fill="#666680")
    tag_w = len(tag) * 12 + 18
    tx = W - tag_w - 30
    rrect(draw, [tx, y+14, tx+tag_w, y+42], 8, "#1A1A2E", outline=color, w=1)
    draw.text((tx+9, y+20), tag, font=font_tag, fill=color)
    y += 96

# SECTION: BREAKFAST
y += 8
rrect(draw, [25, y, W-25, y+38], 10, "#1A150A", outline=gold, w=1)
draw.text((50, y+8), "🍳  DESAYUNO — Con comida", font=font_section, fill=gold)
y += 48

breakfast_items = [
    ("Creatina", "5g (1 cucharadita)", "Mezclar en agua o jugo · Diario", orange, "FUERZA"),
    ("Metamucil Fiber Gummies", "5 gomitas (1 porción)", "5g fibra · Sin azúcar · Diario", green, "FIBRA"),
    ("Proteína (snack)", "1 barra RXBAR o Good & Gather", "12g proteína · Si no hay comida completa", blue, "PROTEÍNA"),
]

for name, dose, note, color, tag in breakfast_items:
    rrect(draw, [25, y, W-25, y+88], 14, dark_card, outline=divider, w=1)
    rrect(draw, [25, y, 31, y+88], 4, color)
    draw.text((50, y+10), name, font=font_label, fill=white)
    draw.text((50, y+46), dose, font=font_value, fill=gold_light)
    draw.text((50, y+68), note, font=font_tiny, fill="#666680")
    tag_w = len(tag) * 12 + 18
    tx = W - tag_w - 30
    rrect(draw, [tx, y+14, tx+tag_w, y+42], 8, "#1A1A2E", outline=color, w=1)
    draw.text((tx+9, y+20), tag, font=font_tag, fill=color)
    y += 96

# SECTION: NIGHT
y += 8
rrect(draw, [25, y, W-25, y+38], 10, "#12001A", outline=purple, w=1)
draw.text((50, y+8), "🌙  NOCHE — Antes de dormir", font=font_section, fill=purple)
y += 48

night_items = [
    ("DSIP", "10 unidades SubQ", "Diario · 5mg vial · Mejora el sueño", purple, "SUEÑO"),
    ("Magnesio Glicinato", "Dosis del fabricante", "Con agua · Relaja músculos y nervios", purple, "RECUPERACIÓN"),
]

for name, dose, note, color, tag in night_items:
    rrect(draw, [25, y, W-25, y+88], 14, dark_card, outline=divider, w=1)
    rrect(draw, [25, y, 31, y+88], 4, color)
    draw.text((50, y+10), name, font=font_label, fill=white)
    draw.text((50, y+46), dose, font=font_value, fill=gold_light)
    draw.text((50, y+68), note, font=font_tiny, fill="#666680")
    tag_w = len(tag) * 12 + 18
    tx = W - tag_w - 30
    rrect(draw, [tx, y+14, tx+tag_w, y+42], 8, "#1A1A2E", outline=color, w=1)
    draw.text((tx+9, y+20), tag, font=font_tag, fill=color)
    y += 96

# Footer notes
y += 12
rrect(draw, [25, y, W-25, y+160], 16, "#0D0D1A", outline=divider, w=1)
draw.text((50, y+16), "💉  Todos los péptidos con jeringa de insulina de 100 unidades", font=font_small, fill=light_gray)
draw.text((50, y+46), "❄️   Refrigerar todos los péptidos después de reconstitución", font=font_small, fill=light_gray)
draw.text((50, y+76), "💧  Tomar mínimo 2 litros de agua al día", font=font_small, fill=light_gray)
draw.text((50, y+106), "📅  Retatrutide solo los LUNES — un día fijo por semana", font=font_small, fill=gold)
draw.text((50, y+134), "⚠️   Uso personal — seguir protocolo médico prescrito", font=font_tiny, fill="#444455")

img.save("/app/dad_weekly_protocol.png", quality=98)
print("Done")
