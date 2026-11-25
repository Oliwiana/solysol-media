F='file:///home/claude/tools/node_modules/@fontsource/inter/files/'
css=f'''
@font-face{{font-family:CG;src:url(package/files/cormorant-garamond-latin-ext-700-normal.woff2)}}
@font-face{{font-family:CG;src:url(package/files/cormorant-garamond-latin-700-normal.woff2)}}
@font-face{{font-family:CGi;src:url(package/files/cormorant-garamond-latin-ext-700-italic.woff2)}}
@font-face{{font-family:CGi;src:url(package/files/cormorant-garamond-latin-700-italic.woff2)}}
''' + ''.join(f"@font-face{{font-family:I;font-weight:{w};src:url({F}inter-latin-ext-{w}-normal.woff2)}}@font-face{{font-family:I;font-weight:{w};src:url({F}inter-latin-{w}-normal.woff2)}}" for w in (400,500,600,700,800,900)) + '''
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:#120d22;color:#FAF7F2;font-family:I;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(70% 55% at 85% 8%,rgba(155,89,196,.55),transparent 70%),radial-gradient(60% 50% at 0% 100%,rgba(60,31,85,.7),transparent 70%),linear-gradient(180deg,#1a1233,#0E1B2C)}
.grain{position:absolute;inset:0;opacity:.18;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter><rect width='300' height='300' filter='url(%23n)' opacity='.9'/></svg>")}
.ghost{position:absolute;font:700 560px/0.8 CG;color:rgba(199,155,230,.07);letter-spacing:-.02em;white-space:nowrap}
.hd{position:absolute;top:40px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;padding-bottom:16px;border-bottom:1px solid rgba(255,255,255,.28);font-weight:600;font-size:19px;letter-spacing:.24em;color:#efe8f5}
.mast{position:absolute;top:92px;left:0;right:0;text-align:center;font:700 76px/1 CG;letter-spacing:.16em}.mast small{display:block;font-weight:600;font-family:I;font-size:15px;letter-spacing:.5em;color:#cdbfdc;margin-top:12px}
.mast.big{top:96px;font-size:150px;letter-spacing:.12em}.mast.big small{font-size:21px;margin-top:18px}
.tape{position:absolute;background:#F2C14E;color:#161412;padding:16px 26px 18px;box-shadow:0 10px 24px rgba(0,0,0,.45)}.tape small{display:inline-block;background:#161412;color:#F2C14E;font-weight:800;font-size:15px;letter-spacing:.14em;padding:4px 10px;margin-bottom:8px}.tape b{display:block;font-weight:900;font-style:italic;font-size:42px;line-height:1.02;text-transform:uppercase}
.badge{position:absolute;width:230px;height:230px;border-radius:50%;background:#7A3E9D;border:4px dashed #F2C14E;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;box-shadow:0 12px 30px rgba(0,0,0,.45)}.badge span{font-weight:800;font-size:17px;letter-spacing:.2em}.badge b{font:700 92px/1 CG}
.ibox{position:absolute;border-left:5px solid #F2C14E;background:rgba(14,27,44,.82);padding:16px 26px 18px}.ibox span{font-weight:800;font-size:17px;letter-spacing:.24em;color:#F2C14E}.ibox b{display:block;font:700 46px CG;margin-top:4px}
.kick{font-weight:700;font-size:19px;letter-spacing:.32em;color:#F2C14E;text-transform:uppercase}
.cols3{position:absolute;left:64px;right:64px;bottom:118px;display:flex;border-top:1px solid rgba(255,255,255,.28);padding-top:26px}.cols3 div{flex:1;text-align:center}.cols3 span{display:block;font-weight:800;font-size:18px;letter-spacing:.2em;color:#F2C14E}.cols3 b{display:block;font:700 40px CG;margin-top:6px}
.wm{font:700 40px CG;letter-spacing:.16em}.wm i{font-family:CGi;color:#C79BE6;letter-spacing:0;margin:0 4px}
.hr{font-weight:700;font-size:17px;letter-spacing:.26em;color:#cdbfdc}
.tag{display:inline-flex;align-items:center;gap:12px;font-weight:800;font-size:20px;letter-spacing:.26em;color:#F2C14E;text-transform:uppercase}
.tag:before{content:"";width:44px;height:3px;background:#F2C14E}
.k{font-family:CGi;color:#E3B6FF}
h1{font:700 118px/0.98 CG;letter-spacing:-.005em}
h2{font:700 92px/1.0 CG}
.lead{font-weight:500;font-size:37px;line-height:1.42;color:#e9e3ef}
.ft{position:absolute;left:72px;right:72px;bottom:48px;display:flex;justify-content:space-between;align-items:flex-end;gap:30px}
.src{font-weight:400;font-size:15px;line-height:1.4;color:#9a8cad;max-width:720px}
.dots{display:flex;gap:7px}.dots i{width:22px;height:4px;background:rgba(255,255,255,.22);border-radius:2px}.dots i.on{background:#C79BE6;width:40px}
.row{display:flex;gap:34px;padding:28px 0;border-top:1px solid rgba(255,255,255,.14)}
.row .d{width:190px;flex:none;font:700 52px/1 CG;color:#C79BE6}
.row b{display:block;font-weight:700;font-size:34px;line-height:1.25}
.row span{display:block;font-weight:400;font-size:29px;line-height:1.4;color:#cfc6da;margin-top:4px}
.card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:22px;padding:34px 38px}
.num{font:700 76px/1 CG;color:#C79BE6}
.pill{display:inline-block;border:2px solid #C79BE6;color:#fff;border-radius:999px;padding:10px 24px;font-weight:700;font-size:26px}
'''
open('s.css','w').write(css)
N=10
CATS={1:'DZIŚ',2:'HISTORIA',3:'ONZ',4:'MARBELLA',5:'POMOC',6:'POMOC',7:'POMOC',8:'WARTO WIEDZIEĆ',9:'WYBRZEŻE',10:'SOL Y SÓL'}
def page(i,body,src='',ghost='',gpos='right:-40px;top:160px'):
    cat=CATS[i]
    dots=''.join(f'<i class="{"on" if j==i else ""}"></i>' for j in range(1,N+1))
    g=f'<div class=ghost style="{gpos}">{ghost}</div>' if ghost else ''
    return f'''<html><head><meta charset=utf-8><link rel=stylesheet href=s.css></head><body><div class=bg></div>{g}<div class=grain></div>
<div class=hd><span>{cat}</span><span>25.11.2026</span><span>SOLYSOL.PL</span></div>
<div class="mast{' big' if i==1 else ''}">SOL Y SÓL<small>COSTA DEL SOL PO POLSKU</small></div>
{body}
<div class=ft><div class=src>{src}</div><div class=dots>{dots}</div></div></body></html>'''
P={}
P[1]=page(1,'''<div class=ibox style="left:64px;top:450px"><span>MARBELLA · DZIŚ</span><b>11:00 – minuta ciszy</b></div>
<div class=tape style="left:58px;top:585px;transform:rotate(-3deg)"><small>POMOC 24 H</small><b>016 – bezpłatnie<br>i poufnie</b></div>
<div class=badge style="right:70px;top:470px;transform:rotate(8deg)"><span>ODCINEK</span><b>6</b><span style="border-top:2px solid #fff;padding-top:6px;margin-top:4px">PRZESUŃ →</span></div>
<div style="position:absolute;left:64px;right:64px;top:770px;text-align:center"><div class=kick>25 listopada · dzień międzynarodowy</div>
<h1 style="margin-top:22px;font-size:104px">Dzień przeciw <span class=k>przemocy<br>wobec kobiet</span></h1>
<p class=lead style="margin-top:20px;font-size:29px">Skąd ta data i gdzie szukać pomocy – także bez hiszpańskiego</p></div>
<div class=cols3><div><span>1960</span><b>Siostry Mirabal</b></div><div><span>16 DNI</span><b>do 10 grudnia</b></div><div><span>WARTO WIEDZIEĆ</span><b>Punto Violeta</b></div></div>''',
'')
P[2]=page(2,'''<div style="position:absolute;left:72px;right:72px;top:370px">
<div class=tag>Skąd ta data?</div><h2 style="margin-top:26px">Las <span class=k>Mariposas</span></h2>
<p class=lead style="margin-top:18px;font-size:31px">Tak nazywano siostry Mirabal – opozycjonistki wobec dyktatury Trujillo na Dominikanie.</p>
<div style="margin-top:34px">
<div class=row><div class=d>1960</div><div><b>25 listopada</b><span>Patria, Minerva i María Teresa Mirabal giną z rąk reżimu.</span></div></div>
<div class=row><div class=d>1981</div><div><b>Bogota</b><span>Aktywistki z Ameryki Łacińskiej ogłaszają 25.11 dniem walki z przemocą wobec kobiet.</span></div></div>
<div class=row style="border-bottom:1px solid rgba(255,255,255,.14)"><div class=d>1999</div><div><b>ONZ</b><span>Zgromadzenie Ogólne ustanawia Międzynarodowy Dzień (rezolucja 54/134).</span></div></div>
</div></div>''','Źródła: ONZ / UNESCO, Amnesty International, CNN, Diario Libre',ghost='1960',gpos='right:-60px;top:900px;font-size:380px')
P[3]=page(3,'''<div style="position:absolute;left:72px;right:72px;top:320px">
<div class=tag>Kampania ONZ</div>
<div style="font:700 380px/0.85 CG;color:#C79BE6;margin-top:30px">16<span style="font-size:120px;color:#FAF7F2"> dni</span></div>
<h2 style="margin-top:20px;font-size:76px">akcji przeciw przemocy <span class=k>wobec kobiet</span></h2>
<div style="margin-top:110px;position:relative;height:140px">
<div style="position:absolute;left:0;right:0;top:40px;height:4px;background:linear-gradient(90deg,#C79BE6,#9B59C4)"></div>
<div style="position:absolute;left:0;top:26px;width:32px;height:32px;border-radius:50%;background:#C79BE6"></div>
<div style="position:absolute;right:0;top:26px;width:32px;height:32px;border-radius:50%;background:#9B59C4"></div>
<div style="position:absolute;left:0;top:76px;font-weight:800;font-size:34px">25.11<span style="display:block;font-weight:400;font-size:22px;color:#cfc6da">dziś – start</span></div>
<div style="position:absolute;right:0;top:76px;text-align:right;font-weight:800;font-size:34px">10.12<span style="display:block;font-weight:400;font-size:22px;color:#cfc6da">Dzień Praw Człowieka</span></div>
</div></div>''','Źródła: El Nuevo Diario, Acento (za ONZ)')
P[4]=page(4,'''<div style="position:absolute;left:72px;right:72px;top:310px">
<div class=tag>Marbella · dziś</div>
<div style="font:700 300px/0.9 CG;color:#C79BE6;margin-top:30px">11:00</div>
<h2 style="font-size:80px;margin-top:10px">Hospital Real <span class=k>de la Misericordia</span></h2>
<p class=lead style="margin-top:16px">Stare miasto Marbelli.</p>
<div style="display:flex;gap:18px;margin-top:70px"><span class=pill style="font-size:32px;padding:14px 30px">minuta ciszy</span><span class=pill style="font-size:32px;padding:14px 30px">odczytanie manifestu</span></div></div>''','Źródła: La Noción, Euro Weekly News')
P[5]=page(5,'''<div style="position:absolute;left:72px;right:72px;top:370px">
<div class=tag>Gdzie szukać pomocy</div>
<div style="display:flex;align-items:flex-end;gap:30px;margin-top:20px"><div style="font:700 260px/0.85 CG;color:#C79BE6">016</div><div style="font-weight:700;font-size:30px;line-height:1.35;padding-bottom:22px">bezpłatnie · poufnie<br>24 h, 7 dni w tygodniu</div></div>
<div style="margin-top:30px">
<div class=row><div class=d style="font-size:34px;width:200px">WhatsApp</div><div><b>600 000 016</b><span>tylko wiadomości</span></div></div>
<div class=row><div class=d style="font-size:34px;width:200px">e-mail</div><div><b>016-online@igualdad.gob.es</b></div></div>
<div class=row><div class=d style="font-size:34px;width:200px">czat</div><div><b>violenciagenero.igualdad.gob.es</b></div></div>
<div class=row style="border-bottom:1px solid rgba(255,255,255,.14)"><div class=d style="font-size:34px;width:200px">ślad</div><div><b>Nie widać go na rachunku</b><span>numer usuń z historii połączeń</span></div></div>
</div></div>''','Źródła: La Moncloa (Ministerio de Igualdad), Maldita, Público')
P[6]=page(6,'''<div style="position:absolute;left:72px;right:72px;top:370px">
<div class=tag>Martwisz się o kogoś?</div>
<h2 style="margin-top:26px;font-size:110px">016 jest też <span class=k>dla bliskich</span></h2>
<p class=lead style="margin-top:20px">Zadzwonić może rodzina, przyjaciółka czy sąsiad – żeby dowiedzieć się, jak pomóc.</p>
<div style="display:flex;gap:24px;margin-top:50px">
<div class=card style="flex:1"><div class=num>53</div><div style="font-weight:700;font-size:28px;margin-top:10px">języki</div><div style="font-size:24px;color:#cfc6da;margin-top:6px">nie musisz znać hiszpańskiego</div></div>
<div class=card style="flex:1"><div class=num>§</div><div style="font-weight:700;font-size:28px;margin-top:10px">porady prawne</div><div style="font-size:24px;color:#cfc6da;margin-top:6px">konsultantki doradzą</div></div>
<div class=card style="flex:1;background:rgba(199,155,230,.16);border-color:#C79BE6"><div class=num>112</div><div style="font-weight:700;font-size:28px;margin-top:10px">zagrożenie teraz</div><div style="font-size:24px;color:#cfc6da;margin-top:6px">dzwoń od razu</div></div>
</div></div>''','Źródła: La Moncloa (Ministerio de Igualdad), Maldita, Público',ghost='016',gpos='right:-40px;top:880px;font-size:420px')
P[7]=page(7,'''<div style="position:absolute;left:72px;right:72px;top:310px">
<div class=tag>Nie możesz zadzwonić?</div>
<h2 style="margin-top:26px">Aplikacja <span class=k>AlertCops</span></h2>
<p class=lead style="margin-top:20px">Bezpłatna aplikacja policji. Przycisk <b>SOS</b> wysyła alarm razem z Twoją lokalizacją.</p>
<div style="margin-top:44px">
<div class=row><div class=d>112</div><div><b>Nagły wypadek</b><span>zagrożenie życia</span></div></div>
<div class=row><div class=d>091</div><div><b>Policía Nacional</b></div></div>
<div class=row style="border-bottom:1px solid rgba(255,255,255,.14)"><div class=d>062</div><div><b>Guardia Civil</b></div></div>
</div></div>''','Źródła: La Moncloa, Konsulat Kolumbii w Walencji, Uniwersytet w Grenadzie (VIICS)',ghost='SOS',gpos='right:-30px;top:860px;font-size:400px')
P[8]=page(8,'''<div style="position:absolute;left:72px;right:72px;top:370px">
<div class=tag>Warto wiedzieć</div>
<h2 style="margin-top:26px;font-size:120px">Punto <span class=k>Violeta</span></h2>
<p class=lead style="margin-top:20px">Fioletowa naklejka z kodem QR oznacza bezpieczne miejsce: tu kobieta może poprosić o wsparcie i dostanie informacje o pomocy – poufnie.</p>
<div style="display:flex;gap:24px;margin-top:46px">
<div class=card style="flex:1"><div class=num>2021</div><div style="font-size:26px;color:#cfc6da;margin-top:10px">sieć tworzy Ministerio de Igualdad</div></div>
<div class=card style="flex:1.4"><div class=num style="font-size:44px">Gdzie?</div><div style="font-size:26px;color:#cfc6da;margin-top:10px">m.in. urzędy Seguridad Social i hotele Paradores</div></div>
</div>
<p style="margin-top:36px;font-weight:700;font-size:28px;color:#C79BE6">Zobaczysz naklejkę? Tam możesz poprosić o pomoc.</p></div>''','Źródła: La Moncloa, Ministerio de Igualdad, Ministerio de Hacienda, Revista Seguridad Social')
P[9]=page(9,'''<div style="position:absolute;left:72px;right:72px;top:370px">
<div class=tag>Co jeszcze dziś</div>
<h2 style="margin-top:22px;font-size:84px">Na wybrzeżu <span class=k>25.11</span></h2>
<div style="margin-top:26px">
<div class=row><div class=d>18°</div><div><b>Pogoda – częściowe zachmurzenie</b><span>od dziś front chłodny, nocą ok. 9°C</span></div></div>
<div class=row><div class=d>Mijas</div><div><b>Targ uliczny w La Cala</b><span>Recinto Ferial</span></div></div>
<div class=row><div class=d>26.11</div><div><b>Jarmark świąteczny</b><span>Fuengirola, Pl. de la Constitución</span></div></div>
<div class=row><div class=d>26–29.11</div><div><b>Open de España – golf kobiet</b><span>Mijas, La Cala Resort</span></div></div>
<div class=row style="border-bottom:1px solid rgba(255,255,255,.14)"><div class=d>27–28.11</div><div><b>Świąteczne światła</b><span>Marbella i San Pedro Alcántara</span></div></div>
</div></div>''','Źródła: AEMET, Diario Sur, La Opinión de Málaga, Marbella Directo')
P[10]=page(10,'''<div style="position:absolute;left:72px;right:72px;top:400px">
<h1 style="font-size:130px">To wszystko<br><span class=k>na dziś.</span></h1>
<p class=lead style="margin-top:34px">Wieczorem o 19:00 – kolejne wydanie.<br>Szczegóły każdej wiadomości – na <b>solysol.pl</b></p>
<div class=card style="margin-top:60px;display:flex;align-items:center;gap:30px;background:rgba(199,155,230,.14);border-color:#C79BE6">
<div style="font:700 90px/1 CG;color:#C79BE6">016</div><div style="font-weight:700;font-size:30px;line-height:1.35">Udostępnij ten post.<br><span style="font-weight:500;color:#cfc6da">Może komuś pomóc.</span></div></div>
<div style="margin-top:50px;font-weight:800;font-size:22px;letter-spacing:.22em;color:#cdbfdc">ZAPISZ · UDOSTĘPNIJ · OBSERWUJ @SOLYSOL.PL</div></div>''','',ghost='SOL',gpos='right:-80px;top:880px;font-size:440px')
for i,h in P.items(): open(f'p{i}.html','w').write(h)
