import json,os,random
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
from shots import SHOTS,HOOK
B='/home/claude/solysol-media/_photos/commons/'
def noir(im,W,H,crop=None):
    im=im.convert('RGB')
    if crop:
        w,h=im.size;im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im=ImageOps.fit(im,(W,H),Image.LANCZOS,centering=(0.5,0.45))
    g=ImageOps.grayscale(im);g=ImageOps.autocontrast(g,cutoff=1);g=ImageEnhance.Contrast(g).enhance(1.15)
    return g.convert('RGB')
cred=[];seen=set()
for i,(t,f,l,c) in enumerate(SHOTS):
    noir(Image.open(B+f),1056,982,c).save(f'img/{i:02d}.jpg',quality=85)
    if f not in seen:
        seen.add(f);d,fn=f.split('/');cc={x['file']:x for x in json.load(open(B+d+'/credits.json'))}[fn];cc['path']=f;cred.append(cc)
noir(Image.open(B+HOOK),1188,2112).save('img/hook.jpg',quality=88)
d,fn=HOOK.split('/');cc={x['file']:x for x in json.load(open(B+d+'/credits.json'))}[fn];cc['path']=HOOK;cred.append(cc)
json.dump(cred,open('credits.json','w'),ensure_ascii=False,indent=1)
print(len(SHOTS),'shots',len(cred),'files')
for c in cred: print(c['path'],'|',c['author'][:40],'|',c['license'])
