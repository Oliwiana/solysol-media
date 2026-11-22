import json,os
from PIL import Image,ImageOps,ImageEnhance
C='/home/claude/solysol-media/_photos/commons/'
# (start_orig, file, fx, fy, crop_frac(of max 9:16 crop), label)
S=[
(0.0,'uvas-nochevieja/05.jpg',.5,.5,1.0,''),
(2.42,'uvas-nochevieja/06.jpg',.55,1.0,0.65,''),
(4.42,'uvas-nochevieja/01.jpg',.4,.5,1.0,''),
(6.0,'uvas-nochevieja/02.jpg',.6,.5,0.8,''),
(7.38,'mediterranean-sea-relief-map/01.jpg',.131,.48,0.55,'Alicante · 1909'),
(9.22,'uvas-nochevieja/04.jpg',.5,.6,1.0,'nadwyżka winogron'),
(11.0,'uvas-nochevieja/03.jpg',.5,.5,1.0,''),
(13.06,'uvas-nochevieja/01.jpg',.75,.4,0.5,''),
(15.0,'uvas-nochevieja/06.jpg',.5,.8,0.6,'„winogrona szczęścia”'),
(16.74,'archivo-legajos-documentos/04.jpg',.5,.5,1.0,''),
(18.5,'newspaper-stack/02.jpg',.5,.5,1.0,'kampania · 1909'),
(20.6,'mediterranean-sea-relief-map/01.jpg',.1,.5,1.0,'cała Hiszpania'),
(23.4,'newspaper-stack/03.jpg',.5,.5,1.0,''),
(25.2,'typewriter-vintage/05.jpg',.45,.5,1.0,''),
(26.6,'loter-a-de-navidad/01.jpg',.5,.62,0.8,'Madryt · 1882'),
(28.7,'ronda-spain-1930s/04.jpg',.5,.5,1.0,''),
(30.5,'champagne-bottles/03.jpg',.5,.5,1.0,'Francja · szampan + winogrona'),
(32.2,'champagne-glasses-new-year/02.jpg',.35,.5,1.0,''),
(33.4,'gran-via-madrid-night/04.jpg',.5,.5,1.0,''),
(35.1,'calle-del-carmen-madrid/04.jpg',.5,.5,1.0,''),
(36.6,'gran-via-madrid-night/03.jpg',.5,.5,1.0,''),
(37.8,'loter-a-de-navidad/06.jpg',.5,.5,1.0,'Puerta del Sol'),
(39.5,'puerta-del-sol-madrid-christmas/06.jpg',.5,.5,1.0,''),
(40.9,'puerta-del-sol-madrid-christmas/05.jpg',.4,.5,1.0,''),
(42.3,'fireworks-night-spain/01.jpg',.6,.4,1.0,''),
(43.4,'fireworks-night-spain/03.jpg',.5,.5,1.0,''),
(44.5,'puerta-del-sol-madrid-christmas/02.jpg',.5,.5,1.0,''),
(46.5,'fireworks-harbour-night/02.jpg',.5,.5,1.0,''),
(48.4,'uvas-nochevieja/02.jpg',.3,.5,0.8,''),
(50.3,'fireworks-night-spain/04.jpg',.5,.5,1.0,''),
(52.0,'puerta-del-sol-madrid-christmas/01.jpg',.5,.5,1.0,''),
(53.6,'uvas-nochevieja/05.jpg',.35,.45,0.6,''),
]
out=[]
for i,(t,f,fx,fy,cf,lab) in enumerate(S):
  im=Image.open(C+f).convert('RGB');W,H=im.size
  r=9/16
  if W/H>r: ch=H;cw=H*r
  else: cw=W;ch=W/r
  cw*=cf;ch*=cf
  x=min(max(fx*W-cw/2,0),W-cw);y=min(max(fy*H-ch/2,0),H-ch)
  im=im.crop((int(x),int(y),int(x+cw),int(y+ch))).resize((1080,1920),Image.LANCZOS)
  im=ImageOps.grayscale(im);im=ImageOps.autocontrast(im,cutoff=1);im=ImageEnhance.Contrast(im).enhance(1.12)
  p=f'/home/claude/w/img/{i:02d}.jpg';im.save(p,quality=85)
  out.append({'t':round(t/1.12,3),'src':p,'lab':lab,'f':f})
json.dump(out,open('/home/claude/w/shots.json','w'),ensure_ascii=False,indent=0)
print(len(out),len(set(s[1] for s in S)))
d=[(out[i+1]['t']-out[i]['t']) for i in range(len(out)-1)];print(max(d),min(d))
