import re

# Read the current HTML
with open('/app/revora/demo1.html', 'r') as f:
    html = f.read()

# Read the new products JS
with open('/app/revora_products.js', 'r') as f:
    new_products_js = f.read()

# 1. Replace the products array
# Find "var products=[" ... up to the line before "var steps=["
old_products_pattern = r'var products=\[.*?\];\s*\n(?=var steps=)'
new_products_js += '\n'  # ensure newline before var steps
html = re.sub(old_products_pattern, new_products_js, html, count=1, flags=re.DOTALL)

# 2. Update GROUPS
old_groups = 'var GROUPS=["all","recovery","growth","metabolic","cellular","sleep","supplies"];'
new_groups = 'var GROUPS=["all","growth","recovery","metabolic","cognitive","cellular","hormonal","sleep","supplies"];'
html = html.replace(old_groups, new_groups)

# 3. Update English grp translations
old_grp_en = 'grp:{all:"All",recovery:"Recovery",growth:"Growth",metabolic:"Metabolic",cellular:"Cellular",sleep:"Sleep",supplies:"Supplies"},'
new_grp_en = 'grp:{all:"All",growth:"Growth",recovery:"Recovery",metabolic:"Metabolic",cognitive:"Cognitive",cellular:"Cellular",hormonal:"Hormonal",sleep:"Sleep",supplies:"Supplies"},'
html = html.replace(old_grp_en, new_grp_en)

# 4. Update Spanish grp translations
old_grp_es = 'grp:{all:"Todos",recovery:"Recuperación",growth:"Crecimiento",metabolic:"Metabólico",cellular:"Celular",sleep:"Sueño",supplies:"Suministros"},'
new_grp_es = 'grp:{all:"Todos",growth:"Crecimiento",recovery:"Recuperación",metabolic:"Metabólico",cognitive:"Cognitivo",cellular:"Celular",hormonal:"Hormonal",sleep:"Sueño",supplies:"Suministros"},'
html = html.replace(old_grp_es, new_grp_es)

# 5. Add CSS for variant selector - insert after .tile-img rules (around line 192)
# Find the CSS section and add variant selector styles
variant_css = """
  /* Variant selector */
  .var-sel{width:100%;margin-top:8px;margin-bottom:6px;position:relative}
  .var-btn{width:100%;display:flex;justify-content:space-between;align-items:center;padding:9px 14px;border-radius:6px;border:1px solid var(--card-line);background:var(--bg2);color:var(--text);font-family:var(--sans);font-size:11px;letter-spacing:.06em;cursor:pointer;transition:all .2s;text-align:left}
  .var-btn:hover{border-color:var(--violet-lt)}
  html[data-theme="light"] .var-btn:hover{border-color:var(--violet)}
  .var-btn::after{content:'▾';font-size:10px;color:var(--text-dim);margin-left:8px}
  .var-btn.open::after{content:'▴'}
  .var-opts{display:none;position:absolute;top:calc(100% + 4px);left:0;right:0;background:var(--bg);border:1px solid var(--card-line);border-radius:6px;overflow:hidden;z-index:10;box-shadow:0 8px 24px rgba(0,0,0,.2)}
  .var-opts.open{display:block}
  .var-opt{padding:9px 14px;font-size:11px;cursor:pointer;transition:background .15s;display:flex;justify-content:space-between;border-bottom:1px solid var(--card-line)}
  .var-opt:last-child{border-bottom:0}
  .var-opt:hover{background:var(--bg2)}
  .var-opt.sel{color:var(--violet-lt);font-weight:600}
  html[data-theme="light"] .var-opt.sel{color:var(--violet)}
  .var-opt .v-price{color:var(--text-dim);font-weight:400}
  .var-opt.sel .v-price{color:var(--violet-lt)}
  html[data-theme="light"] .var-opt.sel .v-price{color:var(--violet)}
"""

# Insert variant CSS after the tile hover styles
# Find the dark theme vial filter line
insert_after = 'html[data-theme="dark"] .tile:hover .vial{filter:drop-shadow(0 16px 32px rgba(107,78,158,.45))}'
html = html.replace(insert_after, insert_after + '\n' + variant_css)

# 6. Replace cardHTML function
old_cardhtml = '''function cardHTML(p,idx){var t=T[LANG];
  var media=p.photo?'<img src="'+PHOTO+'" alt="Revora '+p.name+'">':vial(p.a);
  var blur=(p.state==="oos"||p.state==="soon")?" blur":"";
  var flag="";
  if(p.state==="sale")flag='<div class="flag sale">'+t.st.sale+'</div>';
  else if(p.state==="oos")flag='<div class="flag oos">'+t.st.oos+'</div>';
  else if(p.state==="soon")flag='<div class="flag soon">'+t.st.soonf+'</div>';
  var btn;
  if(p.state==="cart"||p.state==="sale")btn='<button class="act cart" onclick="addToCart('+idx+',this)">'+t.st.cart+'</button>';
  else if(p.state==="opts")btn='<button class="act opts" onclick="addToCart('+idx+',this)">'+t.st.opts+'</button>';
  else btn='<button class="act notify">'+t.st.notify+'</button>';
  return '<article class="card rv in"><div class="tile'+blur+'">'+flag
    +'<div class="tile-img">'+media+'</div>'+btn+'</div>'
    +'<div class="card-meta"><div class="cat">'+p.cat[LANG]+'</div>'
    +'<h3>'+p.name+'</h3><div class="mg">'+p.mg+'</div>'
    +'<div class="price">'+priceHTML(p)+'</div></div></article>';}'''

