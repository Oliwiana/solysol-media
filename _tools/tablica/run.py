import sys; sys.path.insert(0,'/tmp/g'); import gen
from gen import wt
P=lambda f,cap,t,**k: dict(k='photo',f=f,cap=cap,t=round(t,2),**k)
S=lambda f,cap,t: dict(f=f,cap=cap,t=round(t,2))

def o2(L,LS,T,D):
    return {
     3: [dict(k='note',t=LS[3],lab='Ze statku schodzi:',text='Ernest Hemingway',tt=LS[3]+0.3,td=0.9,h=260),
         dict(k='sticker',t=LS[3]+1.0,text='→ 59 LAT, SŁAWNY PISARZ',dy=-30,x=200)],
     4: [P('typewriter-vintage/04','Reportaż dla „Life”',LS[4],sub=S('typewriter-old/03','Klawisze',LS[4]+1.7)),
         dict(k='stamp',t=LS[4]+1.2,text='LIFE · 1959',dx=440,dy=30)],
     5: [P('plaza-de-toros-de-ronda/02','Arena w Rondzie',LS[5],sub=S('plaza-de-toros-de-ronda/06','Azulejos z bykami',LS[5]+1.8)),
         dict(k='sticker',t=wt(T,'Ordóñeza',LS[5]),text='ORDÓÑEZ VS DOMINGUÍN',dy=-30,x=220)],
     9: [dict(k='list',t=LS[9],title='URODZINY · 21.07.1959',items=[('Szampan z Francji',LS[9]),('Jedzenie z Londynu',wt(T,'Jedzenie',LS[9])),('Orkiestra',wt(T,'Orkiestra',LS[9])),('Strzelnica jak na jarmarku',wt(T,'strzelnica',LS[9])),('…i maharadża',wt(T,'maharadża',LS[9]))])],
     10: [], 11: [P('champagne-bottles/05','Szampan',LS[11]-0.3)],
     13: [P('fireworks-night-spain/03','Fajerwerki',LS[13],sub=S('fireworks-night-spain/04','Noc',LS[13]+1.0)),
          dict(k='stamp',t=wt(T,'palmę',LS[13]),text='POŻAR!',dx=380,dy=30,fs=60)],
     14: [dict(k='sticker',t=wt(T,'straż',LS[14]),text='→ STRAŻ POŻARNA Z MALAGI',dy=-30,x=160)],
     15: [dict(k='note',t=LS[15],lab='Reportaż wyjdzie jako książka:',text='„Niebezpieczne lato”',tt=wt(T,'„Niebezpieczne',LS[15]),td=0.9,h=280)],
     16: [P('typewriter-vintage/05','Rękopis',LS[16],sub=S('ronda-puente-nuevo/06','Andaluzja',LS[16]+1.5)),
          dict(k='stamp',t=wt(T,'osiemdziesiątym',LS[16]),text='DOPIERO 1985',dx=520,dy=30)],
     17: [P('la-consula-churriana/02','La Cónsula dziś',LS[17]),dict(k='stamp',t=LS[17]+1.2,text='SZKOŁA HOTELARSKA',dx=600,dy=30,fs=40)],
     18: [P('plaza-de-toros-de-la-malagueta/02','La Malagueta',LS[18]-0.4),
          dict(k='sticker',t=LS[18],text='BYŁBYŚ NA TEJ IMPREZIE? NAPISZ W KOMENTARZU',dy=-20,x=110,fs=40)],
    }

