# Generator grafik LLN Marbella – ciekawostki / historia / „Co się dzieje na Costa del Sol”.
# Użycie: python3 gen_lln_fakty.py dane.json katalog_wyjściowy
# dane.json: {"tag":"MARBELLA · HISTORIA","kicker":"8 FAKTÓW · COSTA DEL SOL","title1":"Marbella,","title2":"jakiej nie znasz",
#   "subtitle":"…","cover":{"photo":"ścieżka","pos":"50% 50%","credit":"Fot. … / Wikimedia Commons, CC BY-SA 4.0"},
#   "facts":[{"label":"1906 · MARBELLA","title":"…","text":"2–4 zdania","photo","pos","credit"}] (4–8 sztuk),
#   "end":{"title1":"Chcesz tu","title2":"zamieszkać?","text":"…"}}
# Wynik: ig-01…ig-NN.jpg (okładka + fakty + zakończenie, maks. 10), fb.jpg 1200×1500, story-01…(okładka + fakty, maks. 8), hero.jpg
import json, sys, os, html, asyncio
from pathlib import Path
D = json.load(open(sys.argv[1])); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
NAVY = "#0f1a33"; ACC = "#e8a04e"; INK = "#f3efe6"; MUTED = "#9aa6bf"
FACTS = D["facts"][:8]; N = len(FACTS) + 2
P = lambda p: "file://" + str(Path(p).resolve())

FONTS = "".join(f'<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/{p}">' for p in [
    "cormorant-garamond/400.css", "cormorant-garamond/500.css", "cormorant-garamond/400-italic.css", "cormorant-garamond/500-italic.css",
    "jost/300.css", "jost/400.css", "jost/500.css", "jetbrains-mono/400.css", "jetbrains-mono/500.css"])
CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:{NAVY};color:{INK};font-family:Jost;overflow:hidden;position:relative}}
.mono{{font-family:'JetBrains Mono'}} .serif{{font-family:'Cormorant Garamond';font-weight:500;line-height:1}}
em{{font-style:italic;color:{ACC}}}
.ph{{position:absolute;left:0;top:0;width:100%;object-fit:cover}}
.top{{position:absolute;left:44px;right:44px;top:40px;display:flex;justify-content:space-between;font:400 21px 'JetBrains Mono';letter-spacing:5px;color:{INK};text-shadow:0 1px 8px rgba(0,0,0,.6)}}
.cr{{font:300 17px Jost;color:rgba(243,239,230,.62)}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:104px;border-top:1px solid #26365c;display:flex;align-items:center;justify-content:space-between;
      padding:0 64px;font:400 22px 'JetBrains Mono';letter-spacing:7px;color:{INK};background:{NAVY}}}
