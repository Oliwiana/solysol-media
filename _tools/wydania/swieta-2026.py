# Dodatek świąteczny Sol y Sól – strony magazynu
def P_cover(n, N):
    return open('/home/claude/swieta_up/cover_A.html').read()

def P_liczby(n, N):
    g = lambda a, b, c=None: f'<div style="border-top:2px solid {INKK};padding-top:14px">{stat(a, b, c or RED)}</div>'
    stats = (g('2,8 mln', 'lampek LED w centrum Malagi – włączenie 27.11') + g('3,8 mln', 'lampek w Marbelli i San Pedro', GRN) +
             g('20 €', 'kosztuje décimo, czyli los El Gordo', GOLD) + g('1812', 'rok pierwszego losowania loterii świątecznej') +
             g('12', 'winogron o północy w Sylwestra', GRN) + g('ok. 17°C', 'średnio w dzień w grudniu w Maladze', GOLD))
    short = ''.join(f'<div style="border-top:1px solid #CFC5B5;padding:12px 0"><div style="{CG}font-size:25px;font-weight:600">{a}</div><div style="font-size:18px;line-height:1.4;color:{MUT};margin-top:3px">{b}</div></div>' for a, b in [
        ('Málaga – koncert na start', 'Po włączeniu świateł 27.11 o 18:30 gra El Kanka, wstęp wolny.'),
        ('Marbella – anioły', 'Nowy pokaz na Plaza de los Naranjos, 3 razy dziennie.'),
        ('Fuengirola – jarmark', 'Drewniane domki na Plaza de la Constitución do ok. 21.12.'),
        ('Estepona – churros', '1.12 o 19:00 na Plaza del Ajedrez, z flashmobem 30 muzyków.')])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Na start")}{H("Święta w liczbach", 88)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px 40px;width:560px">{stats}</div></div>'
             f'<div style="position:absolute;left:668px;right:64px;top:222px">{hdr("Krótko", 34)}{short}</div>'
             + photo('x_hp2.jpg', 0, 790, 1080, 460, '50% 42%')
             + f'<div style="position:absolute;right:64px;top:740px;width:400px;background:{RED};color:#fff;padding:26px 28px;box-shadow:0 18px 40px rgba(0,0,0,.25)"><div style="font-size:15px;font-weight:800;letter-spacing:.22em;color:#F7D9A0">CZY WIESZ, ŻE…</div><div style="{CG}font-size:30px;line-height:1.2;margin-top:8px">Hiszpańskie święta trwają do 6 stycznia – najważniejszy dzień dla dzieci to Trzech Króli.</div></div>'
             + f'<div style="position:absolute;left:64px;top:1214px;font-size:13px;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.6)">Calle Larios w Maladze. Fot. Hernán Piñera / Wikimedia Commons, CC BY-SA 2.0</div>'
             + f'<div style="position:absolute;left:64px;right:64px;bottom:84px"></div>')
    return frame(n, N, 'Na start', inner)

def P_kalendarz(n, N):
    rows = [('27.11', 'pt', 'Málaga · Fuengirola', 'Włączenie świateł. W Maladze o 18:30, potem koncert El Kanki.'),
            ('28.11', 'sob', 'Málaga', 'Rusza mapping na wieży katedry – 19:00, 20:30, 22:00.'),
            ('1.12', 'wt', 'Estepona', 'Światła, kolędy pastorales, churros z czekoladą i flashmob.'),
            ('7–8.12', 'pn–wt', 'Andaluzja', 'Dzień Konstytucji (przeniesiony z niedzieli) i Niepokalane Poczęcie – dwa dni wolne.'),
            ('ok. 21.12', '', 'Fuengirola', 'Ostatnie dni jarmarku na Plaza de la Constitución.'),
            ('22.12', 'wt', 'Cała Hiszpania', 'El Gordo – losowanie od rana na żywo w TVE.'),
            ('24.12', 'czw', 'Nochebuena', 'Wigilia. Sklepy otwarte, ale zamykają wcześniej.'),
            ('25.12', 'pt', 'Navidad', 'Boże Narodzenie – dzień wolny, sklepy zamknięte.'),
            ('28.12', 'pn', 'Día de los Inocentes', 'Hiszpański prima aprilis – uważaj na żarty.'),
            ('31.12', 'czw', 'Nochevieja', '12 winogron o północy. W Maladze na Plaza de la Constitución.'),
            ('5.01', 'wt', 'Cabalgata de Reyes', 'Wieczorne pochody Trzech Króli w miastach.'),
            ('6.01', 'śr', 'Reyes', 'Dzień wolny i prezenty dla dzieci.')]
    rr = ''.join(f'<div style="display:grid;grid-template-columns:170px 1fr;gap:24px;padding:17px 0;border-top:1px solid #CFC5B5">'
                 f'<div><span style="{CG}font-size:40px;font-weight:600;color:{RED if i % 2 == 0 else GRN};line-height:1">{a}</span> <span style="font-size:15px;color:{MUT};letter-spacing:.1em">{b.upper()}</span></div>'
                 f'<div><div style="font-size:15px;font-weight:800;letter-spacing:.18em;color:{GOLD};text-transform:uppercase">{E(c)}</div><div style="font-size:21px;line-height:1.35;margin-top:2px">{E(d)}</div></div></div>' for i, (a, b, c, d) in enumerate(rows))
    inner = f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Kalendarz świąt")}{H("Daty, których <i style=\'color:"+RED+"\'>nie przegap</i>", 80)}{rule()}{rr}</div>'
    return frame(n, N, 'Kalendarz', inner)

def P_malaga(n, N):
    inner = (photo('x_hp2.jpg', 0, 0, 1080, 640, '50% 30%') +
             f'<div style="position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.05) 55%,rgba(0,0,0,.8) 100%)"></div>'
             f'<div style="position:absolute;left:64px;right:64px;top:430px;color:#fff">{kick("Temat numeru · Málaga", "#F2C14E")}{H("Calle Larios <i style=\'color:#F2C14E\'>zapala święta</i>", 86, "#fff")}</div>'
             f'<div style="position:absolute;right:30px;top:22px;font-size:13px;color:rgba(255,255,255,.85)">Fot. Hernán Piñera / Wikimedia Commons, CC BY-SA 2.0</div>'
             f'<div style="position:absolute;left:64px;top:690px;width:580px;columns:2;column-gap:30px">'
             + dc('Święta na Costa del Sol zaczynają się w Maladze. W piątek 27.11 o 18:30 przy wejściu na calle Larios zapalą się świąteczne światła – w centrum to w sumie 2,8 mln lampek LED. Zaraz potem darmowy koncert El Kanki.')
             + p('Główna atrakcja to pokaz światła i muzyki „Natividad de Luz” – lampki nad ulicą zmieniają się w rytm muzyki. Pokazy trwają do 4.01, trzy razy wieczorem, poza 24 i 31.12.', 20)
             + p('Od 28.11 warto podejść też pod katedrę: na jej wieży wyświetlany jest mapping – barwne obrazy na kamiennej fasadzie.', 20)
             + '</div>'
             f'<div style="position:absolute;left:690px;right:64px;top:690px">'
             + f'<div style="background:{GRN};color:#fff;padding:24px 26px"><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:#F2C14E">POKAZY NA LARIOS</div><div style="{CG}font-size:40px;font-weight:600;margin-top:6px">18:30 · 20:30 · 22:00</div><div style="font-size:18px;opacity:.9">codziennie do 4.01, bez 24 i 31.12</div>'
             + f'<div style="height:1px;background:rgba(255,255,255,.3);margin:16px 0"></div><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:#F2C14E">MAPPING NA KATEDRZE</div><div style="{CG}font-size:40px;font-weight:600;margin-top:6px">19:00 · 20:30 · 22:00</div><div style="font-size:18px;opacity:.9">od 28.11</div></div>'
             + pull('W centrum Malagi zaświeci 2,8 mln lampek.')
             + '</div>' + src('Ayuntamiento de Málaga; que.es; malagaes.com; marbella-sanpedro.com. Stan na 18.11.2026.'))
    return frame(n, N, 'Málaga', inner)

