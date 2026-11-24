import json,sys,subprocess,os
sys.path.insert(0,'/tmp/g'); from magcov import FONTS, D as MD, page as magpage
C='/tmp/sm/_photos/commons/'
CSS=f'''{FONTS}*{{box-sizing:border-box;margin:0}}html,body{{width:1080px;height:1350px;overflow:hidden;font-family:IN;background:#0A1422;color:#FAF7F2}}
.top{{position:absolute;left:64px;right:64px;top:44px;display:flex;justify-content:space-between;font-size:16px;font-weight:600;letter-spacing:.18em;padding-bottom:12px;border-bottom:1px solid rgba(250,247,242,.35)}}
.top b{{font-family:CG;font-size:30px;letter-spacing:.08em;font-weight:600}}
.ph{{position:absolute;left:0;right:0;top:0;height:640px;background-size:cover}}
.phg{{position:absolute;left:0;right:0;top:0;height:650px;background:linear-gradient(180deg,rgba(10,20,34,.85) 0%,rgba(10,20,34,.1) 22%,rgba(10,20,34,0) 70%,#0A1422 100%)}}
.cr{{position:absolute;right:64px;font-size:13px;opacity:.6}}
.kick{{display:inline-block;background:#F2C14E;color:#171513;font-size:17px;font-weight:800;letter-spacing:.18em;padding:7px 14px}}
h1{{font-family:CG;font-weight:600;font-size:76px;line-height:1.02;margin-top:18px}} h1 i{{color:#F2C14E}}
.bd p{{font-size:29px;line-height:1.42;margin-top:20px;opacity:.95}} .bd b{{color:#F2C14E;font-weight:800}}
.ft{{position:absolute;left:64px;right:64px;bottom:30px;display:flex;justify-content:space-between;font-size:15px;letter-spacing:.16em;opacity:.7;border-top:1px solid rgba(250,247,242,.3);padding-top:16px}}
.row{{display:flex;gap:34px;align-items:baseline;border-bottom:1px solid rgba(250,247,242,.18);padding:26px 0}}
.num{{font-family:CG;font-weight:600;font-size:84px;color:#F2C14E;min-width:240px;line-height:1}}
'''
def top(ep,i,n): return f'<div class=top><b>SOL Y SÓL</b><span>GWIAZDY NA COSTA DEL SOL · ODC. {ep}</span><span>{i}/{n}</span></div>'
def ft(last=False): return f'<div class=ft><span>{"" if last else "PRZESUŃ →"}</span><span>SOLYSOL.PL</span></div>'
def slide(s,ep,i,n):
    t=s.get('type')
    h=f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>'
    if t in (None,'where') and s.get('photo'):
        h+=f'<div class=ph style="background-image:url(file://{C}{s["photo"]});background-position:{s.get("pos","50% 50%")}"></div><div class=phg></div><div class=cr style="top:604px">{s["credit"]}</div>'
    h+=top(ep,i,n)
    if t is None:
        body=''.join(f'<p>{p}</p>' for p in s['body'])
        h+=f'<div style="position:absolute;left:64px;right:64px;top:650px"><span class=kick>{s["kicker"]}</span><h1>{s["head"]}</h1><div class=bd>{body}</div></div>'
    elif t=='numbers':
        rows=''.join(f'<div class=row><div class=num>{a}</div><div style="font-size:32px;line-height:1.3">{b}</div></div>' for a,b in s['rows'])
        h+=f'<div style="position:absolute;left:64px;right:64px;top:170px"><span class=kick>{s["kicker"]}</span><h1 style="font-size:84px">{s["head"]}</h1><div style="margin-top:30px">{rows}</div></div>'
    elif t=='where':
        rows=''.join(f'<div class=row style="padding:18px 0"><div style="font-size:16px;font-weight:800;letter-spacing:.16em;color:#F2C14E;min-width:220px">{a}</div><div style="font-size:27px;line-height:1.35">{b}</div></div>' for a,b in s['rows'])
        h+=f'<div style="position:absolute;left:64px;right:64px;top:640px"><span class=kick>GDZIE TO DZIŚ ZOBACZYĆ</span><h1>{s["head"]}</h1><div style="margin-top:10px">{rows}</div></div>'
    elif t=='cta':
        eps=''.join(f'<div class=row style="padding:16px 0"><div style="font-size:16px;font-weight:800;letter-spacing:.16em;color:#F2C14E;min-width:150px">{a}</div><div style="font-family:CG;font-size:36px">{b}</div></div>' for a,b,*_ in s['eps'])
        h+=f'''<div style="position:absolute;left:0;right:0;top:0;height:1350px;background:radial-gradient(circle at 80% 10%,rgba(242,193,78,.25),transparent 45%)"></div>
<div style="position:absolute;left:64px;right:64px;top:240px;text-align:center"><div style="display:inline-block;width:210px;height:210px;border-radius:50%;background:#C62828;border:3px dashed #F2C14E;transform:rotate(-8deg);padding-top:52px"><div style="font-size:16px;font-weight:800;letter-spacing:.2em">CAŁA SERIA</div><div style="font-family:CG;font-style:italic;font-size:46px">na profilu</div></div>
<h1 style="font-size:92px;margin-top:34px">Obserwuj – <i>kolejne historie</i> w drodze</h1><div style="font-size:28px;margin-top:20px;opacity:.9">{s["sub"]}</div></div>
<div style="position:absolute;left:120px;right:120px;top:{s.get("ey",820)}px">{eps}</div><div style="position:absolute;left:64px;right:64px;bottom:90px;font-size:15px;opacity:.55">{s["note"]}</div>'''
    h+=ft(t=='cta')+'</body></html>'
    return h
def render(html,out):
    p=out.replace('.jpg','.html'); open(p,'w').write(html)
    for _ in range(2): subprocess.run(['google-chrome','--headless','--no-sandbox','--allow-file-access-from-files','--hide-scrollbars','--window-size=1080,1350',f'--screenshot={out}.png',f'file://{p}'],capture_output=True)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',out+'.png','-q:v','2',out]); os.remove(out+'.png')
for ep in map(int,sys.argv[1:]):
    d=json.load(open(f'/tmp/g/ep{ep}.json')); od=f'/tmp/g/k{ep}'; os.makedirs(od,exist_ok=True)
    n=len(d['slides'])+1
    MD[ep]['d']='25.11.2026'; render(magpage(MD[ep],1350).replace('Z DŹWIĘKIEM ▶','PRZESUŃ →'),f'{od}/ig-1.jpg')
    for i,s in enumerate(d['slides']):
        if i==len(d['slides'])-1 and s.get('type')=='cta' and ep==4: s['eps']=[['ODC. 1','Marbella Club i książę Alfonso'],['ODC. 2','Hemingway w Churrianie'],['ODC. 3','Torremolinos i Pez Espada'],['ODC. 5','Andersen w Maladze']]
        render(slide(s,ep,i+2,n),f'{od}/ig-{i+2}.jpg')
    print(ep,'ok',n)
