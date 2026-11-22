# Generator grafik LLN Marbella – karuzela IG (10 slajdów), grafika FB, 8 relacji.
# Użycie: python3 gen_lln.py dane.json katalog_wyjściowy
# dane.json: {"kicker","title1","title2","subtitle","fbsub","note","contact","items":[7 x {n,img(ścieżka do zdjęcia),lon,lat,area,short,typ,title(z <em>),price,stats:[[k,v]x4, ostatni "Cena"],bullets:[3]}]}
import json, math, sys, os
from pathlib import Path
D=json.load(open(sys.argv[1])); OUTD=Path(sys.argv[2]); OUTD.mkdir(parents=True,exist_ok=True)
ROOT = Path(__file__).parent
OUT = OUTD
NAVY = "#0f1a33"; NAVY2 = "#16233f"; LAND = "#1c2b4c"; ACC = "#e8a04e"; INK = "#f3efe6"; MUTED = "#9aa6bf"
APTS = D["items"]
for a in APTS: a["img"]=str(Path(a["img"]).resolve())
lons=[a["lon"] for a in APTS]; lats=[a["lat"] for a in APTS]
W0=min(lons)-0.08; E0=max(lons)+0.08
if E0-W0<0.5: c=(E0+W0)/2; W0,E0=c-0.25,c+0.25
latc=sum(lats)/len(lats); hspan=(E0-W0)*math.cos(math.radians(latc))*667/1080
S0=latc-hspan*0.62; N0=latc+hspan*0.38


coast = json.load(open(ROOT / "coast.json"))[1]  # Iberia

def proj(W, E, S, N, w):
    sx = w / (E - W); sy = sx / math.cos(math.radians((S + N) / 2))
    h = (N - S) * sy
    return (lambda lon, lat: ((lon - W) * sx, (N - lat) * sy)), h

def land_path(W, E, S, N, w):
    f, h = proj(W, E, S, N, w)
    pts = [p for p in coast if W - 0.4 < p[0] < E + 0.4]
    pts.sort(key=lambda p: -p[0])  # east -> west along coast
    xy = [f(*p) for p in pts]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in xy)
    d += f" L{xy[-1][0]:.1f},-400 L{xy[0][0]:.1f},-400 Z"
    return d, f, h

def map_svg(W, E, S, N, w, labels=True, highlight=None, pin_r=17, towns=True, label_scale=1.0):
    d, f, h = land_path(W, E, S, N, w)
    s = [f'<svg width="{w}" height="{h:.0f}" viewBox="0 0 {w} {h:.0f}" xmlns="http://www.w3.org/2000/svg">',
         f'<rect width="{w}" height="{h:.0f}" fill="{NAVY}"/>',
         f'<path d="{d}" fill="{LAND}" stroke="#2f4270" stroke-width="2"/>']
    if towns:
        for name, lon, lat, dx, dy in [("SOTOGRANDE",-5.285,36.290,14,62),("ESTEPONA",-5.146,36.427,-40,-26),("MARBELLA",-4.885,36.510,-60,-26),("FUENGIROLA",-4.625,36.540,-40,-26),("BENALMÁDENA",-4.52,36.600,-150,-26),("MÁLAGA",-4.42,36.715,-50,-26),("NERJA",-3.876,36.745,-30,-26)]:
            x, y = f(lon, lat)
            if name not in D.get("hide_towns", []) and 0 < x < w and not any(abs(f(a["lon"],a["lat"])[0]-(x+dx+70))<110 and abs(f(a["lon"],a["lat"])[1]-(y+dy))<40 for a in APTS):
                s.append(f'<circle cx="{x:.0f}" cy="{y-4:.0f}" r="3.5" fill="{MUTED}"/>')
                s.append(f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" font-family="JetBrains Mono" font-size="{17*label_scale:.0f}" letter-spacing="3" fill="{MUTED}">{name}</text>')
        x, y = f(W0+0.06, N0-0.03)
        s.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="Cormorant Garamond" font-style="italic" font-size="{30*label_scale:.0f}" fill="#6f7fa3">Sierra Bermeja</text>')
        x, y = f((W0+E0)/2, S0+0.06)
        s.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="Cormorant Garamond" font-size="{30*label_scale:.0f}" letter-spacing="14" fill="#33456d" text-anchor="middle">MORZE ŚRÓDZIEMNE</text>')
    # label offsets (dx,dy of label relative to pin) – alternate up/down to avoid collisions
    offs = {a['n']:((30,100) if a['n']%2 else (-60,-120)) for a in APTS}; offs.update({int(k):tuple(v) for k,v in D.get('offs',{}).items()})
    for a in APTS:
        x, y = f(a["lon"], a["lat"])
        on = highlight is None or highlight == a["n"]
        if labels and highlight is None:
            dx, dy = offs[a["n"]]
            lx, ly = x + dx, y + dy
            s.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{lx+4:.0f}" y2="{ly-26 if dy>0 else ly+36:.0f}" stroke="{ACC}" stroke-width="1.4" opacity=".8"/>')
            s.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-family="Jost" font-weight="500" font-size="23" fill="{INK}">{a["short"]}</text>')
            s.append(f'<text x="{lx:.0f}" y="{ly+25:.0f}" font-family="JetBrains Mono" font-size="19" fill="{ACC}">{a["price"]}</text>')
        if on:
            s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{pin_r}" fill="{ACC}" stroke="{NAVY}" stroke-width="3"/>')
            s.append(f'<text x="{x:.0f}" y="{y+pin_r*0.36:.0f}" text-anchor="middle" font-family="JetBrains Mono" font-weight="500" font-size="{pin_r*1.05:.0f}" fill="{NAVY}">{a["n"]}</text>')
        else:
            s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#4a5c86"/>')
    s.append("</svg>")
    return "\n".join(s)

FONTS = "".join(f'<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/{p}">' for p in [
    "cormorant-garamond/400.css","cormorant-garamond/500.css","cormorant-garamond/400-italic.css","cormorant-garamond/500-italic.css",
    "jost/300.css","jost/400.css","jost/500.css","jetbrains-mono/400.css","jetbrains-mono/500.css"])

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{NAVY};color:{INK};font-family:Jost;overflow:hidden;position:relative}}
.kick{{font-family:'JetBrains Mono';font-size:22px;letter-spacing:7px;color:{ACC}}}
.serif{{font-family:'Cormorant Garamond';font-weight:500;line-height:.98}}
em{{font-style:italic;color:{ACC}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:118px;border-top:1px solid #26365c;display:flex;align-items:center;
      justify-content:space-between;padding:0 70px;font-family:'JetBrains Mono';font-size:24px;letter-spacing:7px;color:{INK}}}