def P_marbella(n, N):
    nums = ''.join(f'<div style="border-top:2px solid {c};padding-top:10px"><div style="{CG}font-size:50px;font-weight:600;line-height:1;color:{c}">{a}</div><div style="font-size:17px;margin-top:6px;color:{MUT}">{b}</div></div>' for a, b, c in [
        ('3,8 mln', 'lampek LED', RED), ('532', 'świetlne łuki', GRN), ('146', 'oświetlonych drzew', GOLD), ('2 421', 'girland', RED)])
    inner = (photo('xmas_naranjos.jpg', 0, 0, 470, 1350, '92% 0%')
             + f'<div style="position:absolute;left:470px;top:0;width:10px;height:1350px;background:{GOLD}"></div>'
             + cap('Plaza de los Naranjos w Marbelli. Fot. Berthold Werner / Wikimedia Commons, CC BY-SA 3.0', 24, 1300, 430)
             + f'<div style="position:absolute;left:530px;right:64px;top:70px">{kick("Marbella · San Pedro")}{H("Anioły nad <i style=\'color:"+RED+"\'>Plaza de los Naranjos</i>", 70)}{rule()}'
             + dc('W tym roku Marbella stawia na pokazy muzyczne. Na Plaza de los Naranjos, najbardziej znanym placu starego miasta, staną cztery wielkie anioły – z trzema pokazami dziennie.')
             + p('San Pedro Alcántara dostanie własną atrakcję: świetlny las na Marqués del Duero, też z trzema pokazami dziennie.', 20)
             + pull('Cztery wielkie anioły i świetlny las.', GRN)
             + f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px 26px">{nums}</div>'
             + '<div style="height:22px"></div>'
             + box('Kiedy włączenie świateł?', 'Ratusz jeszcze nie podał daty. Damy znać od razu, gdy ją ogłosi.', SAND, INKK, RED)
             + '</div>' + f'<div style="position:absolute;left:530px;right:64px;bottom:84px;font-size:13px;color:{MUT}">Źródła: Ayuntamiento de Marbella; Marbella Directo; La Noción; Área Costa del Sol. Stan na 18.11.2026.</div>')
    return frame(n, N, 'Marbella', inner)

def P_fue_est(n, N):
    inner = (photo('xmas_fue.jpg', 0, 0, 536, 520, '50% 60%') + photo('est2.jpg', 544, 0, 536, 520, '50% 50%')
             + f'<div style="position:absolute;left:536px;top:0;width:8px;height:520px;background:{GOLD}"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:440px;background:{PAPER};padding:26px 30px 6px;box-shadow:0 -10px 30px rgba(0,0,0,.12)">{kick("Fuengirola · Estepona")}{H("Jarmark, churros <i style=\'color:"+GRN+"\'>i 2,77 mln lampek</i>", 66)}</div>'
             + f'<div style="position:absolute;left:64px;top:650px;width:440px">{hdr("Fuengirola", 40, RED)}'
             + dc('Światła zapalają się w piątek 27.11 i świecą do 6.01. Najbardziej ozdobiona będzie Plaza de España.', RED)
             + p('Na <b>Plaza de la Constitución</b> staje jarmark z drewnianymi domkami: ozdoby, prezenty, rękodzieło – od końca listopada do ok. 21.12.', 20)
             + f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:6px">{stat("446","łuków",RED,46)}{stat("164","latarni",GRN,46)}{stat("63","figury",GOLD,46)}</div></div>'
             + f'<div style="position:absolute;left:576px;top:650px;width:440px">{hdr("Estepona", 40, GRN)}'
             + dc('Estepona włącza światła we wtorek 1.12 o 19:00 na Plaza del Ajedrez.', GRN)
             + p('W programie kolędy grup <i>pastorales</i>, <b>churros z czekoladą</b> dla wszystkich i flashmob ponad 30 muzyków na żywo.', 20)
             + box('Słowo na dziś', '<b>Pastorales</b> – grupy, które śpiewają tradycyjne andaluzyjskie kolędy przy tamburynach i zambombach.', SAND, INKK, RED)
             + '</div>' + cap('Fuengirola i Estepona. Fot. Javi Masa / Wikimedia Commons, CC BY 3.0; Christian Hergesell / Unsplash', 64, 1215, 952)
             + src('Ayuntamiento de Fuengirola; Área Costa del Sol; Ayuntamiento de Estepona; Al Sol de la Costa. Stan na 18.11.2026.'))
    return frame(n, N, 'Fuengirola · Estepona', inner)

def P_gordo(n, N):
    tl = ''.join(f'<div style="display:grid;grid-template-columns:120px 1fr;gap:18px;padding:18px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:44px;font-weight:600;color:{RED}">{a}</div><div><b style="font-size:24px">{b}</b><div style="font-size:21px;line-height:1.4;color:{MUT}">{c}</div></div></div>' for a, b, c in [
        ('1812', 'Pierwsze losowanie', 'Loteria świąteczna działa od ponad 200 lat – to jedna z najstarszych loterii na świecie.'),
        ('22.12', 'Dzień losowania', 'Od rana cały kraj ogląda transmisję w TVE. Wielu Hiszpanów uważa ten dzień za początek świąt.'),
        ('20 €', 'Décimo', 'Tyle kosztuje dziesiąta część losu. Pełny los (billete) to 10 décimos.')])
    inner = (photo('xmas_loteria.jpg', 0, 10, 1080, 420, '50% 35%', style='none') +
             f'<div style="position:absolute;left:0;right:0;top:10px;height:420px;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.75) 100%)"></div>'
             f'<div style="position:absolute;left:64px;right:64px;top:290px;color:#fff">{kick("Tradycja · 22 grudnia", "#F2C14E")}{H("El Gordo – loteria, <i style=\'color:#F2C14E\'>którą żyje cały kraj</i>", 64, "#fff")}</div>'
             f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.85)">Obraz: Christian Franzen, ok. 1900 / Wikimedia Commons, domena publiczna</div>'
             f'<div style="position:absolute;left:64px;top:470px;width:560px">{tl}'
             + p('<br>Los kupuje się w punktach <b>Loterías y Apuestas del Estado</b> – często wspólnie: z rodziną, w pracy albo w ulubionym barze. Gdy numer wygra, cieszy się cała ulica.', 20) + '</div>'
             f'<div style="position:absolute;left:666px;right:64px;top:470px">'
             + box('Czy wiesz, że…', 'Wylosowane numery i kwoty nie są odczytywane, tylko <b>śpiewane</b> – robią to dzieci ze szkoły San Ildefonso w Madrycie.', RED)
             + '<div style="height:16px"></div>'
             + box('El Gordo, czyli…', '„Gruby” – tak nazywa się główną nagrodę. Stąd potoczna nazwa całego losowania.', GRN)
             + '<div style="height:16px"></div>'
             + box('Uwaga', 'Duże wygrane są w Hiszpanii opodatkowane. Szczegóły sprawdź na stronie Loterías y Apuestas del Estado.', SAND, INKK, RED)
             + '</div>' + src('Loterías y Apuestas del Estado; RTVE. Stan na 18.11.2026.'))
    return frame(n, N, 'Tradycje', inner)

