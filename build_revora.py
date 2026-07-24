import json, re

# Raw product list from user
raw = """REVORA RESEARCH
ADAMAX 5MG $58.99
ADAMAX 10MG $74.99
ADIPOTIDE 5MG $116.99
ADIPOTIDE 10MG $141.99
AICAR 50MG $58.99
AICAR 100MG $74.99
ARA-290 10MG $58.99
ARA-290 16MG $74.99
AOD-9604 5MG $70.99
AOD-9604 10MG $112.99
ACE-031 1MG $37.99
ACTH-1-39 5MG $49.99
B7-33 10MG $141.99
BPC-157 5MG $37.99
BPC-157 10MG $45.99
BAC-WATER 3ML $8.99
BAC-WATER 10ML $10.99
CAGRILINTIDE 5MG $83.99
CAGRILINTIDE 10MG $149.99
CAGRISEMA 5MG $58.99
CJC-1295 W DAC 5MG $133.99
CJC-1295 NO DAC 2MG $41.99
CJC-1295 NO DAC 5MG $54.99
CJC-1295 NO DAC 10MG $99.99
CJC + IPA 10MG $70.99
CARDIOGEN 20MG $79.99
CORTAGEN 20MG $91.99
CRYSTAGEN 20MG $58.99
DERMORPHIN 10MG $66.99
DSIP 5MG $70.99
DULAGLUTIDE 5MG $112.99
DULAGLUTIDE 10MG $183.99
DIHEXA 5MG $45.99
DIHEXA 10MG $54.99
DEMORPHIN 2MG $37.99
EPITHALON 10MG $45.99
EPITHALON 50MG $99.99
EPO 3000IU $49.99
FOX04 2MG $91.99
FOX04 10MG $199.99
FRAG 17-23 10MG $49.99
GLUTATHIONE 600MG $33.99
GLUTATHIONE 1500MG $74.99
GHRP-2 5MG $33.99
GHRP-2 10MG $41.99
GHRP-2 15MG $45.99
GHRP-6 5MG $37.99
GHRP-6 10MG $45.99
GONADORELIN 5MG $45.99
HCG 1000IU $37.99
HCG 2000IU $45.99
HCG 5000IU $62.99
HCG 10000IU $116.99
HMG 75IU $49.99
HGH 6IU $41.99
HGH 8IU $45.99
HGH 10IU $54.99
HGH 12IU $62.99
HGH 15IU $70.99
HGH 24IU $99.99
HGH FRAG 5MG $70.99
HGH FRAG 10MG $120.99
HGH FRAG 12MG $129.99
HGH FRAG 15MG $149.99
HEXARELIN 5MG $83.99
HUMANIN 10MG $183.99
IPAMORELIN 5MG $41.99
IPAMORELIN 10MG $49.99
KISSPEPTIN 5MG $45.99
KISSPEPTIN 10MG $58.99
LIRAGLUTIDE 5MG $62.99
LIRAGLUTIDE 10MG $116.99
LIRAGLUTIDE 30MG $258.99
LL-37 5MG $74.99
MELANOTAN 1 10MG $49.99
MELANOTAN 2 10MG $49.99
TX100 100IU $74.99
CEREBROLYSIN 60MG $58.99
MGF 2MG $49.99
MOTSC 10MG $66.99
MOTSC 15MG $91.99
MOTSC 20MG $108.99
MOTSC 40MG $158.99
NAD+ 100MG $45.99
NAD+ 500MG $54.99
NAD+ 1000MG $66.99
OXYTOCIN 5MG $45.99
OXYTOCIN 10MG $54.99
PEG-MGF 2MG $58.99
PE-22-28 10MG $66.99
PNC-27 5MG $58.99
PT-141 $49.99
RETATRUTIDE 5MG $49.99
RETATRUTIDE 10MG $70.99
RETATRUTIDE 15MG $95.99
RETATRUTIDE 20MG $112.99
RETATRUTIDE 30MG $134.99
RETATRUTIDE 60MG $199.99
SEMAGLUTIDE 5MG $33.99
SEMAGLUTIDE 10MG $41.99
SEMAGLUTIDE 15MG $45.99
SEMAGLUTIDE 20MG $54.99
SEMAGLUTIDE 30MG $83.99
SERMORELIN 5MG $58.99
SERMORELIN 10MG $83.99
SNAP-8 10MG $124.99
KPV 5MG $41.99
KPV 10MG $45.99
SELANK 5MG $37.99
SELANK 10MG $45.99
SEMAX 5MG $37.99
SEMAX 10MG $45.99
SS-31 10MG $62.99
SS-31 50MG $183.99
TB-500 5MG $62.99
TB-500 10MG $108.99
TESAMORELIN 5MG $74.99
TESAMORELIN 10MG $133.99
TESAMORELIN 20MG $199.99
TIRZEPATIDE 5MG $41.99
TIRZEPATIDE 10MG $49.99
TIRZEPATIDE 15MG $58.99
TIRZEPATIDE 20MG $74.99
TIRZEPATIDE 30MG $99.99
TIRZEPATIDE 40MG $116.99
TIRZEPATIDE 50MG $139.99
TIRZEPATIDE 60MG $149.99
TIRZEPATIDE 100MG $174.99
TIRZEPATIDE 120MG $216.99
THYMALIN 10MG $54.99
THY ALPHA-1 5MG $70.99
THY ALPHA-1 10MG $108.99
TRIPTORELIN 2MG $41.99
IGF-1 LR3 100MCG $41.99
IGF-1 LR3 1MG $141.99
FST-344 1MG $174.99
GDF-8 1MG $124.99
LIPO-C 10ML $58.99
MIC 10MG $74.99
LEMON BOTTLE 10ML $58.99
VIP 5MG $62.99
VIP 10MG $99.99
MAZDUTIDE 10MG $158.99
KLOW 80MG $89.99
GLOW 70MG $74.99
100MG GHKCU $42.99
50 MG GHKCU $33.99"""

