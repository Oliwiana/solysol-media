# Okładka v4 – kinowa, pełne zdjęcie, cienka ramka, tytuł w dolnej części kadru siatki (y 240–1680).
import asyncio, json, sys
from pathlib import Path
F="".join(f'<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/{p}">' for p in ["cormorant-garamond/400.css","cormorant-garamond/500.css","cormorant-garamond/500-italic.css","jost/300.css","jost/400.css","jetbrains-mono/400.css","jetbrains-mono/500.css"])
N="#0f1a33"; A="#e8a04e"
def html(c):
    dot='<span style="color:%s;margin:0 18px">·</span>'%A
    facts=dot.join(c["facts"])
    return f'''<!doctype html><html><head><meta charset="utf-8">{F}<style>*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{N};color:#f3efe6;position:relative;overflow:hidden;font-family:Jost}}
em{{font-style:italic;color:{A}}}</style></head><body>
<div style="position:absolute;inset:0;background:url('file://{c["photo"]}') {c.get("pos","50% 50%")}/cover;filter:saturate(1.05) contrast(1.04)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,.97) 0%,rgba(15,26,51,.88) 10%,rgba(15,26,51,.25) 19%,rgba(15,26,51,0) 27%,rgba(15,26,51,0) {c.get("g1",44)}%,rgba(15,26,51,.78) {c.get("g2",58)}%,rgba(15,26,51,.985) {c.get("g3",70)}%,{N} 100%)"></div>
{'<div style="position:absolute;left:0;right:0;top:0;height:230px;background:linear-gradient(180deg,#0f1a33 75%,rgba(15,26,51,0))"></div>' if c.get("topsolid") else ""}
<div style="position:absolute;left:56px;right:56px;top:268px;bottom:236px;border:1.5px solid rgba(243,239,230,.38)"></div>
<div style="position:absolute;left:0;right:0;top:236px;text-align:center"><span style="background:transparent;padding:0 26px;font:500 23px 'JetBrains Mono';letter-spacing:10px;color:#fff;text-shadow:0 2px 16px rgba(0,0,0,.55)">LLN&nbsp;MARBELLA</span></div>
<div style="position:absolute;right:92px;top:304px;display:flex;align-items:center;gap:12px;font:500 20px 'JetBrains Mono';letter-spacing:6px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)">
<span style="display:inline-flex;width:46px;height:46px;border-radius:50%;border:1.5px solid rgba(255,255,255,.85);align-items:center;justify-content:center;padding-left:4px;font-size:16px">▶</span>{c.get("badge","FILM")}</div>
<div style="position:absolute;left:80px;right:80px;top:{c.get("top",1190)}px;text-align:center">
<div style="display:flex;align-items:center;justify-content:center;gap:22px;font:500 24px 'JetBrains Mono';letter-spacing:8px;color:{A}">
<span style="width:56px;height:1.5px;background:{A}"></span>{c["kicker"]}<span style="width:56px;height:1.5px;background:{A}"></span></div>
<div style="font-family:'Cormorant Garamond';font-weight:500;font-size:{c.get("size",128)}px;line-height:.95;margin-top:30px;text-shadow:0 4px 30px rgba(0,0,0,.35)">{c["t1"]}<br><em>{c["t2"]}</em></div>
<div style="font:300 32px Jost;color:#e6eaf2;margin-top:34px;letter-spacing:.5px">{facts}</div></div>
<div style="position:absolute;left:0;right:0;top:1712px;text-align:center;font:400 21px 'JetBrains Mono';letter-spacing:9px;color:#8e9ab5">COSTA DEL SOL · PO POLSKU</div>
</body></html>'''
async def main():
    from playwright.async_api import async_playwright
    cs=json.load(open(sys.argv[1]))
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--allow-file-access-from-files"]); pg=await b.new_page(viewport={"width":1080,"height":1920})
        for c in cs:
            f=Path(c["out"]).with_suffix(".html"); f.write_text(html(c),encoding="utf-8")
            await pg.goto("file://"+str(f.resolve())); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=c["out"],type="jpeg",quality=93)
        await b.close()
asyncio.run(main())