def P_mit(n, N):
    cards = [('„W Hiszpanii prezenty przynosi Mikołaj.”', 'TO ZALEŻY', 'Coraz więcej rodzin daje prezenty 25.12, ale tradycyjnie przynoszą je Trzej Królowie 6.01.'),
             ('„Na święta w Maladze może spaść śnieg.”', 'MIT', 'W grudniu w dzień jest średnio ok. 17°C. Śnieg zobaczysz najwyżej w górach.'),
             ('„26 grudnia jest wolne.”', 'MIT', 'W Andaluzji drugi dzień świąt to zwykły dzień pracy.'),
             ('„W Wigilię wszystko jest zamknięte.”', 'MIT', 'Sklepy zwykle działają, ale zamykają wcześniej niż zwykle.'),
             ('„28 grudnia nie wierz w każdą wiadomość.”', 'FAKT', 'To Día de los Inocentes – żartują znajomi, a czasem nawet gazety.'),
             ('„Hiszpanie też chodzą na pasterkę.”', 'FAKT', 'Nazywa się Misa del Gallo – „msza koguta” – i odbywa się w noc wigilijną.')]
    cc = ''.join(f'<div style="background:{SAND if i % 3 != 1 else "#fff"};border:1px solid #D9CDB8;padding:28px 26px"><div style="{CG}font-style:italic;font-size:31px;font-weight:600;line-height:1.15">{E(a)}</div>'
                 f'<div style="display:inline-block;border:2px solid {RED if b == "MIT" else GRN};color:{RED if b == "MIT" else GRN};font-size:15px;font-weight:800;letter-spacing:.2em;padding:5px 10px;margin:12px 0 8px">{b}</div>'
                 f'<div style="font-size:22px;line-height:1.4">{E(c)}</div></div>' for i, (a, b, c) in enumerate(cards))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Sprawdzamy")}<div style="display:flex;justify-content:space-between;align-items:flex-end">{H("Mit <i style=\'color:"+RED+"\'>czy fakt?</i>", 88)}<div style="{CG}font-style:italic;font-size:24px;text-align:right;color:{MUT}">Sześć rzeczy, które każdy „wie”<br>o świętach w Hiszpanii</div></div>{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">{cc}</div></div>' + src('BOE i kalendarz świąt Junta de Andalucía 2026; AEMET; Conferencia Episcopal Española.'))
    return frame(n, N, 'Sprawdzamy', inner)

def P_pl_es(n, N):
    rows = [('Główny wieczór', '24.12 – Wigilia', '24.12 – Nochebuena'),
            ('Prezenty', '24.12, od Mikołaja lub Gwiazdora', 'Głównie 6.01 od Trzech Króli; coraz częściej też 25.12'),
            ('Na stole', '12 potraw, karp, barszcz, pierogi', 'Owoce morza, pieczona jagnięcina lub indyk, turrón'),
            ('Opłatek', 'Tak – dzielimy się przed kolacją', 'Nie ma tej tradycji'),
            ('Pasterka', 'Tak', 'Tak – Misa del Gallo'),
            ('Kolędy', 'Kolędy i pastorałki', 'Villancicos, w Andaluzji z zambombą'),
            ('26 grudnia', 'Drugi dzień świąt – wolne', 'W Andaluzji dzień pracy'),
            ('Sylwester', 'Szampan o północy', '12 winogron, potem cava'),
            ('Koniec świąt', '2.02 – Matki Bożej Gromnicznej', '6.01 – Trzech Króli')]
    head = f'<div style="display:grid;grid-template-columns:210px 1fr 1fr;gap:18px;padding-bottom:10px"><div></div><div style="font-size:18px;font-weight:800;letter-spacing:.2em;color:{RED}">🇵🇱 POLSKA</div><div style="font-size:18px;font-weight:800;letter-spacing:.2em;color:{GOLD}">🇪🇸 HISZPANIA</div></div>'
    rr = ''.join(f'<div style="display:grid;grid-template-columns:210px 1fr 1fr;gap:18px;padding:22px 0;border-top:1px solid #CFC5B5;background:{"transparent" if i % 2 else "rgba(239,230,214,.6)"}"><div style="{CG}font-size:26px;font-weight:600;padding-left:8px">{E(a)}</div><div style="font-size:22px;line-height:1.35">{E(b)}</div><div style="font-size:22px;line-height:1.35">{E(c)}</div></div>' for i, (a, b, c) in enumerate(rows))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Dla Polaków")}{H("Wigilia czy <i style=\'color:"+RED+"\'>Nochebuena?</i>", 84)}'
             f'<div style="font-size:22px;color:{MUT};margin-top:12px">Jak świętuje Polska, a jak Hiszpania – porównanie w jednym miejscu</div>{rule()}{head}{rr}</div>')
    return frame(n, N, 'Dla Polaków', inner)

def P_slodycze(n, N):
    items = [('x_turron.jpg', 'Turrón', 'Nugat z migdałów i miodu. Twardy (z Alicante) albo miękki (z Jijony) – oba znajdziesz w każdym supermarkecie.', 'Fot. Juan Emilio Prades Bel / Wikimedia Commons, CC BY 4.0'),
             ('x_rosc.jpg', 'Roscón de Reyes', 'Drożdżowy wieniec z kandyzowanymi owocami, jedzony 6.01. W środku figurka i fasolka.', 'Fot. Juan Emilio Prades Bel / Wikimedia Commons, CC BY 4.0')]
    cards = ''.join(f'<div>{""}<img src="file://{PH}{a}" style="width:300px;height:300px;object-fit:cover;border-radius:50%;border:6px solid #F2C14E;display:block;margin:0 auto"><div style="font-size:12px;color:{MUT};margin-top:4px">{E(d)}</div>{hdr(b, 38, RED)}<div style="font-size:20px;line-height:1.45">{E(c)}</div></div>' for a, b, c, d in items)
    more = ''.join(f'<div style="border-top:1px solid #CFC5B5;padding:12px 0;display:grid;grid-template-columns:230px 1fr;gap:16px"><div style="{CG}font-size:28px;font-weight:600;color:{GRN}">{a}</div><div style="font-size:19px;line-height:1.4">{b}</div></div>' for a, b in [
        ('Polvorones', 'Kruche ciasteczka z migdałami, które rozsypują się w ustach. Najsłynniejsze pochodzą z Estepy w prowincji Sewilla.'),
        ('Mantecados', 'Krewni polvorones – na smalcu, często cynamonowe lub cytrynowe.'),
        ('Pestiños', 'Andaluzyjskie smażone ciasteczka w miodzie, z nutą anyżu.'),
        ('Mazapán', 'Marcepan – najbardziej znany jest ten z Toledo.')])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Na słodko")}{H("Co Hiszpanie <i style=\'color:"+RED+"\'>jedzą na święta</i>", 78)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">{cards}</div><div style="margin-top:18px">{more}</div></div>')
    return frame(n, N, 'Na słodko', inner)

def P_ciekawostki(n, N):
    facts = [('Żywe szopki', 'Belén viviente to szopka z aktorami i zwierzętami – w wielu andaluzyjskich miasteczkach to całe przedstawienie.'),
             ('Zambomba', 'Spotkania z kolędami w rytmie flamenco. Nazwa pochodzi od bębna z trzciną, który „buczy” przy pocieraniu.'),
             ('Paga extra', 'W grudniu wielu pracowników dostaje dodatkową pensję – stąd świąteczne zakupy na dużą skalę.'),
             ('Kosz od szefa', 'Cesta de Navidad – kosz z szynką, winem i słodyczami, który firmy dają pracownikom.'),
             ('Listy do Króli', 'Dzieci piszą listy do Trzech Króli i wręczają je ich „paziom” w centrach handlowych.'),
             ('Węgiel dla niegrzecznych', 'Kto był niegrzeczny, dostaje od Króli węgiel – ale z cukru.'),
             ('Fasolka w cieście', 'Kto w rosconie trafi na fasolkę, zwyczajowo płaci za ciasto w przyszłym roku.'),
             ('Winogrona w puszce', 'Przed Sylwestrem sklepy sprzedają 12 obranych winogron w puszce – łatwiej zdążyć.'),
             ('Czerwona bielizna', 'W Sylwestra wiele osób zakłada czerwoną bieliznę – ma przynieść szczęście w nowym roku.'),
             ('Zegar z Puerta del Sol', 'Północ cała Hiszpania odlicza z telewizją, która pokazuje zegar na Puerta del Sol w Madrycie.'),
             ('Śpiewane numery', 'W El Gordo dzieci ze szkoły San Ildefonso śpiewają wylosowane numery.'),
             ('Prima aprilis w grudniu', '28.12 to Día de los Inocentes – dzień żartów, także w mediach.')]
    cc = ''.join(f'<div style="display:flex;gap:16px;padding:12px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:46px;font-weight:600;color:{[RED, GRN, GOLD][i % 3]};line-height:.9;min-width:52px">{i+1}</div><div><div style="font-size:21px;font-weight:700">{E(a)}</div><div style="font-size:18px;line-height:1.4;color:#4A443D;margin-top:3px">{E(b)}</div></div></div>' for i, (a, b) in enumerate(facts))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Ciekawostki")}{H("12 rzeczy, które <i style=\'color:"+RED+"\'>zaskakują Polaków</i>", 74)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 36px">{cc}</div></div>')
    return frame(n, N, 'Ciekawostki', inner)

