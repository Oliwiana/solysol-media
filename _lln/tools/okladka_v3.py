# Okładka v3 – układ magazynowy: zdjęcie w oknie (ostre, bez nadmiernego powiększenia), tytuł na granacie, pasek danych.
# Cały tekst w strefie y 250–1650 (kadr siatki 3:4 = y 240–1680).
import asyncio, json, sys
from pathlib import Path
F="".join(f'<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/{p}">' for p in ["cormorant-garamond/500.css","cormorant-garamond/500-italic.css","jost/300.css","jost/400.css","jost/500.css","jetbrains-mono/400.css","jetbrains-mono/500.css"])
D='<span style="font-family:Cormorant Garamond;font-style:normal">–</span>'
N="#0f1a33"; A="#e8a04e"
def html(c):
    chips="".join(f'<div style="flex:1;text-align:center;{"border-left:1px solid #33456d;" if i else ""}"><div style="font:500 50px Jost;color:{A if i==len(c["chips"])-1 else "#f3efe6"};letter-spacing:-.5px">{v}</div><div style="font:400 19px JetBrains Mono;letter-spacing:5px;color:#9aa6bf;margin-top:8px">{l}</div></div>' for i,(v,l) in enumerate(c["chips"]))
    return f'''<!doctype html><html><head><meta charset="utf-8">{F}<style>*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{N};color:#f3efe6;position:relative;overflow:hidden;font-family:Jost}}
em{{font-style:italic;color:{A}}}</style></head><body>
<div style="position:absolute;inset:0;background:radial-gradient(circle at 85% 70%,#1c2b4c 0,{N} 55%)"></div>
<div style="position:absolute;left:70px;right:70px;top:262px;display:flex;justify-content:space-between;align-items:center;font:500 23px 'JetBrains Mono';letter-spacing:8px">
<span>LLN&nbsp;MARBELLA</span><span style="color:{A}">{c.get("badge","FILM ▶")}</span></div>
<div style="position:absolute;left:70px;right:70px;top:318px;height:1px;background:#33456d"></div>
<div style="position:absolute;left:0;right:0;top:350px;height:{c.get("ph",780)}px;overflow:hidden">
<div style="position:absolute;inset:0;background:url('file://{c["photo"]}') {c.get("pos","50% 50%")}/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,0) 70%,rgba(15,26,51,.55) 100%)"></div>
<div style="position:absolute;left:70px;bottom:34px;background:{N};padding:13px 20px 11px;font:500 22px 'JetBrains Mono';letter-spacing:6px;color:{A}">{c["kicker"]}</div></div>
<div style="position:absolute;left:70px;right:70px;top:{350+c.get("ph",780)+56}px">
<div style="font-family:'Cormorant Garamond';font-weight:500;font-size:{c.get("size",118)}px;line-height:.96">{c["t1"]}<br><em>{c["t2"]}</em></div></div>
<div style="position:absolute;left:70px;right:70px;top:1480px;border-top:1px solid #33456d;padding-top:30px;display:flex">{chips}</div>
<div style="position:absolute;left:0;right:0;top:1745px;text-align:center;font:400 22px 'JetBrains Mono';letter-spacing:8px;color:#9aa6bf">COSTA DEL SOL · PO POLSKU</div>
</body></html>'''
async def main():
    from playwright.async_api import async_playwright
    cs=json.load(open(sys.argv[1]))
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--allow-file-access-from-files"]); pg=await b.new_page(viewport={"width":1080,"height":1920})
        for c in cs:
            f=Path(c["out"]).with_suffix(".html"); f.write_text(html(c),encoding="utf-8")
            await pg.goto("file://"+str(f.resolve())); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=c["out"],type="jpeg",quality=92)
        await b.close()
asyncio.run(main())
