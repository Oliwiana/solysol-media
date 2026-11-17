# usage: python3 gen_day.py data.json  -> renders IG 3 slides + FB single into out/<id>/
import json,sys,os,subprocess
exec(open('/home/claude/social/news2/gen.py').read().split("cover('n1'")[0])
CR['ban2_bwf.jpg']=CR.get('ban2.jpg','')
DATE=sys.argv[2] if len(sys.argv)>2 else '16.11.2026'
src=open('/home/claude/social/news2/gen.py').read()
for a,b in [("WIADOMOŚCI · 16.11.2026","WIADOMOŚCI · '+DATE+'")]: pass

F2='/home/claude/tools/node_modules/@fontsource/'
FX=''.join(f"@font-face{{font-family:Anton;src:url(file://{F2}anton/files/anton-{sub}-400-normal.woff2)}}" for sub in ('latin','latin-ext'))+''.join(f"@font-face{{font-family:Oswald;font-weight:{w};src:url(file://{F2}oswald/files/oswald-{sub}-{w}-normal.woff2)}}" for w in (500,600,700) for sub in ('latin','latin-ext'))
AN="font-family:Anton,Impact,sans-serif;letter-spacing:.01em;"
OS="font-family:Oswald,'Arial Narrow',sans-serif;"
def okladka(d,date):
    photo=d['photo']; cred=d.get('cred') or (('Fot. '+CR[photo]+' / Unsplash') if photo in CR else 'Il. Redakcja Sol y Sól')
    h=f"""<div style="position:absolute;inset:0;background:#141210"></div>
<div style="position:absolute;left:40px;right:40px;top:34px;height:54px;background:#F3EFE8;display:flex;align-items:center;justify-content:space-between;padding:0 20px;{OS}color:#141210">
<span style="font-size:19px;font-weight:700;letter-spacing:.12em;color:#C8692E">{d.get('strip_tag','DZIŚ')} ▸</span><span style="font-size:25px;font-weight:600;text-transform:uppercase">{d.get('strip','')}</span><span style="font-size:19px;font-weight:700;letter-spacing:.12em">1/3</span></div>
<div style="position:absolute;left:40px;right:40px;top:104px;display:flex;justify-content:space-between;{OS}font-size:18px;font-weight:500;letter-spacing:.2em;color:#CBBFAE"><span><b style="color:#E0874F">{d.get('mast','WIADOMOŚCI')}</b> · {date}</span><span>COSTA DEL SOL PO POLSKU</span></div>
<div style="position:absolute;left:40px;right:40px;top:138px;height:1px;background:rgba(243,239,232,.35)"></div>
<div style="position:absolute;left:0;right:0;top:146px;text-align:center;color:#F3EFE8;{CG}font-size:190px;font-weight:500;line-height:1;letter-spacing:.03em;white-space:nowrap">S<span style="display:inline-block;width:124px;height:124px;border-radius:50%;background:#E0874F;vertical-align:-2px;margin:0 4px"></span>L <i style="color:#E0874F;font-size:134px">y</i> SÓL</div>
<div style="position:absolute;left:40px;right:40px;top:356px;height:1px;background:rgba(243,239,232,.35)"></div>
<div style="position:absolute;left:40px;right:40px;top:372px;bottom:150px;overflow:hidden"><img src="file:///home/claude/photos_raw/{photo}" style="width:100%;height:100%;object-fit:cover;object-position:{d['pos']};filter:contrast(1.1) brightness(.9)"></div>
<div style="position:absolute;left:40px;right:40px;top:372px;bottom:150px;background:linear-gradient(180deg,rgba(20,18,16,.6) 0%,rgba(20,18,16,.05) 30%,rgba(20,18,16,.2) 52%,rgba(20,18,16,.96) 100%)"></div>
<div style="position:absolute;left:66px;top:398px">{tag(d['desk'])}</div>
<div style="position:absolute;right:66px;top:398px;font-size:15px;color:rgba(243,239,232,.75)">{cred}</div>
<div style="position:absolute;left:70px;right:70px;top:690px;color:#fff;{CG}font-size:76px;font-style:italic;font-weight:500;line-height:1;text-shadow:0 2px 14px rgba(0,0,0,.6)">{d.get('over','')}</div>
<div style="position:absolute;left:40px;top:790px;background:#E0874F;padding:10px 30px 0;{AN}font-size:{d.get('blocksize',150)}px;line-height:1;color:#141210;box-shadow:0 10px 30px rgba(0,0,0,.35);white-space:nowrap">{d['block']}</div>
<div style="position:absolute;left:70px;right:70px;top:{790+d.get('blocksize',150)+40}px;{OS}font-size:32px;font-weight:600;line-height:1.25;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.7)">{d.get('under','')}</div>
<div style="position:absolute;left:40px;right:40px;bottom:52px;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid rgba(243,239,232,.3);padding-top:20px;color:#F3EFE8;font-size:20px;letter-spacing:.12em;font-weight:600"><span style="opacity:.75">PRZESUŃ, BY PRZECZYTAĆ  →</span><span>SOLYSOL.PL</span></div>"""
    return page(h).replace('<style>','<style>'+FX,1)