def P_sylwester(n, N):
    inner = (photo('xmas_uvas.jpg', 0, 0, 536, 520, '50% 80%') + photo('x_rosc.jpg', 544, 0, 536, 520, '50% 45%')
             + f'<div style="position:absolute;left:536px;top:0;width:8px;height:520px;background:{GOLD}"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:440px;background:{PAPER};padding:26px 30px 6px;box-shadow:0 -10px 30px rgba(0,0,0,.12)">{kick("Sylwester · Trzech Króli")}{H("Winogrona, cava <i style=\'color:"+RED+"\'>i trzech króli</i>", 66)}</div>'
             + f'<div style="position:absolute;left:64px;top:650px;width:440px">{hdr("31.12 – Nochevieja", 38, RED)}'
             + dc('O północy Hiszpanie zjadają 12 winogron – po jednym przy każdym uderzeniu zegara. Każde to szczęście na jeden miesiąc.', RED)
             + p('W Maladze wspólne odliczanie odbywa się na <b>Plaza de la Constitución</b>. Potem toast cavą.', 20)
             + box('Wskazówka', 'Wybierz małe winogrona bez pestek – na 12 uderzeń zegara jest tylko kilkanaście sekund.', GRN) + '</div>'
             + f'<div style="position:absolute;left:576px;top:650px;width:440px">{hdr("5–6.01 – Reyes", 38, GRN)}'
             + dc('Wieczorem 5.01 przez miasta przechodzą Cabalgatas de Reyes – barwne pochody, z wozów leci w tłum deszcz cukierków.', GRN)
             + p('Rano 6.01 dzieci znajdują prezenty, a na stół trafia <b>roscón de Reyes</b>. To dzień wolny.', 20)
             + box('Dla rodziców', 'Na cabalgatę weź torbę lub odwrócony parasol – dzieci łapią do niego cukierki.', RED) + '</div>'
             + cap('Fot. Zarateman / Wikimedia Commons, CC0; Juan Emilio Prades Bel / Wikimedia Commons, CC BY 4.0', 64, 1215, 952))
    return frame(n, N, 'Tradycje', inner)

def P_slowniczek(n, N):
    w = [('¡Feliz Navidad!', 'Wesołych Świąt!'), ('¡Próspero Año Nuevo!', 'Szczęśliwego Nowego Roku!'), ('Nochebuena', 'Wigilia'), ('Nochevieja', 'Sylwester'),
         ('los Reyes Magos', 'Trzej Królowie'), ('el belén', 'szopka'), ('el villancico', 'kolęda'), ('el árbol de Navidad', 'choinka'),
         ('el regalo', 'prezent'), ('las uvas de la suerte', 'winogrona szczęścia'), ('las campanadas', 'uderzenia zegara o północy'), ('el décimo', 'los loterii (1/10)'),
         ('la cabalgata', 'pochód (Trzech Króli)'), ('el turrón', 'nugat'), ('la Misa del Gallo', 'pasterka'), ('el alumbrado', 'iluminacja świąteczna')]
    cc = ''.join(f'<div style="padding:13px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:31px;font-weight:600;color:{[RED, GRN][i % 2]}">{E(a)}</div><div style="font-size:20px;color:#4A443D;margin-top:2px">{E(b)}</div></div>' for i, (a, b) in enumerate(w))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Po hiszpańsku")}{H("Świąteczny <i style=\'color:"+RED+"\'>słowniczek</i>", 86)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px">{cc}</div>'
             f'<div style="margin-top:20px">{box("Złota fraza", "<b>¡Felices fiestas!</b> – „Wesołych świąt!”, uniwersalnie: pasuje i do sąsiada, i do klienta.", GRN)}</div></div>')
    return frame(n, N, 'Po hiszpańsku', inner)

def P_quiz(n, N):
    kids = [('Kto w Hiszpanii przynosi prezenty 6 stycznia?', 'a) Mikołaj  b) Trzej Królowie  c) Aniołek'),
            ('Co dostają od Króli niegrzeczne dzieci?', 'a) rózgę  b) węgiel z cukru  c) nic'),
            ('Ile winogron je się o północy w Sylwestra?', 'a) 7  b) 12  c) 20'),
            ('Co jest ukryte w rosconie?', 'a) figurka i fasolka  b) moneta  c) orzech'),
            ('Jak powiedzieć „Wesołych Świąt” po hiszpańsku?', 'a) ¡Feliz Navidad!  b) ¡Buenos días!  c) ¡Olé!')]
    adults = [('W którym roku odbyło się pierwsze losowanie loterii świątecznej?', 'a) 1812  b) 1912  c) 1975'),
              ('Ile kosztuje décimo, czyli los El Gordo?', 'a) 5 €  b) 20 €  c) 100 €'),
              ('Jak nazywa się hiszpańska pasterka?', 'a) Misa del Gallo  b) Misa del Sol  c) Nochebuena'),
              ('Gdzie w Maladze odlicza się do Nowego Roku?', 'a) Plaza de la Constitución  b) Muelle Uno  c) Gibralfaro'),
              ('Kiedy Hiszpanie robią sobie żarty jak u nas 1 kwietnia?', 'a) 24.12  b) 28.12  c) 6.01')]
    def col(title, emoji, items, start, c):
        qq = ''.join(f'<div style="padding:18px 0;border-top:1px solid #CFC5B5;display:flex;gap:14px"><div style="{CG}font-size:52px;font-weight:600;color:#F2C14E;line-height:.9;min-width:48px">{start+i}</div><div><div style="font-size:23px;font-weight:700;line-height:1.3">{E(a)}</div><div style="font-size:21px;color:#4A443D;margin-top:6px">{E(b)}</div></div></div>' for i, (a, b) in enumerate(items))
        return f'<div><div style="display:flex;align-items:center;gap:12px;background:{c};color:{"#2B2926" if c=="#F2C14E" else "#fff"};padding:14px 18px;font-size:20px;font-weight:800;letter-spacing:.18em">{emoji} {title}</div>{qq}</div>'
    score = ''.join(f'<div style="flex:1;text-align:center;padding:20px 10px;background:{bg};color:#fff"><div style="{CG}font-size:40px;font-weight:600">{a}</div><div style="font-size:17px;margin-top:4px">{b}</div></div>' for a, b, bg in [
        ('0–4 pkt', 'turysta na start', '#2B2926'), ('5–7 pkt', 'prawie Andaluzyjczyk', '#1F5C3F'), ('8–10 pkt', 'prawdziwy malagueño!', '#B8860B')])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Zagrajcie razem")}{H("Quiz dla <i style=\'color:"+RED+"\'>całej rodziny</i>", 82)}'
             f'<div style="font-size:21px;color:{MUT};margin-top:10px">Dzieci odpowiadają na pytania 1–5, dorośli na 6–10. Kto zbierze więcej punktów? Napiszcie wynik w komentarzu 👇</div>{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">{col("DLA DZIECI", "🧒", kids, 1, "#F2C14E")}{col("DLA DOROSŁYCH", "🧑", adults, 6, "#1F5C3F")}</div>'
             f'<div style="display:flex;gap:10px;margin-top:22px">{score}</div>'
             f'<div style="margin-top:14px;background:{SAND};padding:14px 22px;font-size:18px;transform:rotate(180deg);text-align:center">Odpowiedzi: 1b · 2b · 3b · 4a · 5a · 6a · 7b · 8a · 9a · 10b</div></div>')
    return frame(n, N, 'Quiz', inner)

