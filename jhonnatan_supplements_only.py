from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1400
img = Image.new("RGB", (W, H), color="#07070F")
draw = ImageDraw.Draw(img)

gold = "#C9A84C"
gold_light = "#E8C76A"
white = "#FFFFFF"
light_gray = "#B0B0C0"
dark_card = "#10101C"
divider = "#1E1E30"
accent = "#1A1A2E"
green = "#4CAF82"
purple = "#9B8EFF"
blue = "#6EC6FF"
orange = "#FF8C42"

try:
    bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    font_title = ImageFont.truetype(bold, 44)
    font_sub = ImageFont.truetype(regular, 24)
    font_label = ImageFont.truetype(bold, 30)
    font_value_gold = ImageFont.truetype(bold, 36)
    font_small = ImageFont.truetype(regular, 22)
    font_tiny = ImageFont.truetype(regular, 19)
    font_tag = ImageFont.truetype(bold, 20)
    font_week = ImageFont.truetype(bold, 42)
    font_section = ImageFont.truetype(bold, 22)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_label = font_title
    font_value_gold = font_title
    font_small = font_title
    font_tiny = font_title
    font_tag = font_title
    font_week = font_title
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
rrect(draw, [25, 25, W-25, 210], 22, "#0D0D1A", outline=gold, w=2)
rrect(draw, [25, 25, 52, 210], 10, gold)
draw.text((75, 38), "JHONNATAN FERREBUS", font=font_title, fill=gold)
draw.text((75, 98), "Supplement & Nutrition Stack", font=font_sub, fill=light_gray)
draw.text((75, 135), "Personal Reference Card  •  2026", font=font_tiny, fill="#555570")
rrect(draw, [W-175, 45, W-40, 195], 16, gold)
draw.text((W-162, 55), "WEEK", font=font_tag, fill="#080810")
draw.text((W-155, 80), "01", font=font_week, fill="#080810")
draw.text((W-168, 148), "2026", font=font_tiny, fill="#333300")

# SECTION: MORNING
y = 228
rrect(draw, [25, y, W-25, y+36], 10, "#001A0D", outline=green, w=1)
draw.text((50, y+7), "☀️  MORNING — Empty stomach", font=font_section, fill=green)
y += 44

morning = [
    ("Garden of Life Probiotic", "1 capsule", "80B CFU · 15 strains · Critical Care", blue, "DAILY · AM"),
    ("Instant Hydration", "1 packet in 16oz water", "500mg Na · 470mg K · 100mg Mg · Zero sugar", green, "ELECTROLYTES"),
]

for i, (name, dose, note, color, tag) in enumerate(morning):
    rrect(draw, [25, y, W-25, y+100], 16, dark_card, outline=divider, w=1)
    rrect(draw, [25, y, 32, y+100], 4, color)
    rrect(draw, [38, y+12, 82, y+60], 20, accent)
    draw.text((50, y+18), str(i+1), font=font_label, fill=gold)
    draw.text((92, y+14), name, font=font_label, fill=white)
    draw.text((92, y+52), note, font=font_tiny, fill="#666680")
    tag_w = len(tag) * 12 + 20
    tx = W - tag_w - 28
    rrect(draw, [tx, y+14, tx+tag_w, y+46], 10, "#0D0D1A", outline=color, w=1)
    draw.text((tx+10, y+22), tag, font=font_tag, fill=color)
    draw.line([(38, y+72), (W-38, y+72)], fill=divider, width=1)
    draw.text((50, y+78), dose, font=font_value_gold, fill=gold_light)
    y += 108

# SECTION: BREAKFAST
y += 6
rrect(draw, [25, y, W-25, y+36], 10, "#1A150A", outline=gold, w=1)
draw.text((50, y+7), "🍳  WITH FOOD — Breakfast", font=font_section, fill=gold)
y += 44

food = [
    ("Creatine", "5g daily", "Mix in water or shake · No cycling needed", orange, "STRENGTH"),
    ("bio.me Psyllium Husk", "3g (per serving)", "Capsules · Pure psyllium · No additives", green, "FIBER"),
    ("Protein Bar", "1 bar (RXBAR or Good & Gather)", "12g protein · Snack if no full meal", blue, "PROTEIN"),
]

for i, (name, dose, note, color, tag) in enumerate(food):
    rrect(draw, [25, y, W-25, y+100], 16, dark_card, outline=divider, w=1)
    rrect(draw, [25, y, 32, y+100], 4, color)
    rrect(draw, [38, y+12, 82, y+60], 20, accent)
    draw.text((50, y+18), str(i+1), font=font_label, fill=gold)
    draw.text((92, y+14), name, font=font_label, fill=white)
    draw.text((92, y+52), note, font=font_tiny, fill="#666680")
    tag_w = len(tag) * 12 + 20
    tx = W - tag_w - 28
    rrect(draw, [tx, y+14, tx+tag_w, y+46], 10, "#0D0D1A", outline=color, w=1)
    draw.text((tx+10, y+22), tag, font=font_tag, fill=color)
    draw.line([(38, y+72), (W-38, y+72)], fill=divider, width=1)
    draw.text((50, y+78), dose, font=font_value_gold, fill=gold_light)
    y += 108

# SECTION: NIGHT
y += 6
rrect(draw, [25, y, W-25, y+36], 10, "#12001A", outline=purple, w=1)
draw.text((50, y+7), "🌙  NIGHT — Before sleep", font=font_section, fill=purple)
y += 44

night = [
    ("Magnesium Glycinate", "Per label dose", "With water · Muscle & nerve recovery", purple, "RECOVERY"),
]

for i, (name, dose, note, color, tag) in enumerate(night):
    rrect(draw, [25, y, W-25, y+100], 16, dark_card, outline=divider, w=1)
    rrect(draw, [25, y, 32, y+100], 4, color)
    rrect(draw, [38, y+12, 82, y+60], 20, accent)
    draw.text((50, y+18), str(i+1), font=font_label, fill=gold)
    draw.text((92, y+14), name, font=font_label, fill=white)
    draw.text((92, y+52), note, font=font_tiny, fill="#666680")
    tag_w = len(tag) * 12 + 20
    tx = W - tag_w - 28
    rrect(draw, [tx, y+14, tx+tag_w, y+46], 10, "#0D0D1A", outline=color, w=1)
    draw.text((tx+10, y+22), tag, font=font_tag, fill=color)
    draw.line([(38, y+72), (W-38, y+72)], fill=divider, width=1)
    draw.text((50, y+78), dose, font=font_value_gold, fill=gold_light)
    y += 108

# Footer
y += 10
rrect(draw, [25, y, W-25, y+100], 16, "#0D0D1A", outline=divider, w=1)
draw.text((50, y+14), "💧  Drink minimum 2L of water daily", font=font_small, fill=light_gray)
draw.text((50, y+44), "🥗  Real food first — bars are snacks, not meals", font=font_small, fill=light_gray)
draw.text((50, y+74), "⚠️   For personal use only", font=font_tiny, fill="#444455")

img.save("/app/jhonnatan_supplements_only.png", quality=98)
print("Done")