data=json.load(open(sys.argv[1]))
os.makedirs('html',exist_ok=True)
fbsrc=open('/home/claude/social/fb/gen_fb.py').read()
pre_fb=fbsrc.split("for k in ['n1','n2','n3','n4']:")[0].split("exec(calls)")[1]
for d in data:
    k=d['id']; P.clear()
    mast_label=d.get('mast','WIADOMOŚCI')
    cover(k,d['photo'],d['pos'],d['desk'],d['head'],d['deck'])
    facts(k,d['ftitle'],d['pts'],d['note'])
    advice(k,d['atitle'],d['steps'],d['src'])
    if d.get('style')=='okladka': P[k+'-1']=okladka(d,DATE)
    for kk,v in P.items():
        v=v.replace('WIADOMOŚCI · 16.11.2026',f'{mast_label} · {DATE}')
        open(f'html/{kk}.html','w').write(v)
    # FB
    D={k:dict(photo=d['photo'],pos=d['pos'],desk=d['desk'],head=d['head'],pts=d['pts'],steps=d['steps'])}
    ns={'D':D,'P':{},**{n:globals()[n] for n in ['page','tag','kick','CG','INK','IV','ORG','ORL','CR']}}
    exec(pre_fb,ns)
    PF=ns['P']; fbhead=ns['fbhead']; fbfoot=ns['fbfoot']
    dd=D[k]
    ph=''.join(f'<div style="display:grid;grid-template-columns:190px 1fr;gap:22px;padding:22px 0;border-top:1.5px solid #D9CFBF;align-items:center"><span style="{CG}font-size:{48 if len(a)<7 else 38}px;font-weight:600;color:{ORG};line-height:1">{a}</span><div><div style="font-size:25px;font-weight:600;line-height:1.2">{b}</div><div style="font-size:20px;color:#5A534A;margin-top:3px">{c}</div></div></div>' for a,b,c in dd['pts'])
    st=''.join(f'<div style="display:flex;gap:14px;font-size:21px;line-height:1.35;padding:5px 0"><span style="color:{ORL};{CG}font-size:26px;flex:none;width:20px">{i+1}</span><span>{s}</span></div>' for i,s in enumerate(dd['steps'][:3]))
    h=page(f'''{fbhead(dd)}
<div style="position:absolute;left:64px;right:64px;top:552px"><div style="border-bottom:1.5px solid #D9CFBF">{ph}</div></div>
<div style="position:absolute;left:64px;right:64px;bottom:104px;background:{INK};color:{IV};padding:22px 28px">
<div style="font-size:16px;font-weight:700;letter-spacing:.18em;color:{ORL};margin-bottom:6px">{d.get('fbbox','CO ZROBIĆ')}</div>{st}</div>
{fbfoot()}''',IV,INK).replace('WIADOMOŚCI · 16.11.2026',f'{mast_label} · {DATE}').replace("'NARZEKALNIA' if","'NARZEKALNIA' if")
    open(f'html/{k}-fb.html','w').write(h)
print('ok')