def P_koniec(n, N):
    inner = (photo('x_tree_palm.jpg', 0, 10, 1080, 1340, '50% 40%', style='none') +
             f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,24,17,.25) 0%,rgba(8,24,17,.6) 45%,rgba(8,24,17,.94) 70%)"></div>'
             f'<div style="position:absolute;left:64px;right:64px;top:690px;color:#FAF7F2;text-align:center">'
             f'<div style="{CG}font-style:italic;font-size:46px;color:#F2C14E">¡Feliz Navidad!</div>'
             f'<div style="{CG}font-size:120px;font-weight:600;line-height:1">Wesołych Świąt</div>'
             f'<div style="font-size:26px;line-height:1.5;margin-top:20px">życzy redakcja Sol y Sól</div>'
             f'<div style="font-size:23px;line-height:1.5;margin-top:26px;color:#E9E1D2">Daty z Marbelli i kolejnych miejscowości dopiszemy, gdy ratusze je ogłoszą.<br>Codziennie o <b>8:00</b> i <b>19:00</b> – wydania z wybrzeża.</div>'
             f'<div style="display:flex;justify-content:center;gap:16px;margin-top:34px;font-size:19px;font-weight:800;letter-spacing:.16em"><span style="background:{RED};padding:15px 20px">🔔 OBSERWUJ @SOLYSOL.PL</span><span style="border:2px solid #FAF7F2;padding:13px 20px">ZAPISZ · UDOSTĘPNIJ</span></div></div>'
             f'<div style="position:absolute;right:30px;top:24px;font-size:13px;color:rgba(255,255,255,.85)">Fot. Bogdan Migulski / Wikimedia Commons, CC BY 2.0</div>')
    return page(GARL + inner, '#08180F', '#FAF7F2')


def P_dzieci(n, N):
    ideas = [('Wioska Mikołaja', 'Aldea de Papá Noel – w grudniu ma ją większość gmin wybrzeża. Dzieci oddają list i robią zdjęcie z Mikołajem.'),
             ('Listy do Trzech Króli', 'W centrach handlowych i na placach siedzą „paziowie” Króli. To im dzieci wręczają listy z życzeniami.'),
             ('Szopki – belenes', 'Ratusze i bractwa ustawiają duże szopki z ruchomymi figurkami. Wstęp zwykle jest bezpłatny.'),
             ('Cabalgata 5.01', 'Wieczorny pochód Trzech Króli. Z wozów lecą cukierki – weź torbę albo odwrócony parasol.')]
    ii = ''.join(f'<div style="display:flex;gap:16px;padding:16px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:46px;font-weight:600;color:{[RED, GRN, GOLD, RED][i]};line-height:.9;min-width:44px">{i+1}</div><div><div style="font-size:23px;font-weight:700">{E(a)}</div><div style="font-size:20px;line-height:1.42;color:#4A443D;margin-top:3px">{E(b)}</div></div></div>' for i, (a, b) in enumerate(ideas))
    inner = (photo('x_parque.jpg', 0, 0, 1080, 470, '50% 30%')
             + f'<div style="position:absolute;left:0;right:0;top:0;height:470px;background:linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,.35) 40%,rgba(0,0,0,.85) 100%)"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:300px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.5)">{kick("Dla rodzin", "#F2C14E")}{H("Święta <i style=\'color:#F2C14E\'>z dziećmi</i>", 86, "#fff")}</div>'
             + f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.9)">Fot. Daniel Capilla / Wikimedia Commons, CC BY-SA 4.0</div>'
             + f'<div style="position:absolute;left:64px;top:510px;width:560px">{ii}</div>'
             + f'<div style="position:absolute;left:666px;right:64px;top:510px">'
             + box('Pamiętaj', 'W Hiszpanii najważniejszy dzień dla dzieci to <b>6 stycznia</b>. Wiele rodzin daje drobny prezent 25.12, a główny – od Króli.', RED)
             + '<div style="height:16px"></div>'
             + box('Daty w Twojej gminie', 'Wioski Mikołaja, pokazy świateł i cabalgaty gminy ogłaszają zwykle na przełomie listopada i grudnia. Podamy je w wydaniach o 8:00 i 19:00.', SAND, INKK, RED)
             + '</div>' + src('Ayuntamientos gmin Costa del Sol. Stan na 19.11.2026.'))
    return frame(n, N, 'Dla rodzin', inner)

def P_polska_wigilia(n, N):
    subs = [('Karp', 'dorada, lubina albo dorsz – świeże w każdej rybnej'),
            ('Barszcz', 'remolacha cocida – gotowane buraki w próżniowych opakowaniach'),
            ('Śledzie', 'arenque – w słoikach w sklepach z produktami ze Wschodu'),
            ('Kapusta i grzyby', 'chucrut i suszone grzyby – też w tych sklepach')]
    ss = ''.join(f'<div style="display:grid;grid-template-columns:190px 1fr;gap:16px;padding:13px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:28px;font-weight:600;color:{RED}">{E(a)}</div><div style="font-size:19px;line-height:1.4">{E(b)}</div></div>' for a, b in subs)
    inner = (photo('x_wig.jpg', 0, 0, 470, 1350, '30% 50%')
             + f'<div style="position:absolute;left:470px;top:0;width:10px;height:1350px;background:{GOLD}"></div>'
             + cap('Wigilijny stół. Fot. Przykuta / Wikimedia Commons, CC BY-SA 3.0', 24, 1300, 430)
             + f'<div style="position:absolute;left:530px;right:64px;top:70px">{kick("Dla Polaków")}{H("Polska Wigilia <i style=\'color:"+RED+"\'>na wybrzeżu</i>", 60)}{rule()}'
             + dc('Dwanaście potraw zrobisz i w Andaluzji. Resztę produktów kupisz w sklepach z Europy Wschodniej – są m.in. w Torremolinos, Fuengiroli i Marbelli.')
             + f'<div style="margin-top:6px">{hdr("Czym zastąpić", 30, GRN)}{ss}</div>'
             + '<div style="height:18px"></div>'
             + box('Pasterka', 'W Wigilię o północy kościoły odprawiają <b>Misa del Gallo</b>. O mszach po polsku informują polskie parafie i duszpasterstwa – sprawdź u nich.', GRN)
             + '<div style="height:14px"></div>'
             + box('Opłatek', 'W Hiszpanii tej tradycji nie ma – przywieź go z Polski.', SAND, INKK, RED)
             + '</div>' + f'<div style="position:absolute;left:530px;right:64px;bottom:84px;font-size:13px;color:{MUT}">Stan na 19.11.2026.</div>')
    return frame(n, N, 'Dla Polaków', inner)

