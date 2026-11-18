import os
F='/home/claude/tools/node_modules/@fontsource/'
ff=''
for w in (500,600,700):
  for st in ('normal','italic'):
    for sub in ('latin','latin-ext'):
      ff+=f"@font-face{{font-family:'CG';font-weight:{w};font-style:{st};src:url(file://{F}cormorant-garamond/files/cormorant-garamond-{sub}-{w}-{st}.woff2)}}\n"
for w in (400,500,600,700):
  for sub in ('latin','latin-ext'):
    ff+=f"@font-face{{font-family:Inter;font-weight:{w};src:url(file://{F}inter/files/inter-{sub}-{w}-normal.woff2)}}\n"
INK='#171513'; IV='#F6F1E8'; ORG='#C8692E'; ORL='#E0874F'; MED='#3D6672'
CG="font-family:'CG',Georgia,serif;"
def page(inner, bg=INK, fg=IV):
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{ff}*{{box-sizing:border-box;margin:0}}body{{width:1080px;height:1350px;overflow:hidden;font-family:Inter,sans-serif;font-variant-numeric:lining-nums}}</style></head>
<body><div style="position:relative;width:1080px;height:1350px;background:{bg};color:{fg};overflow:hidden">{inner}</div></body></html>'''
def kick(t,c=ORL):
    return f'<div style="display:flex;align-items:center;gap:14px;font-size:22px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:{c}"><span style="width:14px;height:14px;background:{c};transform:rotate(26deg);display:inline-block"></span>{t}</div>'
def bar(fg=IV, line='rgba(246,241,232,.3)', sun=ORL):
    return (f'<div style="position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid {line};padding-top:22px">'
            f'<div style="{CG}font-size:40px;font-weight:500;letter-spacing:.06em;color:{fg}">S<span style="display:inline-block;width:26px;height:26px;border-radius:50%;background:{sun};margin:0 2px"></span>L <i style="color:{sun}">y</i> SÓL</div>'
            f'<div style="font-size:22px;letter-spacing:.14em;font-weight:600;color:{fg};opacity:.8">SOLYSOL.PL</div></div>')
P={}
# 1 Narzekalnia
opts=['Cita previa – na wszystko trzeba się umówić','„Mañana” – fachowiec, który miał być wczoraj','Papierologia: NIE, padrón, certyfikaty','Fiesta u sąsiadów do 3 w nocy','Ceny w Marbelli w sezonie','Ronda i kierowcy bez kierunkowskazów']
oh=''.join(f'<div style="display:flex;gap:26px;align-items:center;padding:20px 0;border-bottom:1.5px solid #DDD4C6"><span style="width:58px;height:58px;border-radius:50%;background:{ORG};color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;flex:none">{"ABCDEF"[i]}</span><span style="font-size:33px;line-height:1.25">{o}</span></div>' for i,o in enumerate(opts))
P['01-narzekalnia']=page(f'''<div style="position:absolute;left:80px;right:80px;top:90px">{kick("Narzekalnia",ORG)}
<div style="{CG}font-size:96px;font-weight:500;line-height:1;margin-top:26px">Co Cię najbardziej <i style="color:{ORG}">wkurza</i> w Hiszpanii?</div>
<div style="margin-top:34px;border-top:3px solid {INK}">{oh}</div>
<div style="font-size:30px;margin-top:34px;line-height:1.4">Napisz literę w komentarzu. <b>Wyniki pokażemy na profilu.</b></div></div>{bar(INK,"#CEC6B9")}''',IV,INK)
# 2 Costa del Crime
P['02-costa-del-crime']=page(f'''<img src="file:///home/claude/photos_raw/ban2_bwf.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:40% 50%;filter:contrast(1.1)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,21,19,.85) 0%,rgba(23,21,19,.15) 25%,rgba(23,21,19,.75) 50%,rgba(23,21,19,.98) 68%)"></div>
<div style="position:absolute;left:80px;right:80px;top:90px">{kick("Costa bez filtra")}</div>
<div style="position:absolute;left:80px;right:80px;top:780px"><div style="{CG}font-size:66px;color:{ORL};line-height:1">1978–1985</div>
<div style="{CG}font-size:92px;font-weight:500;line-height:.98;margin-top:14px">Siedem lat bez <i style="color:{ORL}">ekstradycji</i></div>
<div style="font-size:31px;line-height:1.45;margin-top:22px;color:#E9E2D6">Hiszpania wypowiedziała traktat z Wielką Brytanią. Zbiegli gangsterzy osiedlali się na Costa del Sol. Tak narodziła się „Costa del Crime”.</div></div>{bar()}''')
# 3 NIE
steps=[('Wybierz formularz','EX-15 dla nierezydenta · EX-18 dla obywatela UE mieszkającego tu ponad 3 miesiące'),('Zapłać opłatę','formularz 790, kod 012 – ok. 10 €, przed wizytą'),('Umów wizytę','cita previa na stronie administracji – terminy znikają szybko'),('Spakuj dokumenty','paszport + kopia, formularz, dowód opłaty, potwierdzenie wizyty'),('Odbierz numer','zwykle od ręki lub w ciągu kilku dni')]
sh=''.join(f'<div style="display:grid;grid-template-columns:70px 1fr;gap:18px;padding:22px 0;border-top:1.5px solid rgba(246,241,232,.2)"><span style="{CG}font-size:64px;color:{ORL};line-height:.9">{i+1}</span><div><div style="font-size:34px;font-weight:600">{t}</div><div style="font-size:26px;line-height:1.4;color:#DCD3C6;margin-top:6px">{d}</div></div></div>' for i,(t,d) in enumerate(steps))
P['03-nie-krok-po-kroku']=page(f'''<div style="position:absolute;left:80px;right:80px;top:90px">{kick("Jak to załatwić")}
<div style="{CG}font-size:104px;font-weight:500;line-height:1;margin-top:22px">NIE <i style="color:{ORL}">krok po kroku</i></div>
<div style="margin-top:34px">{sh}</div>
<div style="font-size:22px;color:#B3ABA0;margin-top:18px">Kwoty i formularze mogą się zmienić – sprawdź przed wizytą. Zapisz post 🔖</div></div>{bar()}''')
# 4 Numery
nums=[('112','nagłe wypadki – także po angielsku'),('091','Policía Nacional – w miastach'),('062','Guardia Civil – poza miastami')]
nh=''.join(f'<div style="display:flex;align-items:baseline;gap:40px;padding:34px 0;border-bottom:2px solid #DDD4C6"><span style="{CG}font-size:150px;font-weight:600;color:{ORG};line-height:.85">{a}</span><span style="font-size:36px;line-height:1.3">{b}</span></div>' for a,b in nums)
P['04-numery-alarmowe']=page(f'''<div style="position:absolute;left:80px;right:80px;top:90px">{kick("Zapisz ten post",ORG)}
<div style="{CG}font-size:96px;font-weight:500;line-height:1;margin-top:22px">Numery, które musisz <i style="color:{ORG}">znać</i></div>
<div style="margin-top:30px;border-top:3px solid {INK}">{nh}</div>
<div style="font-size:30px;line-height:1.45;margin-top:34px">Kradzież? Zawsze zgłoś ją na policji (<i>denuncia</i>) – kopia jest potrzebna do ubezpieczenia i nowego dokumentu w konsulacie.</div></div>{bar(INK,"#CEC6B9")}''',IV,INK)
def fact(key,num,head,txt,src,bg=INK,fg=IV,acc=ORL):
    P[key]=page(f'''<div style="position:absolute;left:80px;right:80px;top:90px">{kick("Czy wiesz, że…",acc)}</div>