def o3(L,LS,T,D):
    return {
     3: [P('hotel-pez-espada-torremolinos/01','Wieża hotelu',LS[3],sub=S('hotel-torremolinos/04','Fasada',LS[3]+1.7)),
         dict(k='stamp',t=LS[3]+0.3,text='5 ★',dx=320,dy=30,fs=64),
         dict(k='sticker',t=wt(T,'Pierwszy',LS[3]),text='PIERWSZY LUKSUSOWY W TORREMOLINOS',dy=-30,x=90,fs=40)],
     5: [dict(k='count',t=LS[5],title='HOTELE: 6 LAT PRZED OTWARCIEM',n=6,unit='hoteli')],
     6: [dict(k='note',t=LS[6]-0.2,lab='6 lat PO otwarciu:',text='PONAD 50 HOTELI',tt=wt(T,'ponad',LS[6]),td=0.7,h=260,fs=70)],
     8: [P('alhaurin-el-grande/01','Alhaurín el Grande',LS[8],sub=S('clapperboard/03','Klaps',LS[8]+1.8)),
         dict(k='sticker',t=LS[8]+0.2,text='DIRK BOGARDE · JOHN MILLS',dy=-30,x=180)],
     9: [dict(k='list',t=LS[9],title='GOŚCIE HOTELU',items=[('Anthony Quinn',LS[9]),('Raquel Welch',wt(T,'Raquel',LS[9])),('Ingrid Bergman',wt(T,'Ingrid',LS[9])),('Elizabeth Taylor',wt(T,'Elizabeth',LS[9])),('Sophia Loren',wt(T,'Sophia',LS[10]))])],
     10: [],
     11: [P('hotel-pez-espada-torremolinos/04','Promenada',LS[11],sub=S('hotel-torremolinos/03','Pez Espada',LS[11]+1.8)),
          dict(k='stamp',t=wt(T,'sześćdziesiątym',LS[11]),text='1964',dx=360,dy=30)],
     12: [dict(k='dark',t=LS[12]-0.2,lab='Najsłynniejszy gość:',text='FRANK SINATRA',tt=LS[12],td=0.7,h=280)],
     13: [P('desfiladero-de-los-gaitanes/04','El Chorro',LS[13],sub=S('clapperboard/06','„Ekspres von Ryana”',LS[13]+1.5))],
     14: [dict(k='list',t=LS[14],title='NA SCENIE',items=[('Julio Iglesias',wt(T,'Julio',LS[14])),('Raphael',wt(T,'Raphael',LS[14])),('Massiel',wt(T,'Massiel',LS[14]))])],
     16: [P('torre-de-los-molinos-torremolinos/02','Stare miasto',LS[16]-0.3),
          dict(k='sticker',t=LS[16],text='KOGO SPOTKAŁBYŚ W BARZE? NAPISZ W KOMENTARZU',dy=-20,x=110,fs=40)],
    }

def o4(L,LS,T,D):
    films=[('„Labirynt namiętności”',wt(T,'„Labiryncie',LS[3])),('„Kobiety na skraju…”',LS[4]),('„Mambo Kings”',LS[6]),('„Filadelfia”',wt(T,'„Filadelfia',LS[6]))]
    return {
     2: [dict(k='note',t=LS[2],lab='Rodzi się w Maladze:',text='Antonio Banderas',tt=wt(T,'Antonio',LS[2]),td=0.8,h=260)],
     3: [P('clapperboard/02','Pierwszy klaps',LS[3]-0.2),dict(k='stamp',t=LS[3]+0.4,text='ALMODÓVAR',dx=600,dy=30)],
     4: [dict(k='list',t=LS[4]-0.2,title='FILMY',items=films)],
     5: [P('hollywood-sign/02','Hollywood',LS[5],sub=S('hollywood-sign/06','Los Angeles',LS[5]+1.7)),dict(k='stamp',t=LS[5]+0.6,text='LATA 90.',dx=400,dy=30)],
     6: [],
     7: [P('muelle-uno-m-laga/04','Port w Maladze',LS[7]),dict(k='stamp',t=wt(T,'zawał',LS[7]),text='2017 · ZAWAŁ',dx=480,dy=30)],
     8: [P('teatro-del-soho-m-laga/01','Dawny Teatro Alameda',LS[8]),dict(k='sticker',t=wt(T,'kupuje',LS[8]),text='→ KUPUJE TEATR',dy=-30,x=300)],
     10: [P('teatro-cervantes-malaga/01','Teatralna Malaga',LS[10]),dict(k='sticker',t=LS[10]+0.5,text='„A CHORUS LINE”',dy=-30,x=360)],
     11: [dict(k='note',t=LS[11],lab='2019:',text='„Ból i blask”',tt=wt(T,'„Ból',LS[11]),td=0.6,h=260)],
     12: [dict(k='sticker',t=wt(T,'nominacja',LS[12]),text='★ NOMINACJA DO OSCARA',dy=-30,x=200)],
     14: [dict(k='note',t=LS[14],lab='Od ponad 20 lat mayordomo bractwa:',text='Lágrimas y Favores',tt=wt(T,'Lágrimas',LS[14]),td=0.9,h=300),
          P('semana-santa-malaga/04','Tron',LS[14]+2.2)],
     17: [P('iglesia-de-los-santos-martires-malaga/05','Drzwi kościoła',LS[17]-0.4),
          dict(k='sticker',t=LS[17],text='WIDZIAŁEŚ GO NA PROCESJI? NAPISZ W KOMENTARZU',dy=-20,x=110,fs=40)],
    }