def P_prezenty(n, N):
    gifts = [('Oliwa z oliwek', 'Andaluzja to największy producent oliwy w Hiszpanii. Szukaj napisu „virgen extra” i daty zbioru.'),
             ('Turrón', 'Twardy z Alicante albo miękki z Jijony – w każdym supermarkecie.'),
             ('Mantecados z Estepy', 'Kruche ciastka z oznaczeniem pochodzenia – od listopada wszędzie.'),
             ('Wino Málaga', 'Słodkie wino z oznaczeniem DO Málaga, idealne do deseru.'),
             ('Pasas de Málaga', 'Rodzynki z Axarquíi, suszone na słońcu – z chronionym pochodzeniem.'),
             ('Ceramika andaluzyjska', 'Malowane talerze i miski – kupisz na targach i w miasteczkach w głębi lądu.')]
    gg = ''.join(f'<div style="padding:24px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:34px;font-weight:600;color:{[RED, GRN][i % 2]}">{E(a)}</div><div style="font-size:21px;line-height:1.45;color:#4A443D;margin-top:3px">{E(b)}</div></div>' for i, (a, b) in enumerate(gifts))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Do walizki")}{H("Prezenty <i style=\'color:"+RED+"\'>z Hiszpanii</i>", 86)}'
             f'<div style="font-size:22px;color:{MUT};margin-top:10px">Co przywieźć rodzinie do Polski – smaki i rzeczy z Andaluzji</div>{rule()}</div>'
             + f'<div style="position:absolute;left:64px;top:330px;width:560px;display:grid;grid-template-columns:1fr 1fr;gap:0 30px">{gg}</div>'
             + f'<img src="file://{PH}x_turron.jpg" style="position:absolute;left:670px;top:330px;width:346px;height:346px;object-fit:cover;border-radius:50%;border:6px solid #F2C14E">'
             + cap('Turrón. Fot. Juan Emilio Prades Bel / Wikimedia Commons, CC BY 4.0', 670, 690, 346)
             + f'<div style="position:absolute;left:670px;right:64px;top:740px">'
             + box('Na lotnisku', 'Oliwę, wino i inne płyny powyżej 100 ml pakuj do <b>bagażu rejestrowanego</b>. Butelki owiń ubraniem albo folią bąbelkową.', RED)
             + '<div style="height:14px"></div>'
             + box('Wskazówka', 'Słodycze z oznaczeniem pochodzenia mają na opakowaniu znaczek IGP lub DOP – to gwarancja, że są z danego regionu.', SAND, INKK, RED)
             + '</div>' + src('Junta de Andalucía; Consejos Reguladores DO Málaga, IGP Mantecados de Estepa, DOP Pasas de Málaga; Aena. Stan na 19.11.2026.'))
    return frame(n, N, 'Do walizki', inner)

def P_praktycznie(n, N):
    days = [('7.12', 'poniedziałek', 'Dzień Konstytucji (przeniesiony) – dzień wolny'), ('8.12', 'wtorek', 'Niepokalane Poczęcie – dzień wolny'), ('24.12', 'czwartek', 'Wigilia – sklepy krócej'),
            ('25.12', 'piątek', 'Boże Narodzenie – dzień wolny'), ('31.12', 'czwartek', 'Sylwester – sklepy krócej'),
            ('1.01', 'piątek', 'Nowy Rok – dzień wolny'), ('6.01', 'środa', 'Trzech Króli – dzień wolny')]
    dd = ''.join(f'<div style="display:grid;grid-template-columns:120px 1fr;gap:16px;padding:20px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:40px;font-weight:600;color:{RED if "wolny" in c else GOLD};line-height:1">{a}</div><div><div style="font-size:14px;font-weight:800;letter-spacing:.18em;color:{MUT}">{b.upper()}</div><div style="font-size:21px">{E(c)}</div></div></div>' for a, b, c in days)
    tips = [('112', 'Numer alarmowy – działa też po angielsku.'),
            ('Apteka dyżurna', 'Farmacia de guardia – lista dyżurów na stronie Kolegium Farmaceutów w Maladze i na drzwiach aptek.'),
            ('Pociąg C1', 'Cercanías łączy Málagę, lotnisko, Torremolinos, Benalmádenę i Fuengirolę. W święta sprawdź rozkład na renfe.com.'),
            ('Parkowanie', 'Wieczorami przy iluminacjach centra są zakorkowane. Lepiej pociągiem lub autobusem.')]
    tt = ''.join(f'<div style="padding:20px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:32px;font-weight:600;color:{GRN}">{E(a)}</div><div style="font-size:21px;line-height:1.45;margin-top:2px">{E(b)}</div></div>' for a, b in tips)
    inner = (photo('x_cerc.jpg', 0, 0, 1080, 400, '50% 70%')
             + f'<div style="position:absolute;left:0;right:0;top:0;height:400px;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.72) 100%)"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:240px;color:#fff">{kick("Praktycznie", "#F2C14E")}{H("Co warto <i style=\'color:#F2C14E\'>wiedzieć</i>", 80, "#fff")}</div>'
             + f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.9)">Cercanías C1. Fot. Tyk / Wikimedia Commons, domena publiczna</div>'
             + f'<div style="position:absolute;left:64px;top:440px;width:450px">{hdr("Dni wolne i krótsze", 30, RED)}{dd}'
             + f'<div style="font-size:16px;color:{MUT};margin-top:10px">Od 5 do 8.12 – cztery dni wolne z rzędu. 26.12 w Andaluzji to zwykły dzień.</div></div>'
             + f'<div style="position:absolute;left:566px;right:64px;top:440px">{hdr("Przyda się", 30, GRN)}{tt}</div>'
             + src('BOE; Junta de Andalucía – kalendarz świąt 2026; Renfe; Colegio de Farmacéuticos de Málaga. Stan na 19.11.2026.'))
    return frame(n, N, 'Praktycznie', inner)

def P_konkurs(n, N):
    steps = [('1', 'Obserwuj', '@solysol.pl na Instagramie lub stronę Sol y Sól na Facebooku.'),
             ('2', 'Odpowiedz w komentarzu', 'pod postem konkursowym: jaka polska tradycja świąteczna musi być u Ciebie na Costa del Sol?'),
             ('3', 'Czekaj na wyniki', 'Jury redakcji wybierze najciekawsze odpowiedzi. Wyniki 17.12.')]
    ss = ''.join(f'<div style="display:flex;gap:22px;padding:30px 0;border-top:1px solid rgba(255,246,229,.25)"><div style="{CG}font-size:80px;font-weight:600;color:{RED};line-height:.85;min-width:56px">{a}</div><div><div style="font-size:30px;font-weight:700">{E(b)}</div><div style="font-size:23px;line-height:1.45;opacity:.9;margin-top:4px">{E(c)}</div></div></div>' for a, b, c in steps)
    dates = ''.join(f'<div style="flex:1;border:2px solid {RED};padding:18px 10px;text-align:center"><div style="{CG}font-size:46px;font-weight:600;color:{RED}">{a}</div><div style="font-size:17px;margin-top:4px">{b}</div></div>' for a, b in [('1.12', 'start'), ('15.12', 'koniec zgłoszeń'), ('17.12', 'wyniki'), ('23.12', 'nagrody u Was')])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:70px">{kick("Konkurs")}{H("Wygraj <i style=\'color:"+RED+"\'>świąteczny upominek</i>", 86)}'
             f'<div style="font-size:24px;line-height:1.45;margin-top:16px;opacity:.92">Lokalne firmy z wybrzeża przygotowały upominki dla czytelników Sol y Sól. Pełną listę nagród i fundatorów pokażemy 1 grudnia.</div>{rule()}'
             f'{ss}<div style="display:flex;gap:12px;margin-top:26px">{dates}</div>'
             f'<div style="margin-top:34px;background:{RED};color:#123D2B;padding:24px 28px"><div style="font-size:15px;font-weight:800;letter-spacing:.2em">MASZ FIRMĘ NA WYBRZEŻU?</div><div style="{CG}font-size:32px;font-weight:600;line-height:1.25;margin-top:6px">Dołącz ze swoim upominkiem – napisz do nas w wiadomości do 28.11.</div></div>'
             f'<div style="margin-top:28px;font-size:17px;line-height:1.5;opacity:.75">Udział mogą wziąć osoby pełnoletnie, które odbiorą nagrodę na Costa del Sol. Regulamin w poście konkursowym. Konkurs nie jest sponsorowany, popierany ani administrowany przez Instagram, Facebook ani Metę.</div></div>')
    return frame(n, N, 'Konkurs', inner)


THEMES['noir'] = dict(PAPER='#15130F', INKK='#F4EDE2', MUT='#A89E90', SAND='rgba(255,255,255,.07)', RED='#E0874F', GRN='#C9A15A', GOLD='#E0874F', LINE='rgba(224,135,79,.35)', SUB='#D9D0C3', ZEB='rgba(255,255,255,.04)', CARD='rgba(255,255,255,.08)')

