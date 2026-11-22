# Scenariusz Zagadki #7 – tekst dla lektora (liczby słownie). Rozdziały: (część, tytuł, akapity)
CH = [
(1,"Otwarcie",[
"Piętnasty czerwca tysiąc dziewięćset dziewięćdziesiątego pierwszego roku. Marbella ma nowego burmistrza. Biznesmena z Madrytu, prezesa klubu piłkarskiego Atlético, człowieka, którego cała Hiszpania zna z telewizji i z ostrych słów.",
"Przez jedenaście lat będzie rządził tym miastem jak swoim królestwem. Zbuduje nową Marbellę. Zostawi po sobie wyroki, długi i tysiące budynków postawionych wbrew prawu.",
"To Sol i Sól i „Zagadki Costa del Sol”. Odcinek siódmy. Jesús Gil – Marbella jako jego królestwo."]),
(1,"Restauracja, która runęła",[
"Jesús Gil y Gil urodził się w tysiąc dziewięćset trzydziestym trzecim roku w El Burgo de Osma, w prowincji Soria. Młodo zaczyna robić interesy w budownictwie.",
"I tu pierwsza mroczna karta. W czerwcu tysiąc dziewięćset sześćdziesiątego dziewiątego roku w Los Ángeles de San Rafael pod Segowią zawala się restauracja zbudowana przez jego firmę. Ginie pięćdziesiąt osiem osób.",
"Okazuje się, że budowano bez architekta i bez projektu. Gil zostaje skazany na pięć lat więzienia. Po półtora roku wychodzi na wolność dzięki ułaskawieniu generała Franco.",
"Zdaniem redakcji to zdanie, które warto zapamiętać. Bo ten sam schemat, budować szybko i martwić się przepisami później, wróci w tej historii jeszcze nie raz."]),
(1,"Prezes i showman",[
"W tysiąc dziewięćset osiemdziesiątym siódmym roku Gil zostaje prezesem Atlético Madryt. Klub pod jego rządami zdobywa Puchar Króla, a w sezonie tysiąc dziewięćset dziewięćdziesiąt pięć, dziewięćdziesiąt sześć także mistrzostwo Hiszpanii.",
"Gil kłóci się z sędziami, z dziennikarzami, z politykami. Ma własny program w telewizji.",
"W tysiąc dziewięćset dziewięćdziesiątym pierwszym roku zakłada własną partię. Grupo Independiente Liberal. W skrócie GIL. Jak jego nazwisko."]),
(2,"Miasto w jego rękach",[
"Wybory w maju tysiąc dziewięćset dziewięćdziesiątego pierwszego roku. GIL zdobywa w Marbelli absolutną większość. Nowy burmistrz obiecuje porządek i inwestycje. Ruszają budowy.",
"Wielu mieszkańców jest zachwyconych. GIL wygrywa także kolejne wybory, w tysiąc dziewięćset dziewięćdziesiątym piątym i w tysiąc dziewięćset dziewięćdziesiątym dziewiątym roku. Partia zdobywa też władzę w innych miastach na wybrzeżu.",
"Ale za fasadą dzieje się coś innego. Grunty rolne zmieniają się w działki budowlane. Powstają budynki bez wymaganych pozwoleń. A kasa miasta zaczyna świecić pustkami."]),
(2,"Koszulki za miliony",[
"Pierwsza sprawa, która go dosięgnie, brzmi niewinnie. Koszulki. Piłkarze Atlético grają z napisem Marbella na piersi. Za tę reklamę miasto płaci klubowi, którego prezesem jest burmistrz. Czterysta pięćdziesiąt milionów peset.",
"W październiku dwa tysiące roku sąd w Maladze uznaje to za przestępstwo urzędnicze. Kara: dwadzieścia osiem lat zakazu pełnienia funkcji publicznych i sześć miesięcy aresztu.",
"W kwietniu dwa tysiące drugiego roku Sąd Najwyższy podtrzymuje wyrok. Jesús Gil musi oddać fotel burmistrza. Po jedenastu latach."]),
(2,"Areszt i kolejne zarzuty",[
"To nie był jego pierwszy pobyt za kratami w tamtych latach. W styczniu tysiąc dziewięćset dziewięćdziesiątego dziewiątego roku trafia do aresztu tymczasowego w sprawie zarzutów dotyczących pieniędzy miasta.",
"W kwietniu dwa tysiące drugiego roku znów spędza kilka dni w areszcie, tym razem w śledztwie dotyczącym blisko dwudziestu siedmiu milionów euro z kasy Marbelli. Wychodzi za kaucją.",
"Do tego dochodzi sprawa finansów Atlético. W lutym dwa tysiące trzeciego roku Audiencia Nacional skazuje go w pierwszej instancji. Kilka miesięcy później Gil odchodzi z klubu."]),
(3,"Następca",[
"Fotel burmistrza przejmuje jego wieloletni współpracownik, Julián Muñoz. W ratuszu wciąż pracuje człowiek od urbanistyki, Juan Antonio Roca. O tym, co stało się z nimi dalej, opowiadaliśmy w odcinku o aferze Malaya.",
"A Jesús Gil? W maju dwa tysiące czwartego roku doznaje udaru. Umiera czternastego maja w Madrycie. Ma siedemdziesiąt jeden lat. Na jego pogrzeb przychodzą tłumy."]),
(3,"Królestwo po królu",[
"Dwa lata później rusza operacja Malaya, a rząd rozwiązuje radę Marbelli. Jesús Gil nie żyje i nigdy nie stanął przed tym sądem. Ale prasa pisze, że to w latach jego rządów powstał system, który śledczy rozbierają na części.",
"Szacunki mówią o kilkunastu tysiącach domów i apartamentów zbudowanych na podstawie nielegalnych licencji. A miasto przez lata spłaca długi.",
"Zdaniem redakcji Jesús Gil to najtrudniejsza postać w historii Marbelli. Dla jednych człowiek, który posprzątał miasto i ściągnął pieniądze. Dla innych symbol tego, że na Costa del Sol prawo przez lata było tylko sugestią. Fakty są takie: wyrok za koszulki, wyrok za Atlético w pierwszej instancji i miasto, które wciąż płaci rachunki."]),
(3,"Zakończenie",[
"To były „Zagadki Costa del Sol”. Jeśli chcecie kolejną historię, zostawcie łapkę w górę i zasubskrybujcie kanał. W następnym odcinku, w niedzielę dziesiątego stycznia, opowiemy o Isabel Pantoji i Juliánie Muñozie. Miłość, władza i wyrok.",
"Sol i Sól. Wszystko, co ważne na Costa del Sol. Do usłyszenia w niedzielę o osiemnastej."]),
]
def part(n): return "\n\n".join(p for c in CH if c[0]==n for p in c[2])
if __name__=="__main__":
    for n in (1,2,3): t=part(n); print(n, len(t), len(t.split()))
