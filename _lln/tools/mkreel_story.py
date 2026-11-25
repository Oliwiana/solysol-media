# Dynamiczny film pionowy LLN (1080×1920) ze scen: zdjęcia + duży tekst + wizualizacje (licznik, mapa, oś czasu, dane).
# Użycie: python3 mkreel_story.py film.json katalog_wyjściowy → reel.mp4, reel-cover.jpg
# film.json: {"tag":"MARBELLA · HISTORIA", "cover":{"photo","pos","kicker","title1","title2","sub"},
#   "scenes":[
#     {"t":"title","photos":[...],"kicker","title1","title2","sub"},
#     {"t":"fact","photos":[2–3 zdjęcia],"label":"1832","title":"Hutnicza <em>potęga</em>","text":"1 krótkie zdanie","credit":"Fot. …"},
#     {"t":"counter","from":10000,"to":160000,"prefix":"","suffix":" mieszkańców","label":"1950 → DZIŚ","title":"Z miasteczka <em>w miasto</em>","photo":"tło (opcjonalnie)"},
#     {"t":"map","lon":-4.82,"lat":36.50,"name":"Los Monteros","sub":"Marbella · pierwsza linia plaży"},
#     {"t":"stats","items":[["6","sypialni"],["1229","m²"],["260","m² tarasów"]],"title":"W liczbach"},
#     {"t":"shot","photo":"…","label":"SALON","title":"Okna <em>na ogród</em>"},
#     {"t":"end","kicker","title1","title2","text","price":""}],
#   "audio":"lektor.mp3" (opcjonalnie), "music":"_assets/music/<plik>.mp3" (opcjonalnie), "music_volume":0.22}
# Bezpieczna strefa: tekst między y 260 a 1480 i 70 px od lewej / 150 px od prawej (UI Reels). Kursywa = akcent pomarańczowy.
import json, sys, os, subprocess, asyncio, math
from pathlib import Path
D = json.load(open(sys.argv[1])); OUT = Path(sys.argv[2]).resolve(); OUT.mkdir(parents=True, exist_ok=True)
TMP = OUT / "st_tmp"; TMP.mkdir(exist_ok=True)
ROOT = Path(__file__).resolve().parent
NAVY = "#0f1a33"; ACC = "#e8a04e"; INK = "#f3efe6"; MUTED = "#9aa6bf"; FPS = 30; XF = 0.25
FONTS = "".join(f'<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/{p}">' for p in [
    "cormorant-garamond/500.css", "cormorant-garamond/500-italic.css", "cormorant-garamond/600.css", "jost/300.css", "jost/400.css", "jost/500.css", "jetbrains-mono/400.css", "jetbrains-mono/500.css"])
CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1920px;color:{INK};font-family:Jost;overflow:hidden;position:relative}}
.mono{{font-family:'JetBrains Mono'}} .serif{{font-family:'Cormorant Garamond';font-weight:500;line-height:1.0}} em{{font-style:italic;color:{ACC}}}
.top{{position:absolute;left:70px;right:150px;top:250px;display:flex;justify-content:space-between;font:500 24px 'JetBrains Mono';letter-spacing:6px;text-shadow:0 2px 12px rgba(0,0,0,.8)}}
.sh{{text-shadow:0 4px 24px rgba(0,0,0,.55)}}"""
DASH = lambda h: h.replace("–", '<span style="font-family:\'Cormorant Garamond\';font-style:normal">–</span>')  # w Jost półpauza wygląda jak pauza
page = lambda b, bg="transparent": f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS} body{{background:{bg}}}</style></head><body>{DASH(b)}</body></html>'
shade = f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,.55) 0%,rgba(15,26,51,0) 20%,rgba(15,26,51,0) 42%,rgba(15,26,51,.78) 62%,rgba(15,26,51,.94) 80%,{NAVY} 100%)"></div>'
TAG = D.get("tag", "LLN MARBELLA")
SC = D["scenes"]; NF = sum(1 for s in SC if s["t"] in ("fact", "shot", "counter", "map", "stats"))
def bar(k):  # pasek postępu u góry (wizualnie „oś czasu”)
    segs = "".join(f'<div style="flex:1;height:6px;border-radius:3px;background:{ACC if i <= k else "rgba(255,255,255,.28)"}"></div>' for i in range(NF))
    return f'<div style="position:absolute;left:70px;right:150px;top:200px;display:flex;gap:8px">{segs}</div>'

pages = {}; plan = []  # plan: (rodzaj, dane)
k = -1
for si, s in enumerate(SC):
    t = s["t"]
    if t in ("fact", "shot", "counter", "map", "stats"): k += 1
    if t == "title":
        pages[f"s{si}"] = page(shade + f'''<div class="top"><span>{TAG}</span><span>LLN MARBELLA</span></div>
<div class="sh" style="position:absolute;left:70px;right:150px;top:1020px">
<div class="mono" style="font-size:28px;letter-spacing:8px;color:{ACC}">{s.get("kicker","")}</div>
<div class="serif" style="font-size:136px;margin-top:26px">{s["title1"]}<br><em>{s["title2"]}</em></div>
<div style="font:400 44px/1.3 Jost;color:#e8ecf4;margin-top:34px">{s.get("sub","")}</div></div>''')
        plan.append(("photos", si, s["photos"], s["dur"] / len(s["photos"]) if s.get("dur") else s.get("per", 1.5)))
    elif t in ("fact", "shot"):
        txt = f'<div style="font:400 52px/1.3 Jost;color:#e8ecf4;margin-top:30px">{s["text"]}</div>' if s.get("text") else ""
        cr = f'<div style="position:absolute;left:70px;right:150px;top:1590px;font:300 22px Jost;color:{MUTED}">{s["credit"]}</div>' if s.get("credit") else ""
        pages[f"s{si}"] = page(shade + bar(k) + f'''<div class="top"><span>{TAG}</span><span>{k+1:02d} / {NF:02d}</span></div>
<div class="sh" style="position:absolute;left:70px;right:150px;top:{1000 if s.get("text") else 1180}px">
<div class="mono" style="font-size:52px;font-weight:500;color:{ACC};letter-spacing:4px">{s["label"]}</div>
<div class="serif" style="font-size:122px;margin-top:18px">{s["title"]}</div>{txt}</div>{cr}''')
        _ph = s.get("photos") or [s["photo"]]
        plan.append(("photos", si, _ph, s["dur"] / len(_ph) if s.get("dur") else s.get("per", 1.6 if t == "fact" else 1.7)))
    elif t == "counter":
        n = 26
        for f in range(n + 1):
            e = 1 - (1 - f / n) ** 3; v = s["from"] + (s["to"] - s["from"]) * e
            num = f'{int(round(v)):,}'.replace(",", " ")
            bg = f'<div style="position:absolute;inset:0;background:url(\'file://{s["photo"]}\') center/cover;opacity:.28"></div>' if s.get("photo") else ""
            pages[f"s{si}_{f:02d}"] = page(bg + f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,.55),{NAVY} 70%)"></div>' + bar(k) + f'''
<div class="top"><span>{TAG}</span><span>{k+1:02d} / {NF:02d}</span></div>
<div style="position:absolute;left:70px;right:150px;top:640px">
<div class="mono" style="font-size:44px;color:{ACC};letter-spacing:4px">{s["label"]}</div>
<div style="font:500 190px Jost;margin-top:30px;letter-spacing:-4px">{s.get("prefix","")}{num}</div>
<div style="font:300 54px Jost;color:#e8ecf4;margin-top:6px">{s.get("suffix","")}</div>
<div class="serif" style="font-size:104px;margin-top:60px">{s["title"]}</div>
<div style="font:400 44px/1.3 Jost;color:#e8ecf4;margin-top:26px">{s.get("text","")}</div></div>''', NAVY)
        plan.append(("seq", si, n + 1, s["dur"] - (n + 1) / 20 if s.get("dur") else s.get("hold", 2.6)))
    elif t == "map":
        coast = json.load(open(ROOT / "coast.json"))[1]
        W0, E0, S0, N0 = -5.33, -4.35, 36.25, 36.78
        X = lambda lon: 40 + (lon - W0) / (E0 - W0) * 1000
        Y = lambda lat: 1560 - (lat - S0) / (N0 - S0) * 1000
        pts = [p for p in coast if W0 - .05 < p[0] < E0 + .05 and S0 - .05 < p[1] < N0 + .1]
        pts.sort(key=lambda p: p[0])
        line = " ".join(f"{X(a):.0f},{Y(b):.0f}" for a, b in pts)
        land = f"M0,0 L0,{Y(pts[0][1]):.0f} L" + " L".join(f"{X(a):.0f},{Y(b):.0f}" for a, b in pts) + f" L1080,{Y(pts[-1][1]):.0f} L1080,0 Z"
        towns = [("Málaga", -4.42, 36.72), ("Fuengirola", -4.625, 36.54), ("Marbella", -4.885, 36.51), ("Estepona", -5.146, 36.427), ("Sotogrande", -5.28, 36.29)]
        tw = "".join(f'<circle cx="{X(a):.0f}" cy="{Y(b):.0f}" r="7" fill="{MUTED}"/><text x="{X(a)+(14 if a < -4.5 else -14):.0f}" y="{Y(b)-14:.0f}" text-anchor="{'start' if a < -4.5 else 'end'}" fill="{MUTED}" font-family="JetBrains Mono" font-size="24" letter-spacing="3">{n.upper()}</text>' for n, a, b in towns)
        px, py = X(s["lon"]), Y(s["lat"]); n = 18
        for f in range(n + 1):
            e = min(1, f / n); r = 60 * (1 - e) + 26; op = e
            pin = (f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{r*2.2:.0f}" fill="none" stroke="{ACC}" stroke-width="3" opacity="{(1-e)*.9:.2f}"/>'
                   f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{r if f<n else 22:.0f}" fill="{ACC}" opacity="{op:.2f}"/><circle cx="{px:.0f}" cy="{py:.0f}" r="8" fill="{NAVY}" opacity="{op:.2f}"/>')
            lab = f'<text x="{px-20:.0f}" y="{py+90:.0f}" fill="{INK}" font-family="Cormorant Garamond" font-style="italic" font-size="64" opacity="{op:.2f}">{s["name"]}</text>'
            svg = f'''<svg width="1080" height="1920" style="position:absolute;inset:0"><path d="{land}" fill="#1b2a4b"/><polyline points="{line}" fill="none" stroke="#3a4d78" stroke-width="3"/>{tw}{pin}{lab}
<text x="420" y="1640" fill="#33456d" font-family="Cormorant Garamond" font-size="40" letter-spacing="14">MORZE ŚRÓDZIEMNE</text></svg>'''
            pages[f"s{si}_{f:02d}"] = page(svg + bar(k) + f'''<div class="top"><span>{TAG}</span><span>{k+1:02d} / {NF:02d}</span></div>
<div style="position:absolute;left:70px;right:150px;top:330px"><div class="mono" style="font-size:30px;color:{ACC};letter-spacing:6px">GDZIE TO JEST</div>
<div class="serif" style="font-size:96px;margin-top:14px">{s.get("title","Lokalizacja")}</div>
<div style="font:400 40px Jost;color:#e8ecf4;margin-top:16px">{s.get("sub","")}</div></div>''', NAVY)
        plan.append(("seq", si, n + 1, s["dur"] - (n + 1) / 20 if s.get("dur") else s.get("hold", 2.4)))
    elif t == "stats":
        n = 22
        for f in range(n + 1):
            e = 1 - (1 - f / n) ** 3; rows = ""
            for i, (v, lab) in enumerate(s["items"]):
                try:
                    tv = float(v.replace(",", ".").replace(" ", "")); cur = tv * e
                    show = (f"{cur:.1f}".replace(".", ",") if "," in v else f"{int(round(cur)):,}".replace(",", " "))
                except ValueError:
                    show = v
                w = int(860 * e)
                rows += f'''<div style="margin-top:{0 if i==0 else 54}px"><div style="display:flex;align-items:baseline;gap:22px"><div style="font:500 128px Jost;letter-spacing:-2px">{show}</div>
<div style="font:300 48px Jost;color:#e8ecf4">{lab}</div></div><div style="height:6px;width:{w}px;background:{ACC};margin-top:10px;border-radius:3px"></div></div>'''
            pages[f"s{si}_{f:02d}"] = page(bar(k) + f'''<div class="top"><span>{TAG}</span><span>{k+1:02d} / {NF:02d}</span></div>
<div style="position:absolute;left:70px;right:150px;top:420px"><div class="mono" style="font-size:30px;color:{ACC};letter-spacing:6px">{s.get("kicker","W LICZBACH")}</div>
<div class="serif" style="font-size:100px;margin:16px 0 60px">{s.get("title","")}</div>{rows}</div>''', NAVY)
        plan.append(("seq", si, n + 1, s["dur"] - (n + 1) / 20 if s.get("dur") else s.get("hold", 2.6)))
    elif t == "end":
        price = f'<div style="font:500 96px Jost;color:{ACC};margin-top:36px">{s["price"]}</div>' if s.get("price") else ""
        pages[f"s{si}"] = page(f'''<div style="position:absolute;inset:0;background:radial-gradient(circle at 80% 10%,#1c2b4c 0,{NAVY} 60%)"></div>
<div style="position:absolute;left:70px;right:150px;top:480px">
<div class="mono" style="font-size:28px;letter-spacing:8px;color:{ACC}">{s.get("kicker","LLN MARBELLA · OD 2010")}</div>
<div class="serif" style="font-size:124px;margin-top:30px">{s["title1"]}<br><em>{s["title2"]}</em></div>{price}
<div style="font:300 44px/1.4 Jost;color:#e8ecf4;margin-top:36px">{s.get("text","")}</div>
<div style="margin-top:70px;font:500 40px 'JetBrains Mono';line-height:1.8">+48 882 819 306<br><span style="color:{ACC}">llnmarbella.com</span></div></div>''', NAVY)
        plan.append(("still", si, None, s.get("dur", s.get("hold", 3.6))))
cv = D["cover"]
pages["cover"] = page(f'''<div style="position:absolute;left:0;right:0;top:0;height:1250px;background:url('file://{cv["photo"]}') {cv.get("pos","50% 50%")}/cover"></div>
<div style="position:absolute;left:0;right:0;top:1250px;bottom:0;background:{NAVY}"></div><div style="position:absolute;left:0;right:0;top:1246px;height:5px;background:{ACC}"></div>
<div style="position:absolute;left:60px;right:60px;top:1310px;text-align:center">
<div class="mono" style="font-size:26px;letter-spacing:7px;color:{ACC}">{cv["kicker"]}</div>
<div class="serif" style="font-size:{cv.get("size",100)}px;margin-top:20px">{cv["title1"]} <em>{cv["title2"]}</em></div>
<div style="font:300 34px Jost;color:#dfe4ee;margin-top:20px">{cv.get("sub","")}</div></div>
<div class="mono" style="position:absolute;left:0;right:0;top:1790px;text-align:center;font-size:24px;letter-spacing:8px;color:{MUTED}">LLN MARBELLA · COSTA DEL SOL</div>''', NAVY)

async def shots():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"), args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for kk, h in pages.items():
            f = TMP / f"{kk}.html"; f.write_text(h, encoding="utf-8")
            await pg.goto("file://" + str(f)); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(120)
            await pg.screenshot(path=str(TMP / f"{kk}.png"), omit_background=True)
        await b.close()
asyncio.run(shots())

def enc(args, out): subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args, "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", str(out)], check=True)
parts = []; zi = 0
for pi, (kind, si, data, dur) in enumerate(plan):
    last_scene = pi == len(plan) - 1
    if kind == "photos":
        for j, ph in enumerate(data):
            dur0 = dur + (XF if not (last_scene and j == len(data) - 1) else 0)
            zi += 1; n = int(dur0 * FPS); o = TMP / f"p{si:02d}_{j}.mp4"
            z = f"'min(1+0.12*on/{n},1.12)'" if zi % 2 else f"'max(1.12-0.12*on/{n},1.0)'"
            fade = "fade=in:st=0.1:d=0.35:alpha=1," if j == 0 else ""
            enc(["-i", ph, "-loop", "1", "-t", str(dur0), "-i", str(TMP / f"s{si}.png"), "-filter_complex",
                 f"[0:v]scale=1188:2112:force_original_aspect_ratio=increase,crop=1188:2112,zoompan=z={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS}[bg];"
                 f"[1:v]format=rgba,{fade}null[ov];[bg][ov]overlay=0:0", "-t", str(dur0)], o)
            parts.append((o, dur0))
    elif kind == "seq":
        o = TMP / f"p{si:02d}.mp4"; anim = data / 20; dur = dur + (0 if last_scene else XF)
        enc(["-framerate", "20", "-i", str(TMP / f"s{si}_%02d.png"), "-vf", f"tpad=stop_mode=clone:stop_duration={dur},fps={FPS},format=yuv420p", "-t", str(anim + dur)], o)
        parts.append((o, anim + dur))
    else:
        dur = dur + (0 if last_scene else XF)
        o = TMP / f"p{si:02d}.mp4"; enc(["-loop", "1", "-t", str(dur), "-i", str(TMP / f"s{si}.png"), "-t", str(dur)], o); parts.append((o, dur))
ins = []; [ins.extend(["-i", str(p)]) for p, _ in parts]
fc = []; last = "[0:v]"; off = 0
for i in range(1, len(parts)):
    off += parts[i - 1][1] - XF; o = f"[x{i}]"
    fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={off:.2f}{o}"); last = o
total = off + parts[-1][1]
AUD = ["-f", "lavfi", "-t", str(total), "-i", "anullsrc=r=44100:cl=stereo"]; AF = ""
NP = len(parts)
if D.get("audio"):
    AUD = ["-i", D["audio"]]; AF = f";[{NP}:a]adelay={int(D.get('audio_delay', 0.3)*1000)}:all=1,loudnorm=I=-16:TP=-1.5,apad[aout]"
# muzyka pod lektorem: zapętlona, cicha, automatycznie ściszana, gdy mówi lektor (sidechain), wyciszenie na końcu
MUS = D.get("music")
if MUS:
    AUD += ["-stream_loop", "-1", "-i", MUS]; mi = NP + 1; mv = D.get("music_volume", 0.22)
    if D.get("audio"):
        AF = (f";[{NP}:a]adelay={int(D.get('audio_delay', 0.3)*1000)}:all=1,loudnorm=I=-16:TP=-1.5,apad,asplit=2[v1][v2]"
              f";[{mi}:a]atrim=0:{total:.2f},volume={mv},afade=t=in:d=0.8,afade=t=out:st={max(total-2.0,0):.2f}:d=2[m0]"
              f";[m0][v1]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[mduck]"
              f";[mduck][v2]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[aout]")
    else:
        AF = f";[{mi}:a]atrim=0:{total:.2f},volume={mv*2.5},afade=t=in:d=0.8,afade=t=out:st={max(total-2.0,0):.2f}:d=2,loudnorm=I=-16:TP=-1.5[aout]"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, *AUD,
                "-filter_complex", ";".join(fc) + AF, "-map", last, "-map", "[aout]" if AF else f"{len(parts)}:a", "-t", str(total), "-c:v", "libx264", "-preset", "veryfast",
                "-crf", "25", "-maxrate", "1000k", "-bufsize", "2000k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(OUT / "reel.mp4")], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(TMP / "cover.png"), "-q:v", "3", str(OUT / "reel-cover.jpg")], check=True)
print("ok", OUT / "reel.mp4", f"{total:.1f}s", len(parts), "ujęć")
