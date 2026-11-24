import subprocess,sys,html,json,os
sys.path.insert(0,'/tmp/g'); from magcov import FONTS
B='/tmp/sm/_photos/commons/'
def cred(f):
    d,fn=f.split('/')
    for c in json.load(open(B+d+'/credits.json')):
        if c['file']==fn+'.jpg': return c['author'].split('\n')[0].replace('This Photo was taken by ','').strip()[:40]+', '+c['license']
D={
'wraki':dict(p='shipwreck-storm-painting-17th-century/03',tag='CZY WIESZ, ŻE… · GIBRALTAR',d='24.12.2026',t='Złoto',i='na dnie cieśniny',s='Sussex, Utopia, Gneisenau –',h='trzy wraki',b='W 1694 r. pod Gibraltarem zatonął okręt, który mógł wieźć nawet 10 ton złota. Nikt go nie wydobył.',n='10 TON',n2='ZŁOTA',n3='NA DNIE?'),
'puente':dict(p='ronda-puente-nuevo/06',tag='CZY WIESZ, ŻE… · RONDA',d='16.12.2026',t='Cela',i='w łuku mostu',s='Legenda',h='kontra fakty',b='Puente Nuevo wisi prawie 100 m nad wąwozem. W komorze nad łukiem było więzienie. A co z legendą?',n='100 M',n2='NAD',n3='PRZEPAŚCIĄ'),
'afryka':dict(p='jebel-musa-morocco/05',tag='CZY WIESZ, ŻE… · ESTEPONA',d='10.12.2026',t='Z plaży',i='widać Afrykę',s='Tylko nie codziennie –',h='oto dlaczego',b='Dżebel Musa ma 842 m i stoi ponad 60 km od Estepony. Znika, gdy przychodzi mgiełka albo calima.',n='842 M',n2='DŻEBEL',n3='MUSA'),
'flamingi':dict(p='phoenicopterus-roseus-fuente-de-piedra/01',tag='CZY WIESZ, ŻE… · FUENTE DE PIEDRA',d='03.12.2026',t='35 177 par',i='flamingów',s='Rekord laguny',h='pod Malagą',b='Najwięcej od 1984 roku. W tym sezonie wykluło się tu 15 500 piskląt.',n='15 500',n2='PISKLĄT',n3='W 2026'),
'liczby':dict(p='estepona-aerial/01',tag='LICZBY MIESIĄCA · COSTA DEL SOL',d='01.12.2026',t='Gdzie ceny',i='rosną najszybciej?',s='To nie Marbella –',h='Estepona',b='Estepona: 5070 €/m², +16,8% w rok. Marbella: 5974 €/m², tylko +3,1%. Dane: Idealista, październik 2026.',n='+16,8%',n2='ESTEPONA',n3='W ROK'),
}
def page(c,H=1920):
    off=(H-1350)//2; e=html.escape; cr=cred(c['p'])
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box;margin:0}}html,body{{width:1080px;height:{H}px;overflow:hidden;font-family:IN;background:#171513;color:#FAF7F2}}</style></head><body>
<div style="position:absolute;left:0;right:0;top:0;height:{off+760}px;background:url('file://{B}{c['p']}.jpg') 50% 50%/cover"></div>
<div style="position:absolute;left:0;right:0;top:0;height:{off+770}px;background:linear-gradient(180deg,rgba(23,21,19,.75) 0%,rgba(23,21,19,.1) {off/H*100+12:.0f}%,rgba(23,21,19,0) 60%,rgba(23,21,19,.85) 92%,#171513 100%)"></div>
<div style="position:absolute;left:70px;right:70px;top:{off+60}px;display:flex;justify-content:space-between;align-items:center;font-size:20px;font-weight:600;letter-spacing:.2em;padding-bottom:18px;border-bottom:1px solid rgba(250,247,242,.4)"><span style="font-family:CG;font-size:38px;letter-spacing:.06em">S<span style="color:#E07B39">●</span>L <i style="color:#E07B39">y</i> SÓL</span><span>{e(c['tag'].split(' · ')[0])} · {c['d']}</span></div>
<div style="position:absolute;right:66px;top:{off+190}px;width:250px;height:250px;border-radius:50%;background:#E07B39;color:#171513;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-6deg);box-shadow:0 12px 30px rgba(0,0,0,.45);outline:3px dashed rgba(255,255,255,.85);outline-offset:-14px;text-align:center"><div style="font-family:IX;font-style:italic;font-weight:900;font-size:{70 if len(c['n'])<6 else 54}px;line-height:.95">{e(c['n'])}</div><div style="font-family:IX;font-style:italic;font-weight:900;font-size:28px;margin-top:6px">{e(c['n2'])}</div><div style="font-size:15px;font-weight:800;letter-spacing:.2em;margin-top:4px">{e(c['n3'])}</div></div>
<div style="position:absolute;right:70px;top:{off+690}px;font-size:16px;opacity:.7">Fot. {e(cr)} / Wikimedia Commons · zdjęcie ilustracyjne</div>
<div style="position:absolute;left:70px;right:70px;top:{off+730}px">
<div style="display:inline-block;background:#E07B39;color:#171513;font-size:22px;font-weight:800;letter-spacing:.2em;padding:10px 20px">{e(c['tag'])}</div>
<div style="font-family:CG;font-size:104px;font-weight:600;line-height:1;margin-top:26px">{e(c['t'])} <i style="color:#E07B39;text-decoration:underline;text-decoration-thickness:4px;text-underline-offset:10px">{e(c['i'])}</i></div>
<div style="font-family:IX;font-style:italic;font-weight:900;font-size:44px;margin-top:24px">{e(c['s'])} <span style="background:#E07B39;color:#171513;padding:0 10px">{e(c['h'])}</span></div>
<div style="font-size:30px;line-height:1.4;margin-top:20px;opacity:.9;max-width:880px">{e(c['b'])}</div></div>
<div style="position:absolute;left:70px;right:70px;top:{off+1270}px;display:flex;justify-content:space-between;font-size:20px;font-weight:600;letter-spacing:.18em;border-top:1px solid rgba(250,247,242,.3);padding-top:20px"><span style="color:#E07B39">▶ OBEJRZYJ Z DŹWIĘKIEM</span><span>SOLYSOL.PL</span></div>
</body></html>'''
os.makedirs('/tmp/g/cw',exist_ok=True)
for k in sys.argv[1:]:
    open(f'/tmp/g/cw/{k}.html','w').write(page(D[k]))
    subprocess.run(['google-chrome','--headless','--no-sandbox','--allow-file-access-from-files','--hide-scrollbars','--window-size=1080,1920',f'--screenshot=/tmp/g/cw/{k}.png',f'file:///tmp/g/cw/{k}.html'],capture_output=True)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'/tmp/g/cw/{k}.png','-q:v','3',f'/tmp/g/cw/{k}.jpg']); print(k)