# Category mapping
categories = {
    # Growth
    "CJC-1295 W DAC": ("growth", "Growth", "#6b4e9e"),
    "CJC-1295 NO DAC": ("growth", "Growth", "#6b4e9e"),
    "CJC + IPA": ("growth", "Growth", "#6b4e9e"),
    "IPAMORELIN": ("growth", "Growth", "#6b4e9e"),
    "GHRP-2": ("growth", "Growth", "#4a5a8a"),
    "GHRP-6": ("growth", "Growth", "#4a5a8a"),
    "HGH": ("growth", "Growth", "#6b4e9e"),
    "HGH FRAG": ("growth", "Growth", "#4a5a8a"),
    "SERMORELIN": ("growth", "Growth", "#6b4e9e"),
    "TESAMORELIN": ("growth", "Growth", "#6b4e9e"),
    "HEXARELIN": ("growth", "Growth", "#4a5a8a"),
    "IGF-1 LR3": ("growth", "Growth", "#6b4e9e"),
    "MGF": ("growth", "Growth", "#4a5a8a"),
    "PEG-MGF": ("growth", "Growth", "#4a5a8a"),
    "GDF-8": ("growth", "Growth", "#6b4e9e"),
    "FST-344": ("growth", "Growth", "#6b4e9e"),
    "AOD-9604": ("growth", "Growth", "#4a5a8a"),
    "ACE-031": ("growth", "Growth", "#6b4e9e"),
    
    # Recovery
    "BPC-157": ("recovery", "Recovery", "#3f6d7a"),
    "TB-500": ("recovery", "Recovery", "#3f6d7a"),
    "ARA-290": ("recovery", "Recovery", "#3f6d7a"),
    "B7-33": ("recovery", "Recovery", "#3f6d7a"),
    "THY ALPHA-1": ("recovery", "Recovery", "#5a6b3a"),
    "THYMALIN": ("recovery", "Recovery", "#5a6b3a"),
    "LL-37": ("recovery", "Recovery", "#3f6d7a"),
    "KPV": ("recovery", "Recovery", "#5a6b3a"),
    "SS-31": ("recovery", "Recovery", "#3f6d7a"),
    "CARDIOGEN": ("recovery", "Recovery", "#3f6d7a"),
    "CORTAGEN": ("recovery", "Recovery", "#5a6b3a"),
    "CRYSTAGEN": ("recovery", "Recovery", "#5a6b3a"),
    "VIP": ("recovery", "Recovery", "#3f6d7a"),
    "FOX04": ("recovery", "Recovery", "#5a6b3a"),
    "PNC-27": ("recovery", "Recovery", "#3f6d7a"),
    
    # Metabolic / Weight
    "SEMAGLUTIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "TIRZEPATIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "RETATRUTIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "LIRAGLUTIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "DULAGLUTIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "CAGRILINTIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "CAGRISEMA": ("metabolic", "Metabolic", "#3f8f57"),
    "MAZDUTIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "AICAR": ("metabolic", "Metabolic", "#3f8f57"),
    "ADIPOTIDE": ("metabolic", "Metabolic", "#3f8f57"),
    "FRAG 17-23": ("metabolic", "Metabolic", "#3f8f57"),
    
    # Cognitive
    "SEMAX": ("cognitive", "Cognitive", "#6b4e9e"),
    "SELANK": ("cognitive", "Cognitive", "#6b4e9e"),
    "CEREBROLYSIN": ("cognitive", "Cognitive", "#4a5a8a"),
    "ADAMAX": ("cognitive", "Cognitive", "#6b4e9e"),
    "SNAP-8": ("cognitive", "Cognitive", "#4a5a8a"),
    "DIHEXA": ("cognitive", "Cognitive", "#6b4e9e"),
    "PE-22-28": ("cognitive", "Cognitive", "#4a5a8a"),
    "DERMORPHIN": ("cognitive", "Cognitive", "#4a5a8a"),
    "DEMORPHIN": ("cognitive", "Cognitive", "#4a5a8a"),
    
    # Cellular
    "GHKCU": ("cellular", "Cellular", "#5a6b3a"),
    "NAD+": ("cellular", "Cellular", "#5a6b3a"),
    "GLUTATHIONE": ("cellular", "Cellular", "#5a6b3a"),
    "MOTSC": ("cellular", "Cellular", "#5a6b3a"),
    "HUMANIN": ("cellular", "Cellular", "#5a6b3a"),
    "EPITHALON": ("cellular", "Cellular", "#6b4e9e"),
    "ACTH-1-39": ("cellular", "Cellular", "#5a6b3a"),
    "EPO": ("cellular", "Cellular", "#5a6b3a"),
    
    # Sleep
    "DSIP": ("sleep", "Sleep", "#4a5a8a"),
    
    # Hormonal
    "GONADORELIN": ("hormonal", "Hormonal", "#8b4e6b"),
    "HCG": ("hormonal", "Hormonal", "#8b4e6b"),
    "HMG": ("hormonal", "Hormonal", "#8b4e6b"),
    "TRIPTORELIN": ("hormonal", "Hormonal", "#8b4e6b"),
    "KISSPEPTIN": ("hormonal", "Hormonal", "#8b4e6b"),
    "OXYTOCIN": ("hormonal", "Hormonal", "#8b4e6b"),
    "PT-141": ("hormonal", "Hormonal", "#8b4e6b"),
    "MELANOTAN 1": ("hormonal", "Hormonal", "#8b4e6b"),
    "MELANOTAN 2": ("hormonal", "Hormonal", "#8b4e6b"),
    
    # Supplies / Cosmetic
    "BAC-WATER": ("supplies", "Supplies", "#8b9098"),
    "LIPO-C": ("supplies", "Supplies", "#8b9098"),
    "MIC": ("supplies", "Supplies", "#8b9098"),
    "LEMON BOTTLE": ("supplies", "Supplies", "#8b9098"),
    "TX100": ("supplies", "Supplies", "#8b9098"),
    "KLOW": ("supplies", "Supplies", "#8b9098"),
    "GLOW": ("supplies", "Supplies", "#8b9098"),
}

