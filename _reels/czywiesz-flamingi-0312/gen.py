import json,re
SH=json.load(open('shots.json')); PH=json.load(open('phr.json'))
LB=['','']+['zdjęcie ilustracyjne']*29
for i in (4,6,7,8,26): LB[i]='Laguna Fuente de Piedra'
LB[5]='El Torcal · okolice Antequery'; LB[3]='mapa · Europa'; LB[23]='mapa · Morze Śródziemne'
LB[20]=LB[21]='zdjęcie ilustracyjne · obrączkowanie'
P='paper'
C=[
 dict(a=3.5,b=4.25,cls='stamp',css='left:300px;top:620px;color:#c0281b;font-size:80px',r=-8,s0=2,h='NIE AFRYKA'),
 dict(a=4.4,b=5.75,cls='tag',css='left:360px;top:880px',r=-4,h='MÁLAGA · ANDALUZJA'),
 dict(a=5.9,b=7.55,cls=P,pin=1,css='left:80px;top:860px;width:560px',r=-2,h='<div style="font-size:30px;opacity:.7">laguna · prowincja Malaga</div><div class=big style="font-size:62px;margin-top:8px">FUENTE<br>DE PIEDRA</div>'),
 dict(a=7.7,b=8.7,cls='tag',css='left:440px;top:700px',r=3,h='→ ANTEQUERA'),
 dict(a=9.0,b=13.15,cls=P,pin=1,css='left:90px;top:840px;width:520px;text-align:center',r=-3,h='<div class=big style="font-size:110px">≈1400</div><div style="font-size:36px">hektarów · największa<br>laguna Andaluzji</div>'),
 dict(a=13.4,b=15.4,cls=P,pin=1,css='left:440px;top:860px;width:440px;text-align:center',r=3,h='<div class=big style="font-size:110px">~0,5 m</div><div style="font-size:34px">tyle zwykle ma wody</div>'),
 dict(a=15.6,b=18.0,cls=P,pin=1,css='left:90px;top:840px;width:500px;text-align:center',r=-2,h='<div style="font-size:34px">marzec 2026</div><div class=big style="font-size:120px;color:#c0281b">101 cm</div>'),
 dict(a=20.2,b=29.45,cls=P,pin=1,css='left:80px;top:800px;width:700px;text-align:center',r=-1.5,s0=1.15,cnt=[35177,3.1],h='<div class="big n" style="font-size:150px">0</div><div style="font-size:38px;margin-top:6px">par lęgowych · wiosna 2026</div>'),
 dict(a=25.0,b=29.45,cls='stamp',css='left:250px;top:700px;color:#c0281b;font-size:62px',r=9,s0=2.2,h='REKORD OD 1984'),
 dict(a=29.7,b=32.5,cls=P,pin=1,css='left:420px;top:840px;width:480px;text-align:center',r=3,h='<div class=big style="font-size:120px">15 500</div><div style="font-size:38px">piskląt</div>'),
 dict(a=32.7,b=35.85,cls=P,pin=1,css='left:90px;top:830px;width:580px;text-align:center;background:#1d1a16;color:#efe6d2',r=-2,h='<div class=big style="font-size:120px;color:#f2e35b">Nr 1</div><div style="font-size:36px">kolonia flamingów<br>na Półwyspie Iberyjskim</div>'),
 dict(a=37.3,b=40.25,cls=P,pin=1,css='left:390px;top:850px;width:510px;text-align:center',r=2.5,h='<div class=big style="font-size:84px">1986 → 2026</div><div style="font-size:36px;margin-top:8px">40 lat obrączkowania</div>'),
 dict(a=40.5,b=42.85,cls=P,pin=1,css='left:90px;top:850px;width:520px;text-align:center',r=-3,h='<div class=big style="font-size:116px">21 000+</div><div style="font-size:34px">piskląt z obrączką</div>'),
 dict(a=43.1,b=47.6,cls=P,pin=1,css='left:460px;top:820px;width:430px;text-align:center',r=3,h='<div class=big style="font-size:130px">23</div><div style="font-size:40px">kraje</div>'),
 dict(a=45.6,b=47.6,cls='tag',css='left:90px;top:1010px;font-size:42px',r=-3,h='GWINEA BISSAU → CYPR'),
 dict(a=47.8,b=51.1,cls=P,pin=1,css='left:90px;top:840px;width:540px;text-align:center',r=-2,h='<div class=big style="font-size:120px">1 / 3</div><div style="font-size:34px">obserwacji – z powrotem<br>w Fuente de Piedra</div>'),
 dict(a=51.25,b=55.45,cls=P,pin=1,css='left:120px;top:880px;width:640px;text-align:center;background:#1d1a16;color:#f2e35b',r=-1.5,h='<div class=big style="font-size:54px;letter-spacing:.04em">ZDANIEM REDAKCJI</div>'),
 dict(a=55.6,b=58.2,cls='tag',css='left:200px;top:930px;font-size:52px',r=-3,h='NAPISZ W KOMENTARZU ↓'),
]
for c in C: c['css']=re.sub(r'top:(\d+)px',lambda m:'top:%dpx'%(int(m.group(1))+60),c['css'])
crs='FOT. WIKIMEDIA COMMONS (CC BY / CC BY-SA / CC0) – AUTORZY W OPISIE · ZDJĘCIA ILUSTRACYJNE OPISANE'
h=open('tpl.html').read().replace('__SH__',json.dumps(SH)).replace('__PH__',json.dumps(PH,ensure_ascii=False)).replace('__LB__',json.dumps(LB,ensure_ascii=False)).replace('__CARDS__',json.dumps(C,ensure_ascii=False)).replace('__CR__',crs)
open('index.html','w').write(h)