<div style="position:absolute;left:80px;right:80px;top:280px"><div style="{CG}font-size:300px;font-weight:600;line-height:.85;color:{acc};letter-spacing:-.02em">{num}</div>
<div style="{CG}font-size:84px;font-weight:500;line-height:1.02;margin-top:40px">{head}</div>
<div style="font-size:34px;line-height:1.45;margin-top:30px;opacity:.88">{txt}</div>
<div style="font-size:21px;margin-top:34px;opacity:.6">Źródło: {src}</div></div>{bar(fg, "rgba(246,241,232,.3)" if bg==INK else "#CEC6B9")}''',bg,fg)
fact('05-hymn-bez-slow','4','kraje na świecie mają hymn <i style="color:#E0874F">bez słów</i>','Hiszpania, Bośnia i Hercegowina, Kosowo i San Marino. Dlatego hiszpańscy piłkarze stoją przy hymnie w ciszy.','Real Decreto 1560/1997')
fact('06-zla-strefa-czasowa','1940','Hiszpania żyje <i style="color:#C8692E">w złym czasie</i>','Madryt leży na południe od Londynu, a zegarki pokazują czas Warszawy. Od 1940 r. Stąd tak późne zachody słońca – i kolacja o 22:00.','timeanddate.com',IV,INK,ORG)
fact('07-najstarsza-restauracja','1725','Najstarsza restauracja <i style="color:#E0874F">świata</i> jest w Madrycie','Botín działa od 1725 r. – potwierdza Księga Rekordów Guinnessa. Jadał tu Hemingway.','Guinness World Records')
fact('08-dali-chupa-chups','1969','Logo Chupa Chups narysował <i style="color:#C8692E">Salvador Dalí</i>','Żółtą stokrotkę. Podobno zajęło mu to mniej niż godzinę.','Telefónica',IV,INK,ORG)
fact('09-blekitne-flagi','15%','wszystkich plaż z Błękitną Flagą <i style="color:#E0874F">jest w Hiszpanii</i>','677 plaż w 2026 r. – więcej niż w jakimkolwiek innym kraju. Andaluzja ma ich 143.','ADEAC 2026')
# 10 Mapa Polaka
cats=['Polskie delikatesy','Lekarze po polsku','Fryzjer i beauty','Msza po polsku','Polska szkoła sobotnia','Księgowi i prawnicy']
ch=''.join(f'<div style="display:flex;gap:18px;align-items:center;font-size:34px;padding:12px 0"><span style="width:16px;height:16px;background:{INK};transform:rotate(26deg);display:inline-block"></span>{c}</div>' for c in cats)
P['10-mapa-polaka']=page(f'''<div style="position:absolute;left:80px;right:80px;top:90px">{kick("Mapa Polaka",INK)}
<div style="{CG}font-size:100px;font-weight:500;line-height:1;margin-top:24px">Obsługujesz klientów <i>po polsku?</i></div>
<div style="font-size:34px;line-height:1.4;margin-top:26px">Tworzymy mapę polskich miejsc od Estepony po Málagę – w następnym numerze magazynu.</div>
<div style="margin-top:28px">{ch}</div>
<div style="margin-top:34px;background:{INK};color:{IV};padding:30px 36px;font-size:32px;line-height:1.4">Zgłoś firmę: <b>redakcja@solysol.pl</b><br><span style="color:{ORL}">Wpis podstawowy – bezpłatny.</span></div></div>{bar(INK,"rgba(23,21,19,.3)",INK)}''',ORL,INK)
for k,v in P.items(): open(k+'.html','w').write(v)
print(len(P))
