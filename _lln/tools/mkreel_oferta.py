# Film jednej oferty LLN Marbella (1080×1920, ok. 25 s) – środkowa kolumna siatki IG.
# Użycie: python3 mkreel_oferta.py oferta.json katalog_wyjściowy → reel.mp4, reel-cover.jpg
# oferta.json: {"kicker":"LOS MONTEROS · MARBELLA", "title1":"Willa", "title2":"w pierwszej linii", "hook":"6 sypialni · 1229 m² · plaża za ogrodem",
#   "price":"11,95 mln €" (albo "" – oferta bez ceny), "cover":"/ścieżka/zdjęcie.jpg", "cover_pos":"50% 50%",
#   "shots":[{"img":"/ścieżka.jpg","label":"TARAS NA DACHU","title":"Morze <em>z leżaka</em>"} ...] (6–8 ujęć),
#   "end_title1":"Chcesz ją", "end_title2":"zobaczyć?", "end_text":"Umówimy prezentację na miejscu albo wideo po polsku."}
# Okładka: zdjęcie u góry, granatowy pas z kursywą – w środkowym kadrze 3:4 (to widać w siatce profilu).
import json, sys, os, subprocess, asyncio
from pathlib import Path
D = json.load(open(sys.argv[1])); OUT = Path(sys.argv[2]).resolve(); OUT.mkdir(parents=True, exist_ok=True)
TMP = OUT / "of_tmp"; TMP.mkdir(exist_ok=True)
NAVY = "#0f1a33"; ACC = "#e8a04e"; INK = "#f3efe6"; MUTED = "#9aa6bf"
FPS = 30; DUR = 3.0; XF = 0.4
FONTS = "".join(f'<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/{p}">' for p in [
    "cormorant-garamond/500.css", "cormorant-garamond/500-italic.css", "jost/300.css", "jost/400.css", "jost/500.css", "jetbrains-mono/400.css"])
CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1920px;color:{INK};font-family:Jost;overflow:hidden;position:relative}}
.mono{{font-family:'JetBrains Mono'}} .serif{{font-family:'Cormorant Garamond';font-weight:500;line-height:1.02}} em{{font-style:italic;color:{ACC}}}
.top{{position:absolute;left:60px;right:60px;top:300px;display:flex;justify-content:space-between;font:400 26px 'JetBrains Mono';letter-spacing:6px;text-shadow:0 2px 10px rgba(0,0,0,.7)}}"""
page = lambda b, bg="transparent": f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS} body{{background:{bg}}}</style></head><body>{b}</body></html>'
grad = f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,.5) 0%,rgba(15,26,51,0) 22%,rgba(15,26,51,0) 50%,rgba(15,26,51,.85) 72%,{NAVY} 88%)"></div>'
area = D["kicker"]
pages = {}
# 1. kadr: hak (tekst w strefie 3:4, żeby był czytelny także w siatce)
pages["o00"] = page(grad + f'''<div class="top"><span>LLN MARBELLA</span><span>{area}</span></div>
<div style="position:absolute;left:70px;right:70px;top:1150px;text-align:center">
<div class="serif" style="font-size:120px">{D["title1"]}<br><em>{D["title2"]}</em></div>
<div style="font:300 40px Jost;color:#dfe4ee;margin-top:28px">{D["hook"]}</div></div>''')
for i, s in enumerate(D["shots"], 1):
    pages[f"o{i:02d}"] = page(grad + f'''<div class="top"><span>{i:02d} / {len(D["shots"]):02d}</span><span>{area}</span></div>
<div style="position:absolute;left:70px;right:70px;top:1270px">
<div class="mono" style="font-size:26px;letter-spacing:6px;color:{MUTED}">{s["label"]}</div>
<div class="serif" style="font-size:96px;margin-top:18px">{s["title"]}</div></div>''')
price = f'<div style="font:500 88px Jost;color:{ACC};margin-top:40px">{D["price"]}</div>' if D.get("price") else ""
pages["end"] = page(f'''<div style="position:absolute;inset:0;background:radial-gradient(circle at 80% 10%,#1c2b4c 0,{NAVY} 60%)"></div>
<div style="position:absolute;left:90px;right:90px;top:470px;text-align:center">
<div class="mono" style="font-size:28px;letter-spacing:8px;color:{ACC}">{area}</div>
<div class="serif" style="font-size:118px;margin-top:34px">{D.get("end_title1","Chcesz ją")}<br><em>{D.get("end_title2","zobaczyć?")}</em></div>
{price}
<div style="font:300 40px/1.45 Jost;color:#dfe4ee;margin-top:36px">{D.get("end_text","Umówimy prezentację na miejscu albo wideo po polsku.")}</div>
<div style="margin-top:70px;font:400 36px 'JetBrains Mono';line-height:1.8">+48 882 819 306<br><span style="color:{ACC}">llnmarbella.com</span></div></div>''', NAVY)
# okładka – styl ciekawostek: zdjęcie + granatowy pas, wszystko w kadrze 3:4 (y 240–1680)
pages["cover"] = page(f'''<div style="position:absolute;left:0;right:0;top:0;height:1250px;background:url('file://{D["cover"]}') {D.get("cover_pos","50% 50%")}/cover"></div>
<div style="position:absolute;left:0;right:0;top:1250px;bottom:0;background:{NAVY}"></div>
<div style="position:absolute;left:0;right:0;top:1246px;height:5px;background:{ACC}"></div>
<div style="position:absolute;left:70px;right:70px;top:1320px;text-align:center">
<div class="mono" style="font-size:26px;letter-spacing:7px;color:{ACC}">{area}</div>
<div class="serif" style="font-size:100px;margin-top:22px">{D["title1"]} <em>{D["title2"]}</em></div>
<div style="font:300 34px Jost;color:#dfe4ee;margin-top:22px">{D["hook"]}</div></div>
<div class="mono" style="position:absolute;left:0;right:0;top:1790px;text-align:center;font-size:24px;letter-spacing:8px;color:{MUTED}">LLN MARBELLA · COSTA DEL SOL</div>''', NAVY)

async def shots():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"), args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for k, h in pages.items():
            f = TMP / f"{k}.html"; f.write_text(h, encoding="utf-8")
            await pg.goto("file://" + str(f)); await pg.wait_for_timeout(500); await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=str(TMP / f"{k}.png"), omit_background=(k not in ("end", "cover")))
        await b.close()
asyncio.run(shots())

def seg(img, ov, out, zoom_in=True, dur=DUR):
    n = int(dur * FPS)
    z = f"'min(1+0.10*on/{n},1.10)'" if zoom_in else f"'max(1.10-0.10*on/{n},1.0)'"
    vf = (f"[0:v]scale=1188:2112:force_original_aspect_ratio=increase,crop=1188:2112,"
          f"zoompan=z={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS}[bg];[bg][1:v]overlay=0:0,format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", img, "-loop", "1", "-t", str(dur), "-i", ov,
                    "-filter_complex", vf, "-t", str(dur), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out], check=True)

parts = []; durs = []
seg(D["cover"], str(TMP / "o00.png"), str(TMP / "p00.mp4"), dur=3.2); parts.append(TMP / "p00.mp4"); durs.append(3.2)
for i, s in enumerate(D["shots"], 1):
    seg(s["img"], str(TMP / f"o{i:02d}.png"), str(TMP / f"p{i:02d}.mp4"), i % 2 == 0); parts.append(TMP / f"p{i:02d}.mp4"); durs.append(DUR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", "3.5", "-i", str(TMP / "end.png"), "-vf", "format=yuv420p", "-r", str(FPS),
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(TMP / "pend.mp4")], check=True); parts.append(TMP / "pend.mp4"); durs.append(3.5)
ins = []; [ins.extend(["-i", str(p)]) for p in parts]
fc = []; last = "[0:v]"; off = 0
for i in range(1, len(parts)):
    off += durs[i - 1] - XF; o = f"[x{i}]"
    fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={off:.2f}{o}"); last = o
total = off + durs[-1]
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, "-f", "lavfi", "-t", str(total), "-i", "anullsrc=r=44100:cl=stereo",
                "-filter_complex", ";".join(fc), "-map", last, "-map", f"{len(parts)}:a", "-shortest", "-c:v", "libx264", "-preset", "veryfast",
                "-crf", "24", "-maxrate", "1300k", "-bufsize", "2600k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(OUT / "reel.mp4")], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(TMP / "cover.png"), "-q:v", "3", str(OUT / "reel-cover.jpg")], check=True)
print("ok", OUT / "reel.mp4", f"{total:.1f}s")