# Parse raw list
products = {}
for line in raw.strip().split('\n')[1:]:  # skip "REVORA RESEARCH" header
    line = line.strip()
    if not line:
        continue
    # Match: NAME DOSAGE $PRICE (or NAME $PRICE for PT-141)
    # Handle formats like "CJC-1295 W DAC 5MG $133.99", "NAD+ 100MG $45.99", "100MG GHKCU $42.99", "50 MG GHKCU $33.99"
    
    # Special handling for GHKCU (dosage before name)
    if 'GHKCU' in line:
        m = re.match(r'(\d+)\s*MG\s+GHKCU\s+\$(\d+\.?\d*)', line, re.I)
        if m:
            name = "GHKCU"
            dosage = f"{m.group(1)} mg"
            price = float(m.group(2))
        else:
            continue
    elif 'PT-141' in line:
        m = re.match(r'(PT-141)\s+\$(\d+\.?\d*)', line)
        if m:
            name = "PT-141"
            dosage = "10 mg"
            price = float(m.group(2))
        else:
            continue
    else:
        # Standard format: NAME DOSAGE $PRICE
        m = re.match(r'(.+?)\s+(\d+(?:\.\d+)?\s*(?:MG|ML|IU|MCG|MG))\s+\$(\d+\.?\d*)', line, re.I)
        if m:
            name = m.group(1).strip()
            dosage_raw = m.group(2).strip()
            # Normalize dosage
            dosage_raw = re.sub(r'\s+', ' ', dosage_raw)
            # Convert "5MG" to "5 mg", "100MG" to "100 mg", etc.
            dosage = re.sub(r'(?i)(\d+)\s*MG\b', r'\1 mg', dosage_raw)
            dosage = re.sub(r'(?i)(\d+)\s*ML\b', r'\1 mL', dosage)
            dosage = re.sub(r'(?i)(\d+)\s*IU\b', r'\1 IU', dosage)
            dosage = re.sub(r'(?i)(\d+)\s*MCG\b', r'\1 mcg', dosage)
            dosage = re.sub(r'\s+', ' ', dosage).strip()
            price = float(m.group(3))
        else:
            print(f"FAILED TO PARSE: {line}")
            continue
    
    if name not in products:
        products[name] = []
    products[name].append({"mg": dosage, "price": price})

