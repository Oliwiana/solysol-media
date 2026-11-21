# Reels LLN Marbella (1080×1920, ok. 25 s) z danych posta „7 …” (ten sam dane.json co gen_lln.py).
# Użycie: python3 mkreel_lln.py dane.json katalog_wyjściowy  → reel.mp4, reel-cover.jpg
# Opcjonalnie w dane.json: "reel_imgs": {"1":"/ścieżka/inne.jpg",...} – inne zdjęcie danej oferty do filmu; "reel_hook": "tekst na pierwszy kadr".
import json, sys, os, subprocess, asyncio, html
from pathlib import Path
D = json.load(open(sys.argv[1])); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
TMP = OUT / "reel_tmp"; TMP.mkdir(exist_ok=True)
NAVY = "#0f1a33"; ACC = "#e8a04e"; INK = "#f3efe6"; MUTED = "#9aa6bf"
ITEMS = D["items"]; RI = {int(k): v for k, v in D.get("reel_imgs", {}).items()}
FPS = 30; DUR = 2.6; XF = 0.4
FONTS = "".join(f'<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/{p}">' for p in [
    "cormorant-garamond/500.css", "cormorant-garamond/500-italic.css", "jost/300.css", "jost/400.css", "jost/500.css", "jetbrains-mono/400.css", "jetbrains-mono/500.css"])
CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1920px;background:transparent;color:{INK};font-family:Jost;overflow:hidden;position:relative}}
.mono{{font-family:'JetBrains Mono'}} .serif{{font-family:'Cormorant Garamond';font-weight:500;line-height:1}} em{{font-style:italic;color:{ACC}}}
.top{{position:absolute;left:60px;right:60px;top:120px;display:flex;justify-content:space-between;font:400 26px 'JetBrains Mono';letter-spacing:6px;text-shadow:0 2px 10px rgba(0,0,0,.7)}}"""
page = lambda b, bg="transparent": f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS} body{{background:{bg}}}</style></head><body>{b}</body></html>'
grad = f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,.55) 0%,rgba(15,26,51,0) 16%,rgba(15,26,51,0) 38%,rgba(15,26,51,.88) 62%,{NAVY} 82%)"></div>'

pages = {}
pages["o00"] = page(grad + f'''<div class="top"><span>LLN MARBELLA</span><span>COSTA DEL SOL</span></div>
<div style="position:absolute;left:70px;right:70px;bottom:330px;text-align:center">
<div class="mono" style="font-size:28px;letter-spacing:8px;color:{ACC}">{D["kicker"]}</div>
<div class="serif" style="font-size:132px;margin-top:30px">{D["title1"]}<br><em>{D["title2"]}</em></div>
<div style="font:300 40px Jost;color:#dfe4ee;margin-top:30px">{D.get("reel_hook", D.get("storysub", ""))}</div></div>''')
for a in ITEMS:
    st = " · ".join(f"{k.lower()} {v}" for k, v in a["stats"] if k != "Cena")
    pages[f"o{a['n']:02d}"] = page(grad + f'''<div class="top"><span>{a["n"]:02d} / {len(ITEMS):02d}</span><span>{html.escape(a["area"].upper())}</span></div>
<div style="position:absolute;left:70px;right:70px;bottom:300px">
<div class="mono" style="font-size:26px;letter-spacing:6px;color:{MUTED}">{a["typ"].upper()}</div>
<div class="serif" style="font-size:96px;margin-top:20px">{a["title"]}</div>
<div style="font:400 36px Jost;color:#dfe4ee;margin-top:26px">{st}</div>
<div style="font:500 92px Jost;color:{ACC};margin-top:30px">{a["price"]}</div></div>''')
pages["end"] = page(f'''<div style="position:absolute;inset:0;background:radial-gradient(circle at 80% 10%,#1c2b4c 0,{NAVY} 60%)"></div>
<div style="position:absolute;left:90px;right:90px;top:560px;text-align:center">
<div class="mono" style="font-size:28px;letter-spacing:8px;color:{ACC}">LLN MARBELLA · OD 2010</div>
<div class="serif" style="font-size:118px;margin-top:34px">Który numer<br><em>Ci się podoba?</em></div>
<div style="font:300 42px/1.45 Jost;color:#dfe4ee;margin-top:40px">Napisz numer w wiadomości –<br>wyślemy pełne opisy.</div>
<div style="margin-top:80px;font:400 36px 'JetBrains Mono';line-height:1.8">+48 882 819 306<br><span style="color:{ACC}">llnmarbella.com</span></div></div>''', NAVY)

async def shots():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"), args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for k, h in pages.items():
            f = TMP / f"{k}.html"; f.write_text(h, encoding="utf-8")
            await pg.goto("file://" + str(f)); await pg.wait_for_timeout(500); await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=str(TMP / f"{k}.png"), omit_background=True)
        await b.close()
asyncio.run(shots())

def seg(img, ov, out, zoom_in=True):
    n = int(DUR * FPS)
    z = f"'min(1+0.10*on/{n},1.10)'" if zoom_in else f"'max(1.10-0.10*on/{n},1.0)'"
    vf = (f"[0:v]scale=1188:2112:force_original_aspect_ratio=increase,crop=1188:2112,"
          f"zoompan=z={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS}[bg];[bg][1:v]overlay=0:0,format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", img, "-loop", "1", "-t", str(DUR), "-i", ov,
                    "-filter_complex", vf, "-t", str(DUR), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out], check=True)

parts = []
first = RI.get(ITEMS[0]["n"], ITEMS[0]["img"])
seg(first, str(TMP / "o00.png"), str(TMP / "p00.mp4")); parts.append(TMP / "p00.mp4")
for i, a in enumerate(ITEMS):
    seg(RI.get(a["n"], a["img"]), str(TMP / f"o{a['n']:02d}.png"), str(TMP / f"p{a['n']:02d}.mp4"), i % 2 == 0); parts.append(TMP / f"p{a['n']:02d}.mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", "3", "-i", str(TMP / "end.png"), "-vf", "format=yuv420p", "-r", str(FPS),
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(TMP / "pend.mp4")], check=True); parts.append(TMP / "pend.mp4")
# łączenie z przenikaniem
ins = []; [ins.extend(["-i", str(p)]) for p in parts]
durs = [DUR] * (len(parts) - 1) + [3.0]; fc = []; last = "[0:v]"; off = 0
for i in range(1, len(parts)):
    off += durs[i - 1] - XF; o = f"[x{i}]"
    fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={off:.2f}{o}"); last = o
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, "-f", "lavfi", "-t", str(off + 3.0), "-i", "anullsrc=r=44100:cl=stereo",
                "-filter_complex", ";".join(fc), "-map", last, "-map", f"{len(parts)}:a", "-shortest", "-c:v", "libx264", "-preset", "veryfast",
                "-crf", "24", "-maxrate", "1300k", "-bufsize", "2600k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(OUT / "reel.mp4")], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "1.2", "-i", str(OUT / "reel.mp4"), "-frames:v", "1", "-q:v", "3", str(OUT / "reel-cover.jpg")], check=True)
print("ok", OUT / "reel.mp4", f"{off + 3.0:.1f}s")
