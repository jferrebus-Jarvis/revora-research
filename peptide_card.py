from PIL import Image, ImageDraw, ImageFont
import os

# Canvas
W, H = 1080, 1350
img = Image.new("RGB", (W, H), color="#0A0A0F")
draw = ImageDraw.Draw(img)

# Colors
gold = "#C9A84C"
white = "#FFFFFF"
light_gray = "#AAAAAA"
dark_card = "#13131A"
accent = "#1E1E2E"

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    font_value = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    font_week = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_label = font_title
    font_value = font_title
    font_small = font_title
    font_week = font_title

def draw_rounded_rect(draw, xy, radius, fill):
    x1, y1, x2, y2 = xy
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius], fill=fill)
    draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius], fill=fill)
    draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2], fill=fill)
    draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2], fill=fill)

# Header background
draw_rounded_rect(draw, [40, 40, W-40, 160], 20, dark_card)

# Gold accent bar
draw.rectangle([40, 40, 80, 160], fill=gold)

# Title
draw.text((100, 65), "PEPTIDE PROTOCOL", font=font_title, fill=gold)
draw.text((100, 125), "Week 1 — Dosing Guide", font=font_sub, fill=light_gray)

# Week badge
draw_rounded_rect(draw, [W-200, 55, W-50, 145], 15, gold)
draw.text((W-185, 70), "WEEK", font=font_small, fill="#0A0A0F")
draw.text((W-175, 95), "01", font=font_week, fill="#0A0A0F")

# Peptide data
peptides = [
    {
        "name": "Retatrutide",
        "vial": "5mg vial",
        "dose": "60 units",
        "freq": "Once per week",
        "icon": "💉",
        "note": "Weekly injection"
    },
    {
        "name": "DSIP",
        "vial": "5mg vial",
        "dose": "10 units",
        "freq": "Daily",
        "icon": "🌙",
        "note": "Delta Sleep-Inducing Peptide"
    },
    {
        "name": "Selank",
        "vial": "5mg vial",
        "dose": "18 units",
        "freq": "Daily",
        "icon": "🧠",
        "note": "Nootropic / Anti-anxiety"
    },
    {
        "name": "Kisspeptin",
        "vial": "10mg vial",
        "dose": "5 units",
        "freq": "Daily",
        "icon": "⚡",
        "note": "Hormonal support"
    },
]

card_h = 220
card_margin = 20
start_y = 200

for i, p in enumerate(peptides):
    y = start_y + i * (card_h + card_margin)
    x1, x2 = 40, W - 40

    # Card background
    draw_rounded_rect(draw, [x1, y, x2, y + card_h], 18, dark_card)

    # Left gold accent strip
    draw_rounded_rect(draw, [x1, y, x1 + 8, y + card_h], 4, gold)

    # Number badge
    draw_rounded_rect(draw, [x1 + 20, y + 20, x1 + 65, y + 65], 10, accent)
    draw.text((x1 + 30, y + 25), str(i + 1), font=font_label, fill=gold)

    # Peptide name
    draw.text((x1 + 85, y + 22), p["name"], font=font_label, fill=white)
    draw.text((x1 + 85, y + 65), p["vial"] + "  •  " + p["note"], font=font_small, fill=light_gray)

    # Divider
    draw.line([(x1 + 20, y + 105), (x2 - 20, y + 105)], fill="#2A2A3A", width=1)

    # Dose block
    dose_x = x1 + 60
    draw.text((dose_x, y + 120), "DOSE", font=font_small, fill=light_gray)
    draw.text((dose_x, y + 148), p["dose"], font=font_label, fill=gold)

    # Frequency block
    freq_x = x1 + 320
    draw.text((freq_x, y + 120), "FREQUENCY", font=font_small, fill=light_gray)
    draw.text((freq_x, y + 148), p["freq"], font=font_label, fill=white)

    # Insulin syringe note
    draw.text((x1 + 60, y + 188), "✓ Insulin syringe (100-unit)", font=font_small, fill="#666688")

# Footer
footer_y = start_y + len(peptides) * (card_h + card_margin) + 20
draw_rounded_rect(draw, [40, footer_y, W-40, footer_y + 80], 15, dark_card)
draw.text((W//2 - 200, footer_y + 15), "All doses drawn in insulin syringe", font=font_small, fill=light_gray)
draw.text((W//2 - 160, footer_y + 42), "Store peptides refrigerated after reconstitution", font=font_small, fill="#555566")

img.save("/app/peptide_week1.png")
print("Done")