new_cardhtml = '''function cardHTML(p,idx){var t=T[LANG];
  var media=vial(p.a);
  var blur=(p.state==="oos"||p.state==="soon")?" blur":"";
  var flag="";
  if(p.state==="sale")flag='<div class="flag sale">'+t.st.sale+'</div>';
  else if(p.state==="oos")flag='<div class="flag oos">'+t.st.oos+'</div>';
  else if(p.state==="soon")flag='<div class="flag soon">'+t.st.soonf+'</div>';
  var btn;
  if(p.state==="cart"||p.state==="sale")btn='<button class="act cart" onclick="addToCart('+idx+',this)">'+t.st.cart+'</button>';
  else if(p.state==="opts")btn='<button class="act opts" onclick="addToCart('+idx+',this)">'+t.st.opts+'</button>';
  else btn='<button class="act notify">'+t.st.notify+'</button>';
  var varHTML='';
  if(p.variants&&p.variants.length>1){
    varHTML='<div class="var-sel"><button class="var-btn" onclick="toggleVars(this,'+idx+')">'+p.mg+'</button><div class="var-opts">';
    p.variants.forEach(function(v){var sel=v.mg===p.mg?' sel':'';
      varHTML+='<div class="var-opt'+sel+'" onclick="selVariant('+idx+',\\''+v.mg+'\\','+v.price+',this)"><span>'+v.mg+'</span><span class="v-price">'+money(v.price)+'</span></div>';});
    varHTML+='</div></div>';
  }
  return '<article class="card rv in"><div class="tile'+blur+'">'+flag
    +'<div class="tile-img">'+media+'</div>'+btn+'</div>'
    +'<div class="card-meta"><div class="cat">'+p.cat[LANG]+'</div>'
    +'<h3>'+p.name+'</h3>'+varHTML
    +'<div class="price">'+priceHTML(p)+'</div></div></article>';}'''

html = html.replace(old_cardhtml, new_cardhtml)

# 7. Add variant selector functions before renderChips
new_functions = '''function toggleVars(btn,idx){var opts=btn.nextElementSibling;var isOpen=opts.classList.contains('open');document.querySelectorAll('.var-opts.open').forEach(function(o){o.classList.remove('open');document.querySelectorAll('.var-btn.open').forEach(function(b){b.classList.remove('open');});});if(!isOpen){btn.classList.add('open');opts.classList.add('open');}}
function selVariant(idx,mg,price,el){var p=products[idx];p.mg=mg;p.price=price;var card=el.closest('.card-meta');var btn=card.querySelector('.var-btn');btn.textContent=mg;card.querySelector('.var-btn').classList.remove('open');el.closest('.var-opts').classList.remove('open');card.querySelectorAll('.var-opt').forEach(function(o){o.classList.remove('sel');});el.classList.add('sel');var priceEl=card.querySelector('.price');if(priceEl){priceEl.innerHTML=money(price);}renderCart();}
'''
html = html.replace('function renderChips(){', new_functions + 'function renderChips(){')

# 8. Update priceHTML to handle variant products (always show money)
old_price = '''function priceHTML(p){var t=T[LANG];
  if(p.range) return '<span class="range">'+money(p.range[0])+' – '+money(p.range[1])+'</span>';
  if(p.state==="soon") return '<span class="range" style="color:var(--text-soft)">'+t.st.soonf+'</span>';
  if(p.old) return '<span class="old">'+money(p.old)+'</span>'+money(p.price);
  return money(p.price);}'''

new_price = '''function priceHTML(p){var t=T[LANG];
  if(p.range) return '<span class="range">'+money(p.range[0])+' – '+money(p.range[1])+'</span>';
  if(p.state==="soon") return '<span class="range" style="color:var(--text-soft)">'+t.st.soonf+'</span>';
  if(p.old) return '<span class="old">'+money(p.old)+'</span>'+money(p.price);
  if(p.variants&&p.variants.length>1) return '<span class="from">From </span>'+money(p.variants[0].price);
  return money(p.price);}'''

html = html.replace(old_price, new_price)

# Write the updated HTML
with open('/app/revora/demo1.html', 'w') as f:
    f.write(html)

print("HTML updated successfully!")
print(f"File size: {len(html)} bytes")

# Verify key replacements
checks = [
    ("cognitive" in html, "cognitive category added"),
    ("hormonal" in html, "hormonal category added"),
    ("var-sel" in html, "variant selector CSS added"),
    ("toggleVars" in html, "toggleVars function added"),
    ("selVariant" in html, "selVariant function added"),
    ("variants:" in html, "variant data structure present"),
    ("From " in html, "From price label added"),
]
for ok, desc in checks:
    print(f"  {'✓' if ok else '✗'} {desc}")

