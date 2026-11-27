import json, asyncio, math, subprocess
from pathlib import Path
land=json.load(open('/home/claude/lln/route-land.json'))
L0,L1,A0,A1=-10.5,5.0,32.4,45.2; K=math.cos(math.radians(39))
W=1080; S=W/((L1-L0)*K); H=(A1-A0)*S; Y0=330
P=lambda lo,la:((lo-L0)*K*S, Y0+(A1-la)*S)
paths="".join('<path d="M'+" L".join(f"{P(x,y)[0]:.1f},{P(x,y)[1]:.1f}" for x,y in r)+'Z"/>' for r in land)
C=[("TULUZA",1.44,43.60,1),("BARCELONA",2.17,41.39,0),("ALICANTE",-0.49,38.35,1),("MÁLAGA",-4.42,36.72,0),("TANGER",-5.81,35.76,1),("CASABLANCA",-7.59,33.57,1)]
pts=[P(lo,la) for _,lo,la,_ in C]
seg=[math.dist(pts[i],pts[i+1]) for i in range(len(pts)-1)]; tot=sum(seg)
d="M"+" L".join(f"{x:.1f},{y:.1f}" for x,y in pts)
def html():
    cities="".join(f'<g id="c{i}" style="opacity:0"><circle cx="{x:.1f}" cy="{y:.1f}" r="{13 if n=="MÁLAGA" else 8}" fill="{"#e8a04e" if n=="MÁLAGA" else "#f3efe6"}"/>'
        f'<text x="{x+(22 if r else -22):.1f}" y="{y+9:.1f}" text-anchor="{"start" if r else "end"}" font-family="JetBrains Mono" font-weight="500" font-size="{30 if n=="MÁLAGA" else 24}" letter-spacing="4" fill="{"#e8a04e" if n=="MÁLAGA" else "#c9d1e3"}">{n}</text></g>'
        for i,((n,lo,la,r),(x,y)) in enumerate(zip(C,pts)))
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/jetbrains-mono/500.css">
<link rel="stylesheet" href="file:///home/claude/tools/node_modules/@fontsource/cormorant-garamond/500-italic.css">
<style>body{{margin:0;width:1080px;height:1920px;background:#0f1a33;overflow:hidden}}</style></head><body><div style="position:absolute;font-family:JetBrains Mono;opacity:0">x</div>
<svg width="1080" height="1920" viewBox="0 0 1080 1920">
<defs><radialGradient id="g" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#16244a"/><stop offset="1" stop-color="#0b1429"/></radialGradient></defs>
<rect width="1080" height="1920" fill="url(#g)"/>
<g fill="#1f3058" stroke="#3a5288" stroke-width="1.6">{paths}</g>
<text x="{P(0.2,37.2)[0]:.0f}" y="{P(0.2,37.2)[1]:.0f}" font-family="Cormorant Garamond" font-style="italic" font-size="40" fill="#4f679c">Morze Śródziemne</text>
<text x="40" y="{P(-10,38.2)[1]:.0f}" font-family="Cormorant Garamond" font-style="italic" font-size="36" fill="#4f679c">Atlantyk</text>
<path id="rt" d="{d}" fill="none" stroke="#e8a04e" stroke-width="5" stroke-linecap="round" stroke-dasharray="{tot:.1f}" stroke-dashoffset="{tot:.1f}"/>
{cities}
<text id="pl" font-size="44" fill="#fff" style="opacity:0">✈</text>
</svg>
<script>
const pts={json.dumps([[round(x,1),round(y,1)] for x,y in pts])};const tot={tot:.1f};
window.setT=(p)=>{{ // p 0..1
 const e=p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2; const L=e*tot;
 document.getElementById('rt').setAttribute('stroke-dashoffset',tot-L);
 let acc=0,pos=pts[0],ang=0;
 for(let i=0;i<pts.length-1;i++){{const a=pts[i],b=pts[i+1],s=Math.hypot(b[0]-a[0],b[1]-a[1]);
  if(acc+s>=L){{const k=(L-acc)/s;pos=[a[0]+(b[0]-a[0])*k,a[1]+(b[1]-a[1])*k];ang=Math.atan2(b[1]-a[1],b[0]-a[0]);break}} acc+=s;pos=b;}}
 acc=0; for(let i=0;i<pts.length;i++){{ if(i>0) acc+=Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]);
   const o=Math.max(0,Math.min(1,(L-acc+25)/40)); document.getElementById('c'+i).style.opacity=o; }}
 const pl=document.getElementById('pl'); pl.style.opacity=p<.98?1:0;
 pl.setAttribute('transform',`translate(${{pos[0]}},${{pos[1]}}) rotate(${{ang*180/Math.PI}}) translate(-20,15)`);
}};
</script></body></html>'''
async def main():
    from playwright.async_api import async_playwright
    Path('f').mkdir(exist_ok=True); Path('r.html').write_text(html(),encoding='utf-8')
    FPS=25; DUR=6.7; N=int(FPS*DUR)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--allow-file-access-from-files"]); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto("file://"+str(Path('r.html').resolve())); await pg.evaluate("document.fonts.ready")
        for i in range(N):
            pr=min(1,max(0,(i/FPS-0.3)/5.2))
            await pg.evaluate(f"setT({pr})"); await pg.screenshot(path=f"f/{i:04d}.jpg",type="jpeg",quality=90)
        await b.close()
    subprocess.run(["ffmpeg","-loglevel","error","-y","-framerate",str(FPS),"-i","f/%04d.jpg","-c:v","libx264","-pix_fmt","yuv420p","-crf","18","route.mp4"],check=True)
asyncio.run(main())