.foot .mid{{color:{ACC}}}
.pad{{padding:0 76px}}
"""

def foot(i, mid="PRZESUŃ →"):
    return f'<div class="foot"><span>● COSTA DEL SOL</span><span class="mid">{mid}</span><span>{i:02d} / 10</span></div>'

def page(body, w=1080, h=1350):
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS} body{{width:{w}px;height:{h}px}}</style></head><body>{body}</body></html>'

slides = []
# 1 – okładka z mapą
thumbs = "".join(f'<div style="position:relative;width:118px;height:84px;border-radius:6px;overflow:hidden;border:1px solid #33456d">'
                 f'<img src="file://{a["img"]}" style="width:100%;height:100%;object-fit:cover">'
                 f'<span style="position:absolute;left:6px;top:6px;width:26px;height:26px;border-radius:50%;background:{ACC};color:{NAVY};'
                 f'font:500 15px JetBrains Mono;display:flex;align-items:center;justify-content:center">{a["n"]}</span></div>' for a in APTS)
m = map_svg(W0, E0, S0, N0, 1080)
slides.append(f'''
<div class="pad" style="padding-top:78px">
  <div class="kick">{D["kicker"]}</div>
  <div class="serif" style="font-size:96px;margin-top:26px">{D["title1"]}<br><em>{D["title2"]}</em></div>
  <div style="font-size:31px;font-weight:300;color:#cfd6e4;margin-top:22px">{D["subtitle"]}</div>
  <div style="display:flex;gap:16px;margin-top:30px">{thumbs}</div>
</div>
<div style="position:absolute;left:0;top:565px;width:1080px;height:667px;overflow:hidden;border-top:1px solid #26365c">
  <div style="position:absolute;top:0">{m}</div>
</div>{foot(1)}''')

# 2–8 – apartamenty
for i, a in enumerate(APTS, start=2):
    mini = map_svg(W0, E0, S0+0.04, N0, 300, labels=False, highlight=a["n"], pin_r=14, towns=False)
    stats = "".join(f'<div><div style="font:400 17px JetBrains Mono;letter-spacing:4px;color:{MUTED}">{k.upper()}</div>'
                    f'<div style="font:500 34px Jost;margin-top:8px;{"color:"+ACC if k=="Cena" else ""}">{v}</div></div>' for k, v in a["stats"])
    bl = "".join(f'<li style="margin-top:12px;display:flex;gap:16px"><span style="color:{ACC}">–</span><span>{b}</span></li>' for b in a["bullets"])
    slides.append(f'''
<div style="position:absolute;left:0;top:0;width:1080px;height:640px;overflow:hidden">
  <img src="file://{a["img"]}" style="width:100%;height:100%;object-fit:cover">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,.55) 0%,rgba(15,26,51,0) 28%,rgba(15,26,51,0) 70%,{NAVY} 100%)"></div>
  <div style="position:absolute;left:60px;top:52px;background:rgba(15,26,51,.82);padding:14px 18px 12px;border-radius:6px" class="kick">{a["n"]:02d} / 07 · {a["area"].upper()}</div>
</div>
<div style="position:absolute;right:66px;top:560px;width:300px;border-radius:10px;overflow:hidden;border:1px solid #33456d;box-shadow:0 10px 30px rgba(0,0,0,.35)">{mini}</div>
<div class="pad" style="position:absolute;top:640px;left:0;width:760px">
  <div style="font:400 22px JetBrains Mono;letter-spacing:5px;color:{MUTED}">{a["typ"].upper()}</div>
  <div class="serif" style="font-size:72px;margin-top:14px">{a["title"]}</div>
</div>
<div class="pad" style="position:absolute;top:905px;left:0;right:0;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;border-top:1px solid #26365c;border-bottom:1px solid #26365c;margin:0 76px;padding:26px 0">{stats}</div>
<ul class="pad" style="position:absolute;top:1052px;left:0;list-style:none;font:300 29px Jost;color:#dde3ee">{bl}</ul>
{foot(i)}''')

# 9 – zestawienie
rows = "".join(f'<div style="display:grid;grid-template-columns:60px 1fr 210px 200px;align-items:center;padding:19px 0;border-bottom:1px solid #26365c">'
               f'<span style="width:40px;height:40px;border-radius:50%;background:{ACC};color:{NAVY};font:500 20px JetBrains Mono;display:flex;align-items:center;justify-content:center">{a["n"]}</span>'
               f'<span><span style="font:500 29px Jost">{a["short"]}</span><br><span style="font:300 23px Jost;color:{MUTED}">{a["typ"]}</span></span>'
               f'<span style="font:400 25px JetBrains Mono;color:#cfd6e4">{a["stats"][1][1]}</span>'
               f'<span style="font:500 26px JetBrains Mono;color:{ACC};text-align:right">{a["price"]}</span></div>' for a in APTS)
slides.append(f'''
<div class="pad" style="padding-top:78px">
  <div class="kick">ZESTAWIENIE</div>
  <div class="serif" style="font-size:76px;margin-top:22px">Wszystkie 7 <em>w liczbach</em></div>
  <div style="margin-top:40px;border-top:1px solid #26365c">{rows}</div>
  <div style="font:300 21px Jost;color:{MUTED};margin-top:26px;line-height:1.45">{D["note"]}</div>
</div>{foot(9)}''')

# 10 – kontakt
slides.append(f'''
<div style="position:absolute;inset:0;overflow:hidden"><img src="file://{APTS[-1]["img"]}" style="width:100%;height:100%;object-fit:cover;opacity:.32">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,{NAVY} 0%,rgba(15,26,51,.55) 45%,{NAVY} 100%)"></div></div>
<div class="pad" style="position:relative;padding-top:150px">
  <div class="kick">ZAINTERESOWANY?</div>
  <div class="serif" style="font-size:96px;margin-top:26px">Napisz numer,<br><em>który Ci się podoba</em></div>
  <div style="font:300 33px Jost;color:#dde3ee;margin-top:36px;line-height:1.45;max-width:860px">{D["contact"]}</div>
  <div style="margin-top:70px;font:400 26px JetBrains Mono;letter-spacing:3px;line-height:2.1">
    <div><span style="color:{ACC}">TEL / WHATSAPP</span>&nbsp;&nbsp;+48 882 819 306</div>
    <div><span style="color:{ACC}">WWW</span>&nbsp;&nbsp;llnmarbella.com</div>
  </div>
</div>{foot(10, "@LLNMARBELLA")}''')

for i, b in enumerate(slides, 1):
    (OUT / f"s{i:02d}.html").write_text(page(b), encoding="utf-8")

# FB – jedna grafika 1200x1500 (4:5): mapa + miniatury
fm = map_svg(W0, E0, S0, N0, 1200)
fthumbs = "".join(f'<div style="position:relative;height:140px;border-radius:8px;overflow:hidden;border:1px solid #33456d">'
                  f'<img src="file://{a["img"]}" style="width:100%;height:100%;object-fit:cover">'
                  f'<span style="position:absolute;left:8px;top:8px;width:30px;height:30px;border-radius:50%;background:{ACC};color:{NAVY};font:500 17px JetBrains Mono;display:flex;align-items:center;justify-content:center">{a["n"]}</span></div>' for a in APTS)
fb = f'''
<div style="padding:80px 84px 0">
  <div class="kick">{D["kicker"]}</div>
  <div class="serif" style="font-size:100px;margin-top:24px">{D["title1"]}<br><em>{D["title2"]}</em></div>
  <div style="font-size:29px;font-weight:300;color:#cfd6e4;margin-top:20px">{D["fbsub"]}</div>
</div>
<div style="position:absolute;left:0;top:600px;width:1200px;height:600px;overflow:hidden;border-top:1px solid #26365c;border-bottom:1px solid #26365c">
  <div style="position:absolute;top:{D.get("fb_map_top",-20)}px">{fm}</div>
</div>
<div style="position:absolute;left:84px;right:84px;top:1228px;display:grid;grid-template-columns:repeat(7,1fr);gap:12px">{fthumbs}</div>
<div style="position:absolute;left:84px;right:84px;bottom:42px;display:flex;justify-content:space-between;font:400 22px JetBrains Mono;letter-spacing:5px"><span>● COSTA DEL SOL</span><span style="color:{ACC}">LLNMARBELLA.COM</span><span>+48 882 819 306</span></div>
'''
(OUT / "fb.html").write_text(page(fb, 1200, 1500).replace("body{width:1080px;height:1350px", "body{width:1200px;height:1500px"), encoding="utf-8")
print("ok")

# ---- relacje 1080x1920 ----
def spage(b): return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS} body{{width:1080px;height:1920px}}</style></head><body>{b}</body></html>'
sfoot=lambda t:f'<div style="position:absolute;left:0;right:0;bottom:120px;text-align:center;font:400 24px JetBrains Mono;letter-spacing:7px;color:{INK}">{t}</div>'
sm=map_svg(W0, E0, S0, N0, 1080)
(OUT/"st00.html").write_text(spage(f'''<div class="pad" style="padding-top:230px"><div class="kick">{D["kicker"]}</div>
<div class="serif" style="font-size:112px;margin-top:30px">{D["title1"]}<br><em>{D["title2"]}</em></div>
<div style="font:300 36px Jost;color:#cfd6e4;margin-top:30px">{D.get("storysub",D["subtitle"])}</div></div>
<div style="position:absolute;left:0;top:930px;width:1080px;height:713px;overflow:hidden;border-top:1px solid #26365c;border-bottom:1px solid #26365c">{sm}</div>{sfoot("PRZEWIŃ → KAŻDA OFERTA OSOBNO")}'''),encoding="utf-8")
for a in APTS:
    st=''.join(f'<div><div style="font:400 19px JetBrains Mono;letter-spacing:4px;color:{MUTED}">{k.upper()}</div><div style="font:500 40px Jost;margin-top:8px">{v}</div></div>' for k,v in a['stats'] if k!='Cena')
    (OUT/f"st{a['n']:02d}.html").write_text(spage(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1080px;overflow:hidden"><img src="file://{a["img"]}" style="width:100%;height:100%;object-fit:cover">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,.6) 0%,rgba(15,26,51,0) 22%,rgba(15,26,51,0) 70%,{NAVY} 100%)"></div>
<div class="kick" style="position:absolute;left:60px;top:230px;background:rgba(15,26,51,.82);padding:14px 18px 12px;border-radius:6px">{a["n"]:02d} / 07 · {a["area"].upper()}</div></div>
<div class="pad" style="position:absolute;top:1050px;left:0;right:0"><div style="font:400 24px JetBrains Mono;letter-spacing:5px;color:{MUTED}">{a["typ"].upper()}</div>
<div class="serif" style="font-size:84px;margin-top:16px">{a["title"]}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:46px;padding:28px 0;border-top:1px solid #26365c;border-bottom:1px solid #26365c">{st}</div>
<div style="font:500 76px Jost;color:{ACC};margin-top:40px">{a["price"]}</div></div>{sfoot(f'NAPISZ „{a["n"]}” W WIADOMOŚCI')}'''),encoding="utf-8")

# ---- render do JPG ----
import asyncio
from playwright.async_api import async_playwright
from PIL import Image
async def render():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=os.environ.get("CHROME","/usr/bin/google-chrome"),args=["--allow-file-access-from-files"])
        pg=await b.new_page()
        jobs=[(f"s{i:02d}.html",f"ig-{i:02d}.jpg",1080,1350) for i in range(1,11)]+[("fb.html","fb.jpg",1200,1500)]+[(f"st{i:02d}.html",f"story-{i+1:02d}.jpg",1080,1920) for i in range(0,8)]
        for h,o,w,hh in jobs:
            await pg.set_viewport_size({"width":w,"height":hh}); await pg.goto("file://"+str((OUT/h).resolve()))
            await pg.wait_for_timeout(700); await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=str(OUT/"tmp.png")); Image.open(OUT/"tmp.png").convert("RGB").save(OUT/o,quality=88)
        await b.close()
asyncio.run(render())
im=Image.open(APTS[0]["img"]).convert("RGB"); w,h=im.size; hh=int(w*9/16); y=max(0,(h-hh)//2)
im.crop((0,y,w,y+min(hh,h))).resize((1600,900),Image.LANCZOS).save(OUT/"hero.jpg",quality=86)
print("ok", OUT)