def P_zagaleta(n, N):
    nums = ''.join(f'<div style="border-top:2px solid {c};padding-top:10px"><div style="{CG}font-size:46px;font-weight:600;line-height:1;color:{c}">{a}</div><div style="font-size:16px;line-height:1.3;margin-top:4px;color:{MUT}">{b}</div></div>' for a, b, c in [
        ('900 ha', 'strzeżonych wzgórz w gminie Benahavís', RED), ('270 ha', 'ziemi spółki zarządzającej – nowy właściciel od 12.2024', GRN),
        ('420', 'domów w planie, do tego działka pod hotel', GOLD), ('2', 'pola golfowe, stadnina i lądowisko dla helikopterów', RED)])
    inner = (photo('villa4.jpg', 0, 0, 1080, 600, '50% 55%')
             + f'<div style="position:absolute;left:0;right:0;top:0;height:600px;background:linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.05) 50%,rgba(0,0,0,.82) 100%)"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:360px;color:#fff">{kick("Na długie wieczory · Benahavís", "#F2C14E")}{H("Kto naprawdę kupił <i style=\'color:#F2C14E\'>La Zagaletę?</i>", 80, "#fff")}</div>'
             + f'<div style="position:absolute;right:30px;top:22px;font-size:13px;color:rgba(255,255,255,.9)">Zdjęcie ilustracyjne. Fot. Max Harlynking / Unsplash</div>'
             + f'<div style="position:absolute;left:64px;top:640px;width:560px">'
             + dc('Na wybrzeżu krąży plotka, że ktoś wykupił wszystkie działki w najbardziej ekskluzywnym osiedlu Europy. Prawda jest mniej filmowa, ale równie ciekawa.')
             + p('W grudniu 2024 r. zagraniczny fundusz przejął 100% spółki, która zarządza La Zagaletą i ma tam wolne grunty. Kwoty transakcji nie ujawniono.', 20)
             + p('Prywatne wille i działki nadal należą do swoich właścicieli – i dalej są w sprzedaży. Działki o pow. 4–13 tys. m² kosztują w ofertach zwykle 3–5,5 mln €.', 20)
             + pull('Nie kupiono domów – kupiono spółkę i jej ziemię.', GRN)
             + '</div>'
             + f'<div style="position:absolute;left:670px;right:64px;top:630px"><div style="display:grid;grid-template-columns:1fr;gap:10px">{nums}</div>'
             + '<div style="height:14px"></div>'
             + box('Co dalej?', 'Nowy właściciel zapowiada rozbudowę osiedla i markę La Zagaleta za granicą.', SAND, INKK, RED)
             + '</div>' + src('El Español, Gulf Business, Idealista (12.2024–01.2025); oferty Málaga MLS (11.2026).'))
    return frame(n, N, 'Na długie wieczory', inner)

def P_ap7(n, N):
    nums = ''.join(f'<div style="border-top:2px solid {c};padding-top:12px"><div style="{CG}font-size:56px;font-weight:600;line-height:1;color:{c}">{a}</div><div style="font-size:18px;font-weight:700;margin-top:6px">{b}</div><div style="font-size:16px;line-height:1.35;color:{MUT};margin-top:2px">{d}</div></div>' for a, b, d, c in [
        ('11 233', 'nowych mieszkań na sprzedaż', '14 gmin wybrzeża, III kw. 2026 – co piąte w Hiszpanii', RED),
        ('ok. 120 tys.', 'aut dziennie na A-7', 'między Málagą a Marbellą', GRN),
        ('40 682', 'aut dziennie na płatnej AP-7', 'rekord 2025, latem opłata +63%', GOLD),
        ('70+', 'pól golfowych', 'najwięcej w kontynentalnej Europie', RED)])
    sc = ''.join(f'<div style="display:flex;gap:18px;padding:16px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:52px;font-weight:600;color:{RED};line-height:.85;min-width:40px">{i}</div><div><div style="font-size:21px;font-weight:700">{E(a)}</div><div style="font-size:18px;line-height:1.4;color:#4A443D;margin-top:3px">{E(b)}</div></div></div>' for i, (a, b) in enumerate([
        ('Pociąg', 'Studium dopiero w kwietniu 2027 r., a na budowę (ponad 6,5 mld €) nie ma pieniędzy.'),
        ('Nowa droga albo trzeci pas', 'Między A-7 a AP-7 są pola golfowe i osiedla – miejsca brak.'),
        ('Darmowa AP-7', 'Rząd mówi „nie” – koncesja trwa do 2046 i 2054 r.')], 1))
    inner = (photo('costaaer.jpg', 0, 0, 1080, 470, '45% 50%')
             + f'<div style="position:absolute;left:0;right:0;top:0;height:470px;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba(0,0,0,.8) 100%)"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:250px;color:#fff">{kick("Na długie wieczory · Costa del Sol", "#F2C14E")}{H("Korek <i style=\'color:#F2C14E\'>do 2046 roku?</i>", 88, "#fff")}</div>'
             + f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.9)">Wybrzeże między Marbellą a Fuengirolą. Fot. Mike McBey / Wikimedia Commons, CC BY 2.0</div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:500px;font-size:23px;line-height:1.45">Darmowa A-7 stoi w korkach, płatna AP-7 latem drożeje, pociągu nie ma. A pomiędzy nimi – <b>pola golfowe i osiedla</b>. Gdzie zmieścić nową drogę?</div>'
             + f'<div style="position:absolute;left:64px;top:610px;width:440px;display:grid;grid-template-columns:1fr;gap:16px">{nums}</div>'
             + f'<div style="position:absolute;left:556px;right:64px;top:610px">{hdr("Jakie perspektywy?", 34, RED)}{sc}'
             + '<div style="height:16px"></div>'
             + box('Zdaniem redakcji', 'Bez pociągu korki będą rosły szybciej niż drogi. Kupujesz dom? Sprawdź, ile naprawdę jedziesz w godzinach szczytu.', GRN)
             + '</div>' + src('Brains RE (III kw. 2026), Savills, El Debate, El Español, El Independiente, Esdiario, Olive Press, Euro Weekly News (2025–2026).'))
    return frame(n, N, 'Na długie wieczory', inner)

def P_crime(n, N):
    tl = ''.join(f'<div style="display:grid;grid-template-columns:210px 1fr;gap:18px;padding:14px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:36px;font-weight:600;color:{RED};line-height:1">{a}</div><div style="font-size:19px;line-height:1.4">{E(b)}</div></div>' for a, b in [
        ('1978', 'Wygasa stara umowa o ekstradycji między Hiszpanią a Wielką Brytanią.'),
        ('lata 80.', 'Dziennikarz David Baird tytułuje artykuł „Costa del Crime” – nazwa zostaje.'),
        ('22.07.1985', 'W Londynie podpisano nową umowę. Weszła w życie 1.07.1986 – ale nie działała wstecz.'),
        ('dziś', 'Oba kraje wspólnie ścigają zbiegów w akcji Operation Captura.')])
    fld = ''.join(f'<div style="display:grid;grid-template-columns:150px 1fr;padding:9px 0;border-bottom:1px dashed rgba(27,23,20,.35)"><span style="font-weight:800;font-size:15px;letter-spacing:.12em;color:#7A5B3A">{a}</span><span style="font-size:20px;color:#1b1714">{b}</span></div>' for a, b in [
        ('NAZWISKO', 'Monzer al-Kassar'), ('PSEUDONIM', '„Książę Marbelli”'), ('ADRES', 'rezydencja w Marbelli'),
        ('ZATRZYMANY', '06.2007, lotnisko w Madrycie'), ('WYROK', '30 lat – sąd w Nowym Jorku, 02.2009')])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Na długie wieczory · Zagadki kryminalne")}{H("Costa <i style=\'color:"+RED+"\'>del Crime</i>", 96)}'
             f'<div style="font-size:23px;line-height:1.45;margin-top:14px;color:#4A443D">Przez lata brytyjscy przestępcy mogli uciekać na wybrzeże bez strachu przed ekstradycją. Tak powstała nazwa, która przylgnęła do Costa del Sol.</div>{rule()}{tl}</div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:660px;background:#E8D9BC;color:#1b1714;padding:26px 30px 22px;transform:rotate(-1deg);box-shadow:0 20px 40px rgba(0,0,0,.45)">'
             + f'<div style="position:absolute;left:0;top:-30px;width:230px;height:32px;background:#E8D9BC;border-radius:10px 10px 0 0"></div>'
             + f'<div style="font-size:15px;font-weight:800;letter-spacing:.24em;color:#9E2B25">AKTA · MARBELLA</div>'
             + f'<div style="{CG}font-size:46px;font-weight:600;line-height:1.05;margin:6px 0 10px">Kim był „Książę Marbelli”?</div>'
             + f'<div style="display:grid;grid-template-columns:1fr 330px;gap:26px"><div>{fld}<div style="font-size:18px;line-height:1.45;margin-top:12px">Miał sprzedać ponad 12 tys. sztuk broni kolumbijskiej partyzantce FARC. Kupcami byli w rzeczywistości informatorzy amerykańskiej agencji DEA – część spotkań odbyła się w jego rezydencji w Marbelli.</div></div>'
             + f'<div style="position:relative"><img src="file://{PH}villa0.jpg" style="width:330px;height:300px;object-fit:cover;filter:grayscale(1) contrast(1.1);border:10px solid #fff;box-shadow:0 8px 20px rgba(0,0,0,.3);transform:rotate(2deg)"><div style="font-size:13px;font-style:italic;margin-top:8px">Zdjęcie ilustracyjne. Fot. Frames For Your Heart / Unsplash</div>'
             + f'<div style="position:absolute;right:-6px;top:200px;border:4px solid #9E2B25;color:#9E2B25;font-weight:900;font-size:34px;letter-spacing:.12em;padding:6px 16px;transform:rotate(-12deg);background:rgba(232,217,188,.6)">SKAZANY</div></div></div></div>'
             + src('Traktat ekstradycyjny (Treaty Series 40/1986), Hansard (1985), Olive Press, NCA, gov.uk; DEA (2008, 2009), AFP, CBS News, NBC News.'))
    return frame(n, N, 'Zagadki kryminalne', inner)