.foot .mid{{color:{ACC}}}"""

import re as _re
def DASH(b): return _re.sub(r'–(?![^<]*>)', '<span style="font-family:\'Cormorant Garamond\'">–</span>', b)
def page(body, w, h):
    body = DASH(body)
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS} body{{width:{w}px;height:{h}px}}</style></head><body>{body}</body></html>'

def foot(i, mid="PRZESUŃ →"):
    return f'<div class="foot"><span><span style="color:{ACC}">●</span> COSTA DEL SOL</span><span class="mid">{mid}</span><span>{i:02d} / {N:02d}</span></div>'

def grad(h, start):
    return (f'<div style="position:absolute;left:0;top:0;width:100%;height:{h}px;background:linear-gradient(180deg,rgba(15,26,51,.55) 0%,'
            f'rgba(15,26,51,0) 14%,rgba(15,26,51,0) {start}%,{NAVY} 100%)"></div>')

def cover(w, h, story=False):
    c = D["cover"]; ph = int(h * (0.70 if story else 0.66))
    tsize = 108 if not story else 120
    return f'''<img class="ph" src="{P(c["photo"])}" style="height:{ph}px;object-position:{c.get("pos","50% 50%")}">{grad(ph, 45)}
<div class="top"><span>{D["tag"]}</span><span>COSTA DEL SOL</span></div>
<div style="position:absolute;left:60px;right:60px;bottom:{(150 if not story else 230)}px;text-align:center">
 <div class="mono" style="font-size:23px;letter-spacing:7px;color:{ACC}">{D["kicker"]}</div>
 <div class="serif" style="font-size:{tsize}px;margin-top:22px">{D["title1"]}<br><em>{D["title2"]}</em></div>
 <div style="font:300 34px Jost;color:#cfd6e4;margin-top:22px">{D["subtitle"]}</div>
 <div style="font:300 22px Jost;color:{MUTED};margin-top:26px">@llnmarbella · Przesuń →</div>
 <div class="cr" style="margin-top:8px">{c.get("credit","")}</div>
</div>'''

def fact(i, f, w, h, story=False):
    ph = int(h * (0.50 if not story else 0.60))
    return f'''<img class="ph" src="{P(f["photo"])}" style="height:{ph}px;object-position:{f.get("pos","50% 50%")}">{grad(ph, 62)}
<div class="top"><span>{D["tag"]}</span><span>{i:02d} / {len(FACTS):02d}</span></div>
<div class="cr" style="position:absolute;right:44px;top:{ph-34}px;text-align:right;max-width:70%">{f.get("credit","")}</div>
<div style="position:absolute;left:72px;right:72px;top:{ph+18}px">
 <div style="display:flex;align-items:baseline;gap:26px"><span class="mono" style="font-size:64px;color:{ACC};font-weight:500">{i:02d}</span>
 <span class="mono" style="font-size:22px;letter-spacing:6px;color:{MUTED}">{f["label"]}</span></div>
 <div class="serif" style="font-size:{70 if not story else 78}px;margin-top:18px">{f["title"]}</div>
 <div style="font:300 {31 if not story else 35}px/1.42 Jost;color:#dfe4ee;margin-top:24px">{f["text"]}</div>
</div>'''

E = D.get("end", {})
end = f'''<div style="position:absolute;inset:0;background:radial-gradient(circle at 80% 10%,#1c2b4c 0,{NAVY} 60%)"></div>
<div class="top"><span>{D["tag"]}</span><span>LLN MARBELLA</span></div>
<div style="position:absolute;left:80px;right:80px;top:300px">
 <div class="mono" style="font-size:23px;letter-spacing:7px;color:{ACC}">COSTA DEL SOL · OD 2010</div>
 <div class="serif" style="font-size:104px;margin-top:26px">{E.get("title1","Chcesz tu")}<br><em>{E.get("title2","zamieszkać?")}</em></div>
 <div style="font:300 34px/1.45 Jost;color:#dfe4ee;margin-top:34px">{E.get("text","Pomagamy Polakom kupić dom i apartament na Costa del Sol – od wyboru oferty po notariusza. Napisz do nas w wiadomości.")}</div>
 <div style="margin-top:60px;padding-top:34px;border-top:1px solid #26365c;font:400 30px 'JetBrains Mono';letter-spacing:2px;line-height:1.8">
  +48 882 819 306 · WhatsApp<br><span style="color:{ACC}">llnmarbella.com</span></div>
</div>'''

jobs = []
def add(name, body, w, h, out):
    (OUT / name).write_text(page(body, w, h), encoding="utf-8"); jobs.append((name, out, w, h))

add("s01.html", cover(1080, 1350) + foot(1), 1080, 1350, "ig-01.jpg")
for i, f in enumerate(FACTS, 1):
    add(f"s{i+1:02d}.html", fact(i, f, 1080, 1350) + foot(i + 1), 1080, 1350, f"ig-{i+1:02d}.jpg")
add(f"s{N:02d}.html", end + foot(N, "NAPISZ DO NAS"), 1080, 1350, f"ig-{N:02d}.jpg")
add("fb.html", cover(1200, 1500).replace("bottom:150px", "bottom:110px"), 1200, 1500, "fb.jpg")
sf = lambda t: f'<div style="position:absolute;left:0;right:0;bottom:130px;text-align:center;font:400 22px JetBrains Mono;letter-spacing:6px;color:{ACC}">{t}</div>'
add("st01.html", cover(1080, 1920, True) + sf("@LLNMARBELLA"), 1080, 1920, "story-01.jpg")
for i, f in enumerate(FACTS[:7], 1):
    add(f"st{i+1:02d}.html", fact(i, f, 1080, 1920, True) + sf("WIĘCEJ W POŚCIE NA PROFILU"), 1080, 1920, f"story-{i+1:02d}.jpg")

from playwright.async_api import async_playwright
from PIL import Image
async def render():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"), args=["--allow-file-access-from-files"])
        pg = await b.new_page()
        for h, o, w, hh in jobs:
            await pg.set_viewport_size({"width": w, "height": hh}); await pg.goto("file://" + str((OUT / h).resolve()))
            await pg.wait_for_timeout(600); await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=str(OUT / "tmp.png")); Image.open(OUT / "tmp.png").convert("RGB").save(OUT / o, quality=88)
        await b.close()
asyncio.run(render())
im = Image.open(D["cover"]["photo"]).convert("RGB"); w, h = im.size; hh = int(w * 9 / 16); y = max(0, (h - hh) // 2)
im.crop((0, y, w, y + min(hh, h))).resize((1600, 900), Image.LANCZOS).save(OUT / "hero.jpg", quality=86)
print("ok", OUT, "slajdy:", N)
