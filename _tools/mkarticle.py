# usage: python3 mkarticle.py post.json  (post = {"id":..., "data":{...}} or data with "id")
# writes articles/<id>.json and appends id to articles/index.json (run from repo root)
import json,sys,re,html,os
p=json.load(open(sys.argv[1])); d=p.get('data',p); pid=p.get('id') or d['id']
cap=d.get('fbCaption') or d.get('igCaption','')
lines=[l.rstrip() for l in cap.split('\n')]
# drop first line (emoji + category header), hashtags, "Więcej..." and links lines
body=[]
for i,l in enumerate(lines):
    s=l.strip()
    if i==0: continue
    if s.startswith('#') or s.lower().startswith('więcej') or 'solysol.pl' in s.lower() and len(s)<80: continue
    if s.lower().startswith('źródło'): continue
    body.append(s)
out=[];ul=[]
def flush():
    global ul
    if ul: out.append('<ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul>'); ul=[]
for s in body:
    m=re.match(r'^(▪️|✅|❌|•|-|\d+[\.\)]|\d️⃣)\s*(.*)',s)
    if m and m.group(2): ul.append(html.escape(m.group(2))); continue
    flush()
    if s: out.append(f'<p>{html.escape(s)}</p>')
flush()
src=d.get('sources','')
if src and src!='—': out.append(f'<p><em>Źródła: {html.escape(src)}</em></p>')
out.append('<p><strong>Sol y Sól</strong> – codzienne wiadomości z Costa del Sol po polsku. Obserwuj nas na <a href="https://www.instagram.com/solysol.pl/">Instagramie</a> i Facebooku.</p>')
tag=d.get('tag','')
cat='Wiadomości'
for k,v in [('Kryminal','Kryminalne'),('Costa bez filtra','Costa bez filtra'),('Nieruchom','Nieruchomości'),('firm','Biznes'),('Podatk','Biznes'),('Wybrzeże','Wybrzeże'),('Czy wiesz','Ciekawostki'),('Pytasz','Pytasz – odpowiadamy'),('Kalendarz','Kalendarz')]:
    if k.lower() in tag.lower(): cat=v;break
place=[t.strip() for t in tag.split('·')[1:]]
excerpt=re.sub(r'\s+',' ',' '.join(re.sub('<[^>]+>','',x) for x in out[:1]))[:240]
img=f'{pid}/fb.jpg' if os.path.exists(f'{pid}/fb.jpg') else (f'{pid}/ig-1.jpg' if os.path.exists(f'{pid}/ig-1.jpg') else (f'{pid}/okladka.jpg' if os.path.exists(f'{pid}/okladka.jpg') else ''))
art={'id':pid,'title':d['title'],'category':cat,'tags':['Costa del Sol']+place,'excerpt':excerpt,'html':'\n'.join(out),'image':img}
os.makedirs('articles',exist_ok=True)
json.dump(art,open(f'articles/{pid}.json','w'),ensure_ascii=False,indent=1)
idx=json.load(open('articles/index.json')) if os.path.exists('articles/index.json') else []
if pid not in idx: idx.append(pid)
json.dump(idx,open('articles/index.json','w'))
print('article',pid,cat,img)
