from PIL import Image, ImageDraw, ImageFont
import os

# Canvas - higher resolution
W, H = 1080, 1500
img = Image.new("RGB", (W, H), color="#080810")
draw = ImageDraw.Draw(img)

# Colors
gold = "#C9A84C"
gold_light = "#E8C76A"
white = "#FFFFFF"
light_gray = "#B0B0C0"
dark_card = "#11111C"
accent = "#1A1A2E"
blue_accent = "#1E2A4A"
divider = "#222235"

# Fonts
try:
    bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    font_name_big = ImageFont.truetype(bold, 58)
    font_title = ImageFont.truetype(bold, 46)
    font_subtitle = ImageFont.truetype(regular, 26)
    font_label = ImageFont.truetype(bold, 30)
    font_value = ImageFont.truetype(bold, 34)
    font_value_gold = ImageFont.truetype(bold, 36)
    font_small = ImageFont.truetype(regular, 22)
    font_tiny = ImageFont.truetype(regular, 19)
    font_tag = ImageFont.truetype(bold, 20)
    font_week = ImageFont.truetype(bold, 42)
except:
    font_name_big = ImageFont.load_default()
    font_title = font_name_big
    font_subtitle = font_name_big
    font_label = font_name_big
    font_value = font_name_big
    font_value_gold = font_name_big
    font_small = font_name_big
    font_tiny = font_name_big
    font_tag = font_name_big
    font_week = font_name_big

def rrect(draw, xy, r, fill, outline=None, outline_width=0):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill, outline=outline, width=outline_width)

# ── BACKGROUND gradient effect (manual stripes)
for row in range(H):
    ratio = row / H
    r = int(8 + ratio * 5)
    g = int(8 + ratio * 5)
    b = int(16 + ratio * 12)
    draw.line([(0, row), (W, row)], fill=(r, g, b))

# ── TOP HEADER ──────────────────────────────────────────
rrect(draw, [30, 30, W-30, 210], 24, "#0E0E1E", outline=gold, outline_width=2)

# Gold left bar
rrect(draw, [30, 30, 58, 210], 12, gold)

# Name
draw.text((80, 45), "JHONNATAN FERREBUS", font=font_title, fill=gold)
draw.text((80, 105), "Peptide Protocol  —  Week 1", font=font_subtitle, fill=light_gray)
draw.text((80, 140), "Personal Dosing Reference Card", font=font_tiny, fill="#555570")

# Week badge top right
rrect(draw, [W-175, 50, W-45, 190], 16, gold)
draw.text((W-162, 58), "WEEK", font=font_tag, fill="#080810")
draw.text((W-155, 82), "01", font=font_week, fill="#080810")
draw.text((W-168, 142), "2026", font=font_tiny, fill="#333300")

# ── PEPTIDE CARDS ────────────────────────────────────────
peptides = [
    {
        "name": "Retatrutide",
        "vial": "5mg vial",
        "dose": "60 units",
        "freq": "Once per week",
        "time": "Morning",
        "time_color": "#FFD700",
        "emoji": "🌅",
        "tag": "WEEKLY",
        "tag_color": "#C9A84C",
        "tag_bg": "#2A2000",
    },
    {
        "name": "Selank",
        "vial": "5mg vial",
        "dose": "18 units",
        "freq": "Daily",
        "time": "Morning",
        "time_color": "#FFD700",
        "emoji": "🧠",
        "tag": "DAILY · AM",
        "tag_color": "#6EC6FF",
        "tag_bg": "#001A2E",
    },
    {
        "name": "MOTS-C",
        "vial": "5mg vial",
        "dose": "Daily",
        "freq": "Daily",
        "time": "Morning or Pre-Workout",
        "time_color": "#FF8C42",
        "emoji": "⚡",
        "tag": "DAILY · PRE-WO",
        "tag_color": "#FF8C42",
        "tag_bg": "#2A1000",
    },
    {
        "name": "DSIP",
        "vial": "5mg vial",
        "dose": "10 units",
        "freq": "Daily",
        "time": "Before Sleep",
        "time_color": "#9B8EFF",
        "emoji": "🌙",
        "tag": "DAILY · PM",
        "tag_color": "#9B8EFF",
        "tag_bg": "#12002A",
    },
]

card_h = 240
gap = 18
start_y = 240

for i, p in enumerate(peptides):
    y = start_y + i * (card_h + gap)
    x1, x2 = 30, W - 30

    # Card bg
    rrect(draw, [x1, y, x2, y + card_h], 20, dark_card, outline=divider, outline_width=1)

    # Left color stripe
    stripe_color = p["tag_color"]
    rrect(draw, [x1, y, x1 + 7, y + card_h], 4, stripe_color)

    # Number circle
    rrect(draw, [x1 + 18, y + 18, x1 + 66, y + 66], 24, accent)
    num_text = str(i + 1)
    draw.text((x1 + 30 if i < 9 else x1 + 22, y + 24), num_text, font=font_label, fill=gold)

    # Peptide name
    draw.text((x1 + 85, y + 18), p["name"], font=font_label, fill=white)

    # Vial info
    draw.text((x1 + 85, y + 58), p["vial"], font=font_small, fill=light_gray)

    # Tag badge
    tag_w = len(p["tag"]) * 13 + 20
    tag_x = x2 - tag_w - 20
    rrect(draw, [tag_x, y + 18, tag_x + tag_w, y + 52], 10, p["tag_bg"], outline=p["tag_color"], outline_width=1)
    draw.text((tag_x + 10, y + 25), p["tag"], font=font_tag, fill=p["tag_color"])

    # Divider
    draw.line([(x1 + 18, y + 95), (x2 - 18, y + 95)], fill=divider, width=1)

    # DOSE
    col1_x = x1 + 40
    draw.text((col1_x, y + 108), "DOSE", font=font_tiny, fill="#666680")
    draw.text((col1_x, y + 132), p["dose"], font=font_value_gold, fill=gold_light)

    # FREQUENCY
    col2_x = x1 + 260
    draw.text((col2_x, y + 108), "FREQUENCY", font=font_tiny, fill="#666680")
    draw.text((col2_x, y + 132), p["freq"], font=font_value, fill=white)

    # TIME divider
    draw.line([(x1 + 18, y + 182), (x2 - 18, y + 182)], fill=divider, width=1)

    # Time row
    draw.text((col1_x, y + 196), "⏰  " + p["time"], font=font_small, fill=p["time_color"])
    draw.text((col2_x + 80, y + 196), "✓ Insulin syringe", font=font_small, fill="#444460")

# ── FOOTER ──────────────────────────────────────────────
footer_y = start_y + len(peptides) * (card_h + gap) + 20
rrect(draw, [30, footer_y, W-30, footer_y + 100], 18, "#0E0E1E", outline=divider, outline_width=1)

draw.text((60, footer_y + 18), "💉  All doses drawn with 100-unit insulin syringe", font=font_small, fill=light_gray)
draw.text((60, footer_y + 48), "❄️   Refrigerate all peptides after reconstitution", font=font_small, fill=light_gray)
draw.text((60, footer_y + 75), "⚠️   For personal use only — follow your prescribed protocol", font=font_tiny, fill="#444455")

img.save("/app/peptide_week1_v2.png", quality=98)
print("Done")
