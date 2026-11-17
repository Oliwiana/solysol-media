# usage: python3 _tools/mkstory.py <id>  -> <id>/story.jpg (1080x1920) from <id>/ig-1.jpg (or okladka.jpg)
import sys,os
from PIL import Image,ImageDraw,ImageFont
d=sys.argv[1]; src=next(p for p in [f'{d}/ig-1.jpg',f'{d}/okladka.jpg'] if os.path.exists(p))
bg=Image.new('RGB',(1080,1920),(23,21,19)); im=Image.open(src).convert('RGB')
w=1000; h=int(im.height*w/im.width)
if h>1560: h=1560; w=int(im.width*h/im.height)
im=im.resize((w,h),Image.LANCZOS); y=(1920-h)//2-20; bg.paste(im,((1080-w)//2,y))
dr=ImageDraw.Draw(bg)
def font(sz):
  for f in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
    if os.path.exists(f): return ImageFont.truetype(f,sz)
  return ImageFont.load_default()
t='NOWY POST NA PROFILU  →  SOLYSOL.PL'; f=font(30)
tw=dr.textlength(t,font=f); dr.text(((1080-tw)/2,y+h+40),t,fill=(224,135,79),font=f)
bg.save(f'{d}/story.jpg',quality=90); print(f'{d}/story.jpg')
