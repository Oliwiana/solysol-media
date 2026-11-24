import subprocess,sys,html
F='file:///home/claude/tools/node_modules/@fontsource'
def ff(fam,pkg,w,st='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{pkg}/files/{pkg}-{s}-{w}-{st}.woff2)}}" for s in ('latin','latin-ext'))
FONTS=ff('CG','cormorant-garamond',600)+ff('CG','cormorant-garamond',600,'italic')+ff('IN','inter',600)+ff('IN','inter',800)+ff('IX','inter',900,'italic')
D={
2:dict(p='la-consula-churriana/01',pos='50% 45%',k='GWIAZDY NA COSTA DEL SOL · ODC. 2',d='05.12.2026',t='Urodziny Hemingwaya',i='i straż pożarna',s='La Cónsula pod Malagą, lato 1959',bl='ROK',bv='1959',sl='FAJERWERKI',sv='PODPALIŁY PALMĘ',f=[('1959','Algeciras'),('21.07','60. urodziny'),('1985','„Niebezpieczne lato”')],cr='Fot. Daniel Capilla / Wikimedia Commons, CC BY-SA 4.0'),
3:dict(p='hotel-pez-espada-torremolinos/03',pos='50% 40%',k='GWIAZDY NA COSTA DEL SOL · ODC. 3',d='12.12.2026',t='Pez Espada –',i='hotel gwiazd',s='Sinatra, Sophia Loren i Torremolinos lat 60.',bl='OTWARCIE',bv='31.05.1959',sl='6 LAT PÓŹNIEJ',sv='PONAD 50 HOTELI',f=[('5 ★','pierwszy w mieście'),('1964','Sinatra'),('El Chorro','plan filmowy')],cr='Fot. Biblioteca Fac. Empresa y Gestión Pública, Univ. de Zaragoza / Wikimedia Commons, CC BY-SA 2.0'),
4:dict(p='teatro-del-soho-malaga/01',pos='50% 45%',k='GWIAZDY NA COSTA DEL SOL · ODC. 4',d='19.12.2026',t='Banderas',i='i jego Malaga',s='Hollywood, własny teatr i Niedziela Palmowa',bl='TEATR',bv='15.11.2019',sl='CO ROKU',sv='WRACA NA PROCESJĘ',f=[('1982','Almodóvar'),('2019','Teatro del Soho'),('20+ lat','Lágrimas y Favores')],cr='Fot. Daniel Capilla / Wikimedia Commons, CC BY-SA 4.0'),
5:dict(p='malaga-port-19th-century/06',pos='50% 50%',k='GWIAZDY NA COSTA DEL SOL · ODC. 5',d='26.12.2026',t='Andersen',i='najszczęśliwszy w Maladze',s='Autor „Brzydkiego kaczątka”, jesień 1862',bl='KSIĄŻKA',bv='„W Hiszpanii”',sl='DZIŚ',sv='POMNIK Z BRĄZU',f=[('1862','statkiem do Malagi'),('La Manquita','katedra'),('1863','„W Hiszpanii”')],cr='Ryc. Gustave Doré / Wikimedia Commons, domena publiczna'),
}
def page(c,H=1920):
    off=(H-1350)//2  # 3:4 safe area centred
    e=html.escape
    facts=''.join(f'<div style="flex:1;text-align:center"><div style="font-size:16px;font-weight:800;letter-spacing:.2em;color:#F2C14E">{e(a)}</div><div style="font-family:CG;font-size:30px;font-weight:600;line-height:1.12;margin-top:8px">{e(b)}</div></div>' for a,b in c['f'])
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box;margin:0}}html,body{{width:1080px;height:{H}px;overflow:hidden;font-family:IN;background:#0A1422;color:#FAF7F2}}</style></head><body>
<div style="position:absolute;inset:0;background:url('file:///tmp/sm/_photos/commons/{c['p']}.jpg') {c['pos']}/cover;filter:saturate(1.1)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,20,34,.85) 0%,rgba(10,20,34,.55) {12+off/H*100:.0f}%,rgba(10,20,34,.12) 40%,rgba(10,20,34,.45) 58%,rgba(10,20,34,.93) 74%,#0A1422 100%)"></div>
<div style="position:absolute;inset:0;box-shadow:inset 0 0 180px rgba(0,0,0,.45)"></div>
<div style="position:absolute;left:64px;right:64px;top:{off+40}px;text-align:center">
<div style="display:flex;justify-content:space-between;font-size:16px;font-weight:600;letter-spacing:.18em;padding-bottom:12px;border-bottom:1px solid rgba(250,247,242,.5)"><span>GWIAZDY</span><span>{c['d']}</span><span>SOLYSOL.PL</span></div>
<div style="font-family:CG;font-size:140px;font-weight:600;line-height:1;letter-spacing:.1em;margin-top:20px;padding-left:.1em;text-shadow:0 4px 24px rgba(0,0,0,.35)">SOL Y SÓL</div>
<div style="font-size:18px;font-weight:600;letter-spacing:.42em;margin-top:8px;padding-left:.42em">COSTA DEL SOL PO POLSKU</div></div>
<div style="position:absolute;left:64px;top:{off+440}px"><div style="background:rgba(12,24,40,.74);border-left:5px solid #F2C14E;padding:16px 22px 18px;margin-bottom:16px;width:400px"><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:#F2C14E">{e(c['bl'])}</div><div style="font-family:CG;font-size:40px;font-weight:600;line-height:1.08;margin-top:6px">{e(c['bv'])}</div></div>
<div style="background:#F2C14E;color:#171513;padding:14px 20px 16px;width:400px;transform:rotate(-2deg);box-shadow:0 14px 30px rgba(0,0,0,.45)"><div style="display:inline-block;background:#171513;color:#F2C14E;font-size:13px;font-weight:800;letter-spacing:.18em;padding:4px 10px">{e(c['sl'])}</div><div style="font-family:IX;font-style:italic;font-weight:900;font-size:34px;line-height:1.02;letter-spacing:-.02em;margin-top:8px">{e(c['sv'])}</div></div></div>
<div style="position:absolute;right:58px;top:{off+470}px;width:230px;height:230px;border-radius:50%;background:#C62828;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:0 10px 30px rgba(0,0,0,.4);border:3px dashed #F2C14E;text-align:center"><div style="font-size:16px;font-weight:800;letter-spacing:.2em">ODCINEK</div><div style="font-family:CG;font-style:italic;font-size:80px;line-height:.9;margin:2px 0">{c['k'][-1]}</div><div style="width:110px;height:1px;background:rgba(255,255,255,.6);margin:4px 0 6px"></div><div style="font-size:14px;font-weight:800;letter-spacing:.14em">Z DŹWIĘKIEM ▶</div></div>
<div style="position:absolute;left:50px;right:50px;top:{off+780}px;text-align:center">
<div style="font-size:17px;font-weight:600;letter-spacing:.24em;color:#F2C14E">{e(c['k'])}</div>
<div style="font-family:CG;font-size:92px;font-weight:600;line-height:.98;margin-top:12px;text-shadow:0 4px 22px rgba(0,0,0,.55)">{e(c['t'])} <i style="color:#F2C14E">{e(c['i'])}</i></div>
<div style="font-size:24px;margin:18px auto 0;line-height:1.35;max-width:820px;opacity:.92">{e(c['s'])}</div></div>
<div style="position:absolute;left:64px;right:64px;top:{off+1150}px;border-top:1px solid rgba(250,247,242,.45);padding-top:18px;display:flex;gap:30px">{facts}</div>
<div style="position:absolute;left:64px;right:64px;top:{off+1300}px;font-size:12px;opacity:.6;text-align:right">{e(c['cr'])} · zdjęcie ilustracyjne</div>
</body></html>'''
if __name__=="__main__":
 for n in map(int,sys.argv[1:]):
     for H,suf in ((1920,'cover'),):
         open(f'/tmp/g/r{n}/mag.html','w').write(page(D[n],H))
         subprocess.run(['google-chrome','--headless','--no-sandbox','--allow-file-access-from-files','--hide-scrollbars',f'--window-size=1080,{H}',f'--screenshot=/tmp/g/r{n}/mag.png',f'file:///tmp/g/r{n}/mag.html'],capture_output=True)
         subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'/tmp/g/r{n}/mag.png','-q:v','3',f'/tmp/g/r{n}/magcover.jpg'])
     print(n)
 