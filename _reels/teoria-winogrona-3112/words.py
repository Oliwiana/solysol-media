import json,re
raw="""Dwanaście 0.1|winogron 0.66|o 1.16|północy. 1.3|Skąd 2.42|naprawdę 2.82|się 3.32|wzięły? 3.48|Krąży 4.42|teoria, 4.82|że 5.38|to 5.56|sprytny 5.82|marketing. 6.3|W 7.38|1909 7.44|roku 8.82|rolnicy 9.22|spod 9.78|Alicante 10.02|mieli 10.62|ogromną 10.98|nadwyżkę 11.58|winogron. 12.1|Żeby 13.06|ją 13.26|sprzedać, 13.48|wymyślili 14.12|winogrona 15|szczęścia. 15.64|Co 16.74|jest 16.88|udokumentowane? 17.16|Kampania 18.5|z 18.96|1909 19.02|naprawdę 20.58|rozsławiła 21.16|zwyczaj 21.86|w 22.24|całej 22.34|Hiszpanii, 22.64|ale 23.54|madryckie 23.74|gazety 24.24|piszą 24.76|o 25.1|winogronach 25.18|już 25.8|w 25.96|1882 26.04|roku. 28.04|Bogate 28.78|rodziny 29.14|podpatrzyły 29.64|we 30.26|Francji 30.4|sylwestrowego 30.84|szampana 31.6|z 32.119|winogronami. 32.2|A 33.42|zwykli 33.58|Madrytczycy? 33.96|Gdy 35.1|ratusz 35.28|utrudnił 35.68|im 36.22|świętowanie 36.38|na 36.98|ulicach, 37.12|przyszli 37.84|na 38.24|Puerta 38.42|del 38.78|Sol 39|i 39.48|jedli 39.6|winogrona 39.88|na 40.92|złość 41.1|elitom. 41.46|Kpina 42.34|stała 42.98|się 43.28|tradycją. 43.44|Werdykt? 44.56|Częściowo 45.5|prawda. 46.08|Rolnicy 46.9|spopularyzowali 47.4|zwyczaj, 48.38|ale 49.06|go 49.28|nie 49.48|wymyślili. 49.66|A 50.78|Ty 50.9|wierzysz 51.46|w 51.9|winogrona 52.02|szczęścia? 52.52|Napisz 53.5|w 53.82|komentarzu. 53.9"""
W=[(w.rsplit(' ',1)[0],float(w.rsplit(' ',1)[1])/1.12) for w in raw.split('|')]
W[0]=('12',W[0][1])
KEY={'12','teoria,','marketing.','1909','Alicante','nadwyżkę','szczęścia.','szczęścia?','udokumentowane?','1882','Francji','szampana','Puerta','del','Sol','złość','elitom.','Kpina','tradycją.','Częściowo','prawda.','nie','wymyślili.','ratusz','Hiszpanii,'}
G=[];cur=[]
for w,t in W:
  cur.append([w,round(t,3),w in KEY])
  if re.search(r'[.,?!]$',w) or (len(cur)>=4 and w not in ('Puerta','del','na','w','z','o','A','i')):
    G.append(cur);cur=[]
if cur:G.append(cur)
json.dump(G,open('groups.json','w'),ensure_ascii=False)
print(len(G))
H=[]
for g in G:
  if len(g)==1 and H and len(H[-1])<=5 and g[0][0]!='Werdykt?': H[-1]+=g
  else: H.append(g)
json.dump(H,open('groups.json','w'),ensure_ascii=False)
for g in H: print(' '.join(w[0] for w in g))
