# Gwiazdy na Costa del Sol – odcinek długi: Książę, który wymyślił Marbellę
CH = [
(1,"Otwarcie",[
"Zima, rok tysiąc dziewięćset czterdziesty szósty. Z pałacu pod Madrytem wyjeżdża na południe stary Rolls-Royce Phantom. W środku siedzi niemiecki arystokrata, książę Max von Hohenlohe. Jedzie zobaczyć wybrzeże, o którym opowiadał mu kuzyn. Morze, sosny, zapach fig.",
"Gdzieś między Malagą a Gibraltarem zatrzymuje się na piknik w sosnowym lesie nad samą plażą. Niedaleko leży Marbella. Mała, biała miejscowość rybaków.",
"Nikt wtedy nie przypuszcza, że ten jeden piknik zmieni to miejsce na zawsze. Jak to się stało, że rybacka wioska stała się Marbellą gwiazd? I kim był człowiek, którego tu nazywano po prostu księciem?",
"To Sol i Sól i seria „Gwiazdy na Costa del Sol”. Odcinek pierwszy. Książę, który wymyślił Marbellę."]),
(1,"Syn księcia",[
"Ten człowiek to Alfonso, syn księcia Maxa. Urodził się w Madrycie w tysiąc dziewięćset dwudziestym czwartym roku. Ojciec pochodził ze starego niemieckiego rodu Hohenlohe.",
"Rok po pikniku ojciec wysyła Alfonsa na wybrzeże z prostym zadaniem. Ma kupić ziemię w miejscu, które tak mu się spodobało. Alfonso jest młody, ma dwadzieścia trzy lata. Przyjeżdża, rozgląda się i kupuje starą finkę wśród drzew figowych i sosen. Posiadłość nazywa się Santa Margarita.",
"Na początku to po prostu rodzinna kryjówka nad morzem. Miejsce na wakacje dla Hohenlohe i ich przyjaciół. A przyjaciele, jak to w takich rodzinach, mają nazwiska z pierwszych stron gazet."]),
(2,"Dwadzieścia pokoi",[
"Goście przyjeżdżają coraz częściej. I zostają coraz dłużej. Alfonso dochodzi do wniosku, że skoro i tak przyjmuje ludzi pod swoim dachem, może zrobić z tego hotel.",
"W tysiąc dziewięćset pięćdziesiątym czwartym roku otwiera Marbella Club. Na początku ma dwadzieścia pokoi. Jadalnia i bar mieszczą się w starym domu na fince. Nie ma tu przepychu. Są ogrody, sosny, kilka kroków do plaży i atmosfera prywatnego przyjęcia.",
"Zdaniem redakcji właśnie w tym tkwił sekret. To nie miał być kolejny hotel. To miał być klub dla znajomych, do którego każdy chciał należeć."]),
(2,"Ślub w Wenecji",[
"Rok później o Alfonsie mówi cała Europa. We wrześniu tysiąc dziewięćset pięćdziesiątego piątego roku w Wenecji żeni się z księżniczką Irą von Fürstenberg. Panna młoda ma piętnaście lat. Jej matka pochodzi z rodziny Agnellich, właścicieli Fiata.",
"Zdjęcia z weneckiego ślubu obiegają gazety na całym świecie. Para ma dwóch synów, ale małżeństwo nie przetrwa. Rozwodzą się w tysiąc dziewięćset sześćdziesiątym roku.",
"Ira pozostanie jednak związana z Marbellą przez całe życie. Media nazywały ją później księżniczką Marbelli."]),
(2,"Hrabia Rudi",[
"W grudniu tysiąc dziewięćset pięćdziesiątego szóstego roku do Marbelli przyjeżdża młody krewny Alfonsa. Rudolf von Schönburg, dla wszystkich po prostu hrabia Rudi. Pochodzi z Saksonii. Jego rodzina straciła majątek po drugiej wojnie światowej. Rudi właśnie skończył szkołę hotelarską w Szwajcarii.",
"Zaczyna jako zastępca dyrektora. Od tysiąc dziewięćset sześćdziesiątego pierwszego roku przez ponad dwadzieścia lat kieruje hotelem. Alfonso jest twarzą klubu, a Rudi pilnuje, żeby wszystko działało jak w zegarku.",
"Hrabia Rudi zmarł w Marbelli w październiku dwa tysiące dwudziestego szóstego roku. Miał dziewięćdziesiąt cztery lata. Do końca był związany z klubem."]),
(3,"Gwiazdy przyjeżdżają",[
"W latach pięćdziesiątych i sześćdziesiątych do Marbella Club zjeżdża śmietanka towarzyska. Przyjeżdżają między innymi Ava Gardner i Audrey Hepburn. W tysiąc dziewięćset sześćdziesiątym roku w okolicy klubu fotografowano Brigitte Bardot.",
"Według historii hotelu w latach sześćdziesiątych powstaje tu słynny salon szampański. Miejsce, w którym bawi się jet set z dala od fotoreporterów.",
"Hotel pisze, że pod koniec lat sześćdziesiątych Marbella zaczyna konkurować z Lazurowym Wybrzeżem i Saint-Tropez. A w tysiąc dziewięćset siedemdziesiątym roku kilka kilometrów dalej José Banús otwiera wielkim przyjęciem port Puerto Banús. Zdaniem redakcji bez klubu księcia ta wielka noc nie miałaby takich gości. O tamtej nocy opowiadamy w osobnym odcinku."]),
(3,"Ostatnie lata",[
"W latach dziewięćdziesiątych Alfonso sprzedaje swoje udziały w hotelu. Wyjeżdża w góry, do Rondy, i zaczyna nowy rozdział. Zakłada winnicę i robi wino.",
"Umiera w Marbelli dwudziestego pierwszego grudnia dwa tysiące trzeciego roku. Ma siedemdziesiąt dziewięć lat. Główna ulica, przy której stoi jego hotel, nosi dziś imię księcia Alfonsa von Hohenlohe.",
"Zdaniem redakcji był pierwszym, który zobaczył w rybackiej wiosce coś więcej."]),
(3,"Zakończenie",[
"W dwa tysiące dwudziestym czwartym roku Marbella Club świętował siedemdziesiąte urodziny. Z dwudziestu pokoi na dawnej fince wyrósł jeden z najbardziej znanych hoteli w Europie.",
"Zdaniem redakcji to tu narodziła się Marbella, jaką znamy. Wszystko zaczęło się od jednego pikniku i starego Rolls-Royce’a.",
"Jeśli podobała wam się ta historia, zostawcie łapkę w górę i zasubskrybujcie kanał. Napiszcie w komentarzu, kogo z dawnych gości chcielibyście spotkać w klubie. To był Sol i Sól. Wszystko, co ważne na Costa del Sol."]),
]
import re
def part(n): return "\n\n".join(p for c in CH if c[0]==n for p in c[2])
def tts(s):
    s=s.replace('Marbella Club','Marbeja Klab')
    for a,b in [('Marbellę','Marbeję'),('Marbelli','Marbei'),('Marbellą','Marbeją'),('Marbella','Marbeja'),('finkę','finkę'),('jet set','dżet set')]:
        s=s.replace(a,b)
    return s
if __name__=="__main__":
    for n in (1,2,3): t=part(n); print(n, len(tts(t)), len(t.split()))
