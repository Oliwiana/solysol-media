import sys,subprocess
sys.path.insert(0,'/tmp/kb'); import board
F='file:///home/claude/tools/node_modules/@fontsource'
H={2:('la-consula-churriana/01','La Cónsula · 1959','Na urodziny <b>Hemingwaya</b> przyjechała <b>straż pożarna</b>'),
   3:('hotel-pez-espada-torremolinos/03','Pez Espada · 1959','<b>Sinatra</b>, Ava Gardner, Sophia Loren – <b>jeden hotel</b>'),
   4:('teatro-del-soho-malaga/01','Teatro del Soho · Malaga','Gwiazda Hollywood, która <b>co roku wraca</b> do Malagi'),
   5:('malaga-port-19th-century/06','Malaga · 1862','Autor „Brzydkiego kaczątka” był <b>najszczęśliwszy</b> w Maladze')}
for n in map(int,sys.argv[1:]):
    f,cap,txt=H[n]; board.prep(f,f'/tmp/g/r{n}/img/hookp.jpg')
    html=f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>
@font-face{{font-family:T;src:url({F}/special-elite/files/special-elite-latin-ext-400-normal.woff2)}}@font-face{{font-family:T;src:url({F}/special-elite/files/special-elite-latin-400-normal.woff2)}}
@font-face{{font-family:I;font-weight:900;src:url({F}/inter/files/inter-latin-ext-900-normal.woff2)}}@font-face{{font-family:I;font-weight:900;src:url({F}/inter/files/inter-latin-900-normal.woff2)}}
@font-face{{font-family:CG;font-weight:600;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-ext-600-normal.woff2)}}@font-face{{font-family:CG;font-weight:600;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2)}}
body{{margin:0;width:1080px;height:1920px;background:#2a1e14;position:relative;overflow:hidden;font-family:I}}
body:before{{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}}
.p{{position:absolute;left:110px;top:330px;width:860px;padding:28px 28px 104px;box-sizing:border-box;background:#efe6d2;transform:rotate(-2.5deg);box-shadow:6px 14px 30px rgba(0,0,0,.6)}}
.p img{{width:100%;display:block;filter:contrast(1.05) sepia(.12)}}.p div{{position:absolute;left:34px;bottom:30px;font-family:T;font-size:42px}}
.pin{{position:absolute;width:30px;height:30px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);left:50%;top:-14px;margin-left:-15px;box-shadow:2px 4px 6px rgba(0,0,0,.6)}}
.h{{position:absolute;left:70px;right:70px;top:1190px;color:#efe6d2;font-weight:900;font-size:90px;line-height:1.08;text-transform:uppercase}}.h b{{color:#F6C343}}
.t{{position:absolute;left:70px;top:1095px;background:#F6C343;color:#171513;font-weight:900;font-size:34px;padding:10px 22px;letter-spacing:.06em;transform:rotate(-2deg)}}
.s{{position:absolute;right:90px;top:250px;color:#c0281b;border:8px solid;border-radius:8px;padding:6px 24px;font-weight:900;font-size:50px;transform:rotate(9deg);background:rgba(239,230,210,.9)}}
.top{{position:absolute;left:64px;top:62px;color:#efe6d2;font-family:CG;font-weight:600;font-size:40px;letter-spacing:.08em}}.top i{{color:#F6C343}}
#vig{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 50%,rgba(0,0,0,.75) 100%)}}
</style></head><body><div class=p><div class=pin></div><img src="img/hookp.jpg"><div>{cap}</div></div>
<div class=s>ODC. {n}</div><div class=t>GWIAZDY NA COSTA DEL SOL</div><div class=h>{txt}</div><div id=vig></div><div class=top>SOL <i>y</i> SÓL</div></body></html>'''
    open(f'/tmp/g/r{n}/hook.html','w').write(html)
    subprocess.run(['google-chrome','--headless','--no-sandbox','--allow-file-access-from-files','--hide-scrollbars','--window-size=1080,1920',f'--screenshot=/tmp/g/r{n}/hook.png',f'file:///tmp/g/r{n}/hook.html'],capture_output=True)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'/tmp/g/r{n}/hook.png','-q:v','3',f'/tmp/g/r{n}/hook.jpg'])
    print(n,'ok')
