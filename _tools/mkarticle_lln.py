# usage (z katalogu repo): python3 _tools/mkarticle_lln.py post.json  – post = {"id":..., "data":{...}} z aplikacji Redakcja (brand "lln")
# zapisuje lln/articles/<id>.json i dopisuje id do lln/articles/index.json; zdjęcie: lln/<id>/hero.jpg (skopiuj wcześniej z aplikacji img/<id>/hero.jpg)
import json,sys,os,re
p=json.load(open(sys.argv[1])); d=p.get('data',p); pid=p.get('id') or d['id']
assert d.get('brand')=='lln' and d.get('articleHtml'), 'to nie jest wpis LLN z articleHtml'
html=d['articleHtml']
excerpt=d.get('excerpt') or re.sub(r'\s+',' ',re.sub('<[^>]+>','',html.split('</p>')[0]))[:240]
img=f'lln/{pid}/hero.jpg' if os.path.exists(f'lln/{pid}/hero.jpg') else ''
art={'rev':int(d.get('articleRev',1)),'id':pid,'title':d.get('articleTitle') or d['title'],'slug':d.get('articleSlug',''),
     'category':d.get('articleCategory','Wybór ofert'),'tags':d.get('articleTags',['Costa del Sol']),'excerpt':excerpt,'html':html,'image':img}
os.makedirs('lln/articles',exist_ok=True)
json.dump(art,open(f'lln/articles/{pid}.json','w'),ensure_ascii=False,indent=1)
f='lln/articles/index.json'; idx=json.load(open(f)) if os.path.exists(f) else []
if pid not in idx: idx.append(pid)
json.dump(idx,open(f,'w'))
print('lln article',pid,img)