def o5(L,LS,T,D):
    return {
     2: [dict(k='note',t=LS[2],lab='Pisarz z Danii:',text='Hans Christian Andersen',tt=wt(T,'Hans',LS[2]),td=1.0,h=300),
         P('malaga-port-19th-century/03','Rycina portu',LS[2]+2.4)],
     3: [dict(k='sticker',t=wt(T,'Jonasem',LS[3]),text='+ PRZYJACIEL JONAS COLLIN',dy=-30,x=180)],
     5: [P('malaga-port-19th-century/04','Zatoka Malagi',LS[5],sub=S('puerto-de-malaga-faro/01','Latarnia La Farola',LS[5]+1.8)),
         dict(k='sticker',t=wt(T,'Czeka',LS[5]),text='→ CZEKA NA KRÓLOWĄ IZABELĘ II',dy=-30,x=120)],
     7: [P('catedral-de-m-laga/04','La Manquita',LS[7],sub=S('catedral-de-m-laga/06','Portal katedry',LS[7]+1.6)),
         dict(k='stamp',t=wt(T,'Manquitę',LS[7]),text='1 WIEŻA',dx=420,dy=30)],
     10: [dict(k='note',t=LS[10],lab='1863 · książka:',text='„W Hiszpanii”',tt=wt(T,'„W',LS[10]),td=0.7,h=260)],
     11: [P('paseo-del-parque-malaga/06','Paseo del Parque',LS[11]),
          dict(k='dark',t=wt(T,'szczęśliwy',LS[11])-0.6,lab='Andersen o Maladze:',text='nigdzie w Hiszpanii nie był tak szczęśliwy',tt=wt(T,'szczęśliwy',LS[11])-0.4,td=1.4,h=320)],
     12: [P('malaga-port-19th-century/02','Malaga i morze',LS[12])],
     13: [P('plaza-de-la-marina-malaga/03','Plaza de la Marina',LS[13]),dict(k='stamp',t=wt(T,'brązu',LS[13]),text='POMNIK Z BRĄZU',dx=560,dy=30,fs=40)],
     15: [P('alameda-principal-malaga/03','Alameda',LS[15]-0.4),
          dict(k='sticker',t=LS[15],text='GDZIE TY CZUJESZ SIĘ U SIEBIE? NAPISZ W KOMENTARZU',dy=-20,x=90,fs=38)],
    }
H={2:'LA CÓNSULA',3:'TORREMOLINOS',4:'MALAGA',5:'MALAGA'}
SUB={2:'Odc. 2 · Gwiazdy na Costa del Sol · solysol.pl',3:'Odc. 3 · Gwiazdy na Costa del Sol · solysol.pl',4:'Odc. 4 · Gwiazdy na Costa del Sol · solysol.pl',5:'Finał serii · Gwiazdy na Costa del Sol · solysol.pl'}
for n in map(int,sys.argv[1:]):
    gen.render(n,{2:o2,3:o3,4:o4,5:o5}[n],H[n],endsub=SUB[n])