def P_mafie(n, N):
    nums = ''.join(f'<div style="border-top:2px solid {RED};padding-top:12px"><div style="{CG}font-size:64px;font-weight:600;line-height:1;color:{RED}">{a}</div><div style="font-size:19px;font-weight:700;margin-top:6px">{b}</div><div style="font-size:16px;line-height:1.35;color:{MUT};margin-top:2px">{d}</div></div>' for a, b, d in [
        ('32', 'strzelaniny', 'od 01.2024 do 05.2025 – 8 zabitych, 42 rannych'),
        ('26', 'zabójstw w prowincji', 'w 2025 r. – najwięcej od 2015 r.'),
        ('7', 'rozbitych gangów', 'w miesiąc (10–11.2025), 55 zatrzymanych'),
        ('04.2024', 'Plan Marbella', 'po 7 strzelaninach w 2 miesiące')])
    inner = (photo('pol.jpg', 0, 0, 1080, 560, '50% 55%')
             + f'<div style="position:absolute;left:0;right:0;top:0;height:560px;background:linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,0) 22%,rgba(21,19,15,.75) 58%,rgba(21,19,15,1) 100%)"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:330px">{kick("Na długie wieczory · Zagadki kryminalne")}{H("Raj <i style=\'color:"+RED+"\'>dla mafii?</i>", 100)}</div>'
             + f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.9)">Zdjęcie ilustracyjne. Fot. Contando Estrelas / Wikimedia Commons, CC BY-SA 2.0</div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:600px;font-size:23px;line-height:1.45">Słońce, porty jachtowe i luksusowe osiedla przyciągają nie tylko turystów. Policja mówi o międzynarodowych gangach, porachunkach w biały dzień i coraz młodszych zabójcach.</div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:730px;display:grid;grid-template-columns:1fr 1fr;gap:24px 40px">{nums}</div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:1060px">'
             + box('Co to znaczy dla Ciebie', 'To głównie porachunki między gangami narkotykowymi, a nie ataki na turystów. Najwięcej strzelanin było w Maladze i Marbelli. W 2026 r. rząd znów wysłał na wybrzeże dodatkowe patrole.', 'rgba(255,255,255,.07)', INKK, RED)
             + '</div>' + src('MSW Hiszpanii (11.2025), El Debate, El Español, Vozpópuli, ARA (2025–2026).'))
    return frame(n, N, 'Zagadki kryminalne', inner)


def P_banus(n, N):
    guests = ''.join(f'<div style="display:flex;gap:16px;padding:13px 0;border-top:1px solid #CFC5B5"><div style="font-size:30px;line-height:1;min-width:38px">{a}</div><div><div style="font-size:21px;font-weight:700">{E(b)}</div><div style="font-size:17px;line-height:1.35;color:#4A443D;margin-top:2px">{E(c)}</div></div></div>' for a, b, c in [
        ('👑', 'Książę Rainier i Grace Kelly', 'para książęca Monako'),
        ('👑', 'Juan Carlos i Zofia', 'przyszli król i królowa Hiszpanii'),
        ('✈️', 'Hugh Hefner', 'przyleciał prywatnym Boeingiem 707'),
        ('🎬', 'Roman Polański i Aga Chan', 'reżyser i przywódca duchowy ismailitów'),
        ('❤️', 'Christiaan Barnard', 'kardiochirurg, autor pierwszego przeszczepu serca'),
        ('🎤', 'Julio Iglesias', 'młody piosenkarz śpiewał dla gości')])
    inner = (photo('banus.jpg', 0, 0, 1080, 560, '50% 50%')
             + f'<div style="position:absolute;left:0;right:0;top:0;height:560px;background:linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 25%,rgba(0,0,0,.55) 55%,rgba(0,0,0,.88) 100%)"></div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:330px;color:#fff">{kick("Na długie wieczory · Kto tu przylatywał?", "#F2C14E")}{H("Grace Kelly, Hefner <i style=\'color:#F2C14E\'>i Polański</i>", 78, "#fff")}</div>'
             + f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.9)">Puerto Banús dziś. Fot. Tomas Fano / Wikimedia Commons, CC BY-SA 2.0</div>'
             + f'<div style="position:absolute;left:64px;top:600px;width:440px">'
             + dc('2 sierpnia 1970 r. José Banús wydał przyjęcie na otwarcie swojego portu pod Marbellą. Na liście gości było 1700 nazwisk – to do dziś najsłynniejsza impreza w historii wybrzeża.')
             + p('Puerto Banús wygląda jak stara rybacka wioska z białymi domkami. Nic bardziej mylnego – zbudowano je od zera właśnie w 1970 r.', 20)
             + f'<div style="display:flex;gap:16px;margin-top:8px"><div style="background:{RED};color:#fff;padding:18px 20px;flex:1"><div style="{CG}font-size:54px;font-weight:600;line-height:1">1700</div><div style="font-size:16px;margin-top:4px">gości na przyjęciu</div></div>'
             + f'<div style="background:{GRN};color:#fff;padding:18px 20px;flex:1"><div style="{CG}font-size:54px;font-weight:600;line-height:1">707</div><div style="font-size:16px;margin-top:4px">Boeing Hefnera</div></div></div>'
             + '</div>'
             + f'<div style="position:absolute;left:556px;right:64px;top:600px">{hdr("Na liście gości", 34, RED)}{guests}</div>'
             + src('Archivo Histórico Provincial de Málaga (Junta de Andalucía), andalucia.com, Olive Press (2020), Terra Meridiana, puerto-banus.com.'))
    return frame(n, N, 'Na długie wieczory', inner)

THEME_SEQ = ['light','light','green','light','light','light','light','red','light','light','light','light','light','light','red','light','light','light','noir','light','light','light','green','light']
PAGES = [P_cover, P_liczby, P_kalendarz, P_malaga, P_marbella, P_fue_est, P_dzieci, P_gordo, P_mit, P_pl_es, P_polska_wigilia, P_slodycze, P_prezenty, P_sylwester, P_ciekawostki, P_banus, P_zagaleta, P_ap7, P_crime, P_praktycznie, P_slowniczek, P_quiz, P_konkurs, P_koniec]