# Sort variants within each product by price
for name in products:
    products[name].sort(key=lambda v: v["price"])

# Build JS array
js_lines = []
js_lines.append("var products=[")

for name, variants in products.items():
    cat_info = categories.get(name, ("supplies", "Supplies", "#8b9098"))
    g, cat_en, accent = cat_info
    cat_es = {
        "Growth": "Crecimiento", "Recovery": "Recuperación", "Metabolic": "Metabólico",
        "Cellular": "Celular", "Cognitive": "Cognitivo", "Sleep": "Sueño",
        "Hormonal": "Hormonal", "Supplies": "Suministros"
    }.get(cat_en, cat_en)
    
    # Build variants string
    if len(variants) == 1:
        v = variants[0]
        mg_str = v["mg"]
        price = v["price"]
        js_lines.append(f'  {{g:"{g}",cat:{{en:"{cat_en}",es:"{cat_es}"}},name:"{name}",mg:"{mg_str}",price:{price},state:"cart",a:"{accent}"}},')
    else:
        # Multiple variants
        var_str = ",".join([f'{{mg:"{v["mg"]}",price:{v["price"]}}}' for v in variants])
        first = variants[0]
        js_lines.append(f'  {{g:"{g}",cat:{{en:"{cat_en}",es:"{cat_es}"}},name:"{name}",variants:[{var_str}],mg:"{first["mg"]}",price:{first["price"]},state:"cart",a:"{accent}"}},')

js_lines.append("];")

js_output = '\n'.join(js_lines)

# Count products
total = len(products)
total_variants = sum(len(v) for v in products.values())
print(f"Generated {total} product cards with {total_variants} total variants")

# Write the JS products array to a file
with open('/app/revora_products.js', 'w') as f:
    f.write(js_output)

print("\nFirst 20 lines:")
for line in js_lines[:20]:
    print(line)
print(f"\n... {len(js_lines)} total lines")

