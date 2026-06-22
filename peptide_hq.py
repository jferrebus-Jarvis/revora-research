from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1560
img = Image.new("RGB", (W, H), color=(8, 8, 16))
draw = ImageDraw.Draw(img)

# Colors
GOLD = (201, 168, 76)
GOLD_L = (232, 199, 106)
WHITE = (255, 255, 255)
GRAY = (176, 176, 192)
CARD_BG = (17, 17, 28)
ACCENT_BG = (26, 26, 46)
DIVIDER = (30, 30, 53)
DIM = (68, 68, 96)

def px(path, size): return ImageFont.truetype(path, size)

F = "/app/fonts/"
f_black  = F+"Inter-Black.ttf"
f_xbold  = F+"Inter-ExtraBold.ttf"
f_bold   = F+"Inter-Bold.ttf"
f_semi   = F+"Inter-SemiBold.ttf"
f_med    = F+"Inter-Medium.ttf"
f_reg    = F+"Inter-Regular.ttf"

# Gradient background
for row in range(H):
    t = row / H
    r = int(8 + t*6)
    g = int(8 + t*4)
    b = int(16 + t*14)
    draw.line([(0, row), (W, row)], fill=(r, g, b))

def rrect(xy, r, fill, outline=None, ow=0):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=ow)

def text_c(txt, x, y, font, fill, center_in=None):
    """Draw text, optionally centered in a width"""
    if center_in:
        bbox = draw.textbbox((0,0), txt, font=font)
        tw = bbox[2] - bbox[0]
        x = x + (center_in - tw) // 2
    draw.text((x, y), txt, font=font, fill=fill)

# ── HEADER ──────────────────────────────────────────────
rrect([30, 30, W-30, 215], 24, CARD_BG, outline=GOLD, ow=2)
# Gold left bar
rrect([30, 30, 56, 215], 12, GOLD)

# Name
draw.text((76, 50), "JHONNATAN FERREBUS", font=px(f_black, 50), fill=GOLD)
draw.text((76, 115), "Protocolo de Péptidos  —  Semana 1", font=px(f_reg, 24), fill=GRAY)
draw.text((76, 152), "Tarjeta Personal de Dosis", font=px(f_reg, 17), fill=(70, 70, 96))

# Week badge
rrect([W-185, 48, W-44, 198], 18, GOLD)
draw.text((W-167, 58), "SEMANA", font=px(f_bold, 15), fill=(8,8,16))
draw.text((W-163, 80), "01", font=px(f_black, 58), fill=(8,8,16))
draw.text((W-170, 152), "2026", font=px(f_med, 14), fill=(40,30,0))

# ── CARDS ────────────────────────────────────────────────
peptides = [
    dict(name="Retatrutide", vial="Frasco 5mg",  dose="60 unidades",            freq="Una vez / semana",  time="Por la mañana",            t_col=(255,215,0),   tag="SEMANAL",         tag_col=(201,168,76),  tag_bg=(42,32,0)),
    dict(name="Selank",      vial="Frasco 5mg",  dose="18 unidades",            freq="Diario",           time="Por la mañana",            t_col=(255,215,0),   tag="DIARIO · AM",     tag_col=(110,198,255), tag_bg=(0,26,46)),
    dict(name="MOTS-C",      vial="Frasco 5mg",  dose="10 unidades  (1mg/día)", freq="Diario",           time="Mañana o Pre-Entrenamiento",t_col=(255,140,66),  tag="DIARIO · PRE-ENT",tag_col=(255,140,66),  tag_bg=(42,16,0)),
    dict(name="DSIP",        vial="Frasco 5mg",  dose="10 unidades",            freq="Diario",           time="Antes de dormir",          t_col=(155,142,255), tag="DIARIO · PM",     tag_col=(155,142,255), tag_bg=(18,0,42)),
]

card_h = 248
gap = 16
sy = 238

for i, p in enumerate(peptides):
    y = sy + i * (card_h + gap)
    x1, x2 = 30, W-30

    rrect([x1, y, x2, y+card_h], 22, CARD_BG, outline=DIVIDER, ow=1)
    # color stripe
    rrect([x1, y, x1+6, y+card_h], 4, p["tag_col"])

    # number badge
    rrect([x1+18, y+18, x1+70, y+70], 16, ACCENT_BG)
    draw.text((x1+28, y+22), str(i+1), font=px(f_bold, 32), fill=GOLD)

    # name + vial
    draw.text((x1+88, y+18), p["name"], font=px(f_bold, 30), fill=WHITE)
    draw.text((x1+88, y+60), p["vial"], font=px(f_reg, 18), fill=(112,112,160))

    # tag badge
    tag_font = px(f_bold, 16)
    tag_bbox = draw.textbbox((0,0), p["tag"], font=tag_font)
    tw = tag_bbox[2] - tag_bbox[0]
    tx = x2 - tw - 46
    rrect([tx, y+18, tx+tw+28, y+54], 10, p["tag_bg"], outline=p["tag_col"], ow=1)
    draw.text((tx+14, y+25), p["tag"], font=tag_font, fill=p["tag_col"])

    # divider
    draw.line([(x1+18, y+96), (x2-18, y+96)], fill=DIVIDER, width=1)

    # DOSE
    col1 = x1+44
    draw.text((col1, y+108), "DOSIS", font=px(f_semi, 13), fill=DIM)
    draw.text((col1, y+130), p["dose"], font=px(f_xbold, 28), fill=GOLD_L)

    # FRECUENCIA
    col2 = x1+380
    draw.text((col2, y+108), "FRECUENCIA", font=px(f_semi, 13), fill=DIM)
    draw.text((col2, y+130), p["freq"], font=px(f_bold, 26), fill=WHITE)

    # bottom row
    draw.line([(x1+18, y+188), (x2-18, y+188)], fill=DIVIDER, width=1)
    draw.text((col1, y+202), "⏰  " + p["time"], font=px(f_med, 17), fill=p["t_col"])
    draw.text((col2+20, y+204), "✓ Jeringa de insulina", font=px(f_reg, 15), fill=(56,56,80))

# ── FOOTER ───────────────────────────────────────────────
fy = sy + len(peptides)*(card_h+gap) + 10
rrect([30, fy, W-30, fy+108], 18, CARD_BG, outline=DIVIDER, ow=1)
draw.text((58, fy+16), "💉  Todas las dosis: jeringa de insulina 100 unidades", font=px(f_reg, 17), fill=GRAY)
draw.text((58, fy+48), "❄️   Refrigerar todos los péptidos tras reconstituir", font=px(f_reg, 17), fill=GRAY)
draw.text((58, fy+78), "⚠️   Uso personal — seguir el protocolo indicado", font=px(f_reg, 15), fill=(64,64,80))

img.save("/app/peptide_hq.png", quality=98, dpi=(300,300))
print("Done")
