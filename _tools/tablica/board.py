import json,sys,os,html
from PIL import Image, ImageOps, ImageEnhance
B='/tmp/sm/_photos/commons/'
def prep(f,out):
    im=Image.open(B+f+'.jpg').convert('L'); W,H=im.size; r=4/3
    if W/H>r: nw=int(H*r); im=im.crop(((W-nw)//2,0,(W-nw)//2+nw,H))
    else: nh=int(W/r); im=im.crop((0,(H-nh)//2,W,(H-nh)//2+nh))
    im=im.resize((960,720)); im=ImageEnhance.Contrast(im).enhance(1.15); im.save(out,quality=86)
def cred(f):
    d,fn=f.split('/')
    for c in json.load(open(B+d+'/credits.json')):
        if c['file']==fn+'.jpg': return c['author'].split('\n')[0].replace('This Photo was taken by ','').strip()[:30]+' ('+c['license']+')'
def build(spec,outdir,Wd=1080,Hd=1920):
    els=[];strings=[];cams=[];js=[];creds=[]
    y=spec.get('y0',260); side=0; prev=None
    for i,b in enumerate(spec['beats']):
        t=b['t']; k=b['k']; eid=f'e{i}'
        if k=='head':
            els.append(f'<div class=e id={eid}a style="left:70px;top:{y}px;font-family:T;color:#efe6d2;font-size:96px;letter-spacing:.04em"></div><div class=e id={eid}b style="left:74px;top:{y+120}px;font-family:T;color:#F6C343;font-size:60px"></div>')
            js.append(f"typ('{eid}a',{json.dumps(b['a'])},{t},0.6,t);typ('{eid}b',{json.dumps(b['b'])},{b['tb']},0.5,t);")
            cams.append((t,y+300 if Wd<1500 else y+250)); prev=(Wd//2,y+260); y+=300; continue
        if k in('photo','note','dark','list','count'):
            w=b.get('w',(760 if Wd<1500 else 880) if k=='photo' else (860 if Wd<1500 else 1100)); x=((120 if Wd<1500 else 230) if side==0 else Wd-w-(120 if Wd<1500 else 230)) if k=='photo' else (Wd-w)//2
            rot=b.get('rot',(-2.5 if side==0 else 2.5)); side^=1
            if k=='photo':
                fn=f'p{i}.jpg'; prep(b['f'],f'{outdir}/img/{fn}'); creds.append(cred(b['f']))
                h=int(w*0.75)+26+96
                inner=f'<img src="img/{fn}" style="width:100%;display:block"><div class=pc>{html.escape(b["cap"])}</div>'
                pad='26px 26px 96px'
            elif k=='list':
                h=170+len(b['items'])*86
                inner=f'<div style="font-family:I;font-weight:900;font-size:40px;letter-spacing:.08em">{b["title"]}</div>'+''.join(f'<div class=li id={eid}l{j} style="opacity:0">— {html.escape(n)}</div>' for j,(n,_) in enumerate(b['items']))
                for j,(n,tt) in enumerate(b['items']): js.append(f"pop('{eid}l{j}',{tt},t,1.3);")
                pad='44px 50px'
            elif k=='count':
                h=520; n=b['n']
                cells=''.join(f'<div class=u id={eid}u{j}></div>' for j in range(n))
                inner=f'<div style="font-size:40px">{b["title"]}</div><div style="display:flex;flex-wrap:wrap;gap:16px;width:700px;margin:34px auto 0">{cells}</div><div class=cnt><span id={eid}n>0</span> <span style="font-size:44px">{b["unit"]}</span></div>'
                js.append(f"{{let c=0;for(let j=0;j<{n};j++){{const a={t+0.3}+j*0.07;const kk=E(a,0.2,t);const u=document.getElementById('{eid}u'+j);u.style.opacity=kk;u.style.transform='scale('+kk+')';if(t>=a+0.1)c++}}document.getElementById('{eid}n').textContent=c}}")
                pad='40px 50px'
            else:
                h=b.get('h',300)
                lab=f'<div style="font-size:32px;opacity:.75">{html.escape(b.get("lab",""))}</div>' if b.get('lab') else ''
                big=f'<div id={eid}q style="font-size:{b.get("fs",54 if Wd<1500 else 66)}px;line-height:1.2;margin-top:14px;min-height:60px"></div>'
                inner=lab+big
                js.append(f"typ('{eid}q',{json.dumps(b['text'])},{b.get('tt',t+0.3)},{b.get('td',1.6)},t);")
                pad='44px 50px'
            cls='paper dark' if k=='dark' else 'paper'
            els.append(f'<div class="e {cls}" id={eid} style="left:{x}px;top:{y}px;width:{w}px;padding:{pad};box-sizing:border-box;transform:rotate({rot}deg)"><div class=pin></div>{inner}</div>')
            js.append(f"pop('{eid}',{t},t,1.12);")
            pin=(x+w//2,y+6)
            if prev:
                sid=f's{i}'; x1,y1=prev; x2,y2=pin; cx=(x1+x2)/2+(160 if side else -160)
                strings.append(f'<path id={sid} d="M{x1} {y1} C {cx} {y1+120}, {cx} {y2-120}, {x2} {y2}" stroke="#c0281b" stroke-width=4 fill=none />')
                js.append(f"str('{sid}',{t-0.45},0.4,t);")
            cams.append((t-0.45,eid)); prev=pin; last=(x,y,w,h)
            if b.get('sub'):  # secondary small photo
                s=b['sub']; fn=f'q{i}.jpg'; prep(s['f'],f'{outdir}/img/{fn}'); creds.append(cred(s['f']))
                sw=430 if Wd<1500 else 560; sx=(x+w-60 if Wd>1500 else Wd-sw-50) if x<Wd/2-w/2 else (x-sw+60 if Wd>1500 else 50); sy=y+h-260
                els.append(f'<div class="e paper" id={eid}s style="left:{sx}px;top:{sy}px;width:{sw}px;padding:18px 18px 64px;box-sizing:border-box;transform:rotate({-rot*1.6}deg);z-index:3"><div class=pin></div><img src="img/{fn}" style="width:100%;display:block"><div class=pc style="font-size:28px;bottom:16px">{html.escape(s["cap"])}</div></div>')
                js.append(f"pop('{eid}s',{s['t']},t,1.2);"); h=max(h,sy-y+sw*0.75+82)
            y+=h+b.get('gap',150); continue
        if k in('stamp','sticker'):
            x,yy,w,h=last
            if k=='stamp':
                els.append(f'<div class="e stamp" id={eid} style="left:{x+w-b.get("dx",420)}px;top:{yy+b.get("dy",40)}px;color:#c0281b;font-size:{b.get("fs",48)}px;transform:rotate(10deg);z-index:4">{html.escape(b["text"])}</div>')
                js.append(f"pop('{eid}',{t},t,2.2);")
            else:
                els.append(f'<div class="e" id={eid} style="left:{b.get("x",x+w-380)}px;top:{yy+h+b.get("dy",-40)}px;transform:rotate(-4deg);background:#F6C343;color:#171513;font-weight:900;font-size:{b.get("fs",46)}px;padding:12px 26px;box-shadow:6px 12px 24px rgba(0,0,0,.5);z-index:4;max-width:820px">{html.escape(b["text"])}</div>')
                js.append(f"pop('{eid}',{t},t,1.6);")
    BH=y+900
    return els,strings,cams,js,creds,BH
