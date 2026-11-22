import sys
F='file:///home/claude/tools/node_modules/@fontsource'
def ff(fam,path,w,st='normal'): return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{path.replace('X',s)})}}" for s in ('latin','latin-ext'))
FONTS=ff('AN','anton/files/anton-X-400-normal.woff2',400)+ff('CG','cormorant-garamond/files/cormorant-garamond-X-600-italic.woff2',600,'italic')+ff('IN','inter/files/inter-X-800-normal.woff2',800)+ff('IX','inter/files/inter-X-900-italic.woff2',900,'italic')
def thumb(photo,pos,l1,l2,box,seal,ep):
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{margin:0;box-sizing:border-box}}body{{width:1280px;height:720px;overflow:hidden;background:#0A1422;font-family:IN}}</style></head><body>
<div style="position:absolute;inset:0;background:url('file:///home/claude/photos_raw/{photo}') {pos}/cover;filter:saturate(1.3) contrast(1.05)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,16,30,.95) 0%,rgba(8,16,30,.8) 42%,rgba(8,16,30,.1) 75%)"></div>
<div style="position:absolute;left:0;top:0;bottom:0;width:14px;background:#F2C14E"></div>
<div style="position:absolute;left:56px;top:44px;font-family:IN;font-weight:800;font-size:22px;letter-spacing:.2em;color:#F2C14E">ZAGADKI COSTA DEL SOL · {ep}</div>
<div style="position:absolute;left:52px;top:90px;width:760px;font-family:AN;font-size:118px;line-height:.98;color:#fff;text-transform:uppercase;text-shadow:0 6px 24px rgba(0,0,0,.6)">{l1}</div>
<div style="position:absolute;left:56px;top:{90+2*116+10}px;font-family:CG;font-style:italic;font-size:84px;color:#F2C14E;line-height:1;text-shadow:0 4px 18px rgba(0,0,0,.7)">{l2}</div>
<div style="position:absolute;left:56px;bottom:56px;background:#F2C14E;color:#111;padding:12px 22px;transform:rotate(-2deg);font-family:IX;font-style:italic;font-weight:900;font-size:46px;text-transform:uppercase;box-shadow:0 12px 30px rgba(0,0,0,.5)">{box}</div>
<div style="position:absolute;right:60px;top:60px;width:210px;height:210px;border-radius:50%;background:#C62828;border:4px dashed #F2C14E;transform:rotate(10deg);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,.5)">
<div style="font-weight:800;font-size:18px;letter-spacing:.2em">{seal[0]}</div><div style="font-family:CG;font-style:italic;font-size:40px;line-height:1.05;margin:4px 0">{seal[1]}</div><div style="font-weight:800;font-size:16px;letter-spacing:.16em">{seal[2]}</div></div>
<div style="position:absolute;right:40px;bottom:30px;font-family:IN;font-weight:800;font-size:26px;letter-spacing:.1em;color:#fff">SOL <span style="color:#F2C14E">y</span> SÓL</div>
</body></html>"""
open('t1.html','w').write(thumb('banus.jpg','60% 50%','James Bond<br>kontra','Marbella','72 apartamenty zamiast willi',['AFERA','Goldfinger','ŚLEDZTWO'],'ODC. 1'))
E=[('02','mrb_ayto4.jpg','50% 50%','Dzień bez<br>burmistrza','Afera Malaya','Rada miasta rozwiązana',['ROK','2006','MARBELLA']),
('03','villa3.jpg','50% 50%','Książę<br>Marbelli','al-Kassar','Handlarz bronią w willi',['ODC.','kryminał','PRAWDZIWY']),
('04','sun0.jpg','50% 50%','Costa<br>del Crime','gangsterzy z Anglii','Raj dla zbiegów',['LATA','70–80','BEZ EKSTRADYCJI']),
('05','ban2.jpg','50% 60%','Noc otwarcia<br>Puerto Banús','1970','Gwiazdy w jednym porcie',['GOŚCIE','z Hollywood','I KSIĄŻĘTA']),
('06','x_palacio_mrb.jpg','50% 50%','Król Fahd<br>i Marbella','saudyjski pałac','Miliony w mieście',['LATA','80.','MARBELLA']),
('07','mrb0.jpg','50% 50%','Jesús Gil<br>i Marbella','jego królestwo','Władza bez granic',['BURMISTRZ','1991–2002','MARBELLA']),
('08','mrb3.jpg','50% 50%','Miłość,<br>władza','i wyrok','Pantoja i Muñoz',['SPRAWA','Malaya','CZ. 2']),
('09','mrbaer.jpg','50% 50%','Ballena<br>Blanca','pralnia pieniędzy','Pieniądze z całego świata',['ROK','2005','ŚLEDZTWO']),
('10','villa4.jpg','50% 50%','Król<br>jet setu','Adnan Khashoggi','Jacht, przyjęcia, Marbella',['LATA','80.','JET SET']),
('11','port.jpg','50% 50%','Nocne łodzie<br>w Cieśninie','narcolanchas','Przemyt nocą',['DZIŚ','Gibraltar','CIEŚNINA'])]
for n,ph,pos,l1,l2,box,seal in E:
    open(f'z{n}.html','w').write(thumb(ph,pos,l1,l2,box,seal,'ODC. '+str(int(n))))
