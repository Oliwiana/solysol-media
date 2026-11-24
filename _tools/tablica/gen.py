import json,sys,re,os,html
sys.path.insert(0,'/tmp/kb'); import board,page
SP=1.15
def load(n):
    sys.path.insert(0,f'/tmp/sm/_reels/gwiazdy-0{n}-reel')
    import importlib; import data; importlib.reload(data); D=data.D; sys.path.pop(0)
    lines=[l['text'].replace('*','') for l in D['lines']]
    W=[w for w in json.load(open(f'/tmp/g/tr{n}.json'))['words'] if w['type']=='word']
    disp=' '.join(lines).split(); assert len(disp)==len(W)
    LS=[];i=0;IDX=[]
    for l in lines: LS.append(round(W[i]['start']/SP,2)); IDX.append(i); i+=len(l.split())
    T=[(d,round(w['start']/SP,3),round(w['end']/SP,3)) for d,w in zip(disp,W)]
    return D,lines,LS,IDX,T

def wt(T,word,after=0.0,end=False):
    nz=lambda x: re.sub(r'[^\wąćęłńóśźżÁáÓóÍíÑñ]','',x.lower())
    k=nz(word)
    for d,a,b in T:
        if a>=after-0.01 and nz(d).startswith(k): return b if end else a
    raise Exception('no word '+word)

def caps(T):
    out=[];cur=[]
    for d,a,b in T:
        cur.append([d,a,b])
        if len(' '.join(c[0] for c in cur))>22 or re.search(r'[.?!:]$',d): out.append(cur);cur=[]
    if cur: out.append(cur)
    return out

def auto(D,lines,LS,T,ov,head):
    beats=[]; n=len(lines)
    for i,l in enumerate(lines):
        if i==0: continue
        t=LS[i]; te=LS[i+1] if i+1<n else t+3
        if i in ov:
            r=ov[i]
            if r: beats+= r
            continue
        meta=D['lines'][i]; shots=[s for s in meta['shots']]
        if i==1:
            beats.append(dict(k='head',t=t,a=head,b=meta.get('tag',''),tb=t+0.9))
            if shots and not shots[0][0].startswith('PH:'):
                beats.append(dict(k='photo',t=round(t+1.4,2),f=shots[0][0][:-4],cap=shots[0][1]))
            continue
        if l.startswith('I tu robi się'):
            beats.append(dict(k='note',t=t,text=l,tt=t+0.1,td=1.0,h=200,fs=58)); continue
        if l.startswith('Zdaniem redakcji'):
            beats.append(dict(k='dark',t=t,lab='Zdaniem redakcji:',text=l.split('–',1)[1].strip(),tt=t+0.5,td=1.6,h=320)); continue
        if 'Napisz w komentarzu' in l:
            beats.append(dict(k='sticker',t=t,text=(l.replace(' Napisz w komentarzu.','')+' NAPISZ W KOMENTARZU').upper(),dy=-20,x=110,fs=40)); continue
        if l.startswith('Obserwuj'):
            continue
        ph=[s for s in shots if s[0].startswith('PH:')]; real=[s for s in shots if not s[0].startswith('PH:')]
        if ph:
            beats.append(dict(k='note',t=t,lab=ph[0][1]+':',text=ph[0][0][3:],tt=t+0.25,td=0.9,h=280))
            if real: beats.append(dict(k='photo',t=round((t+te)/2,2),f=real[0][0][:-4],cap=real[0][1]))
            continue
        if not real: continue
        b=dict(k='photo',t=t,f=real[0][0][:-4],cap=real[0][1])
        if len(real)>1 and te-t>1.6: b['sub']=dict(f=real[1][0][:-4],cap=real[1][1],t=round(t+(te-t)*0.5,2))
        beats.append(b)
        if meta.get('tag'): beats.append(dict(k='stamp',t=round(t+0.6,2),text=meta['tag'],dx=480,dy=30))
    return beats

def render(n,ov_fn,head,top='GWIAZDY NA COSTA DEL SOL',endtxt='Obserwuj @solysol.pl',endsub=None):
    D,lines,LS,IDX,T=load(n)
    ov=ov_fn(lines,LS,T,D) if ov_fn else {}
    beats=auto(D,lines,LS,T,ov,head)
    out=f'/tmp/g/r{n}'; os.makedirs(out+'/img',exist_ok=True)
    obs=[i for i,l in enumerate(lines) if l.startswith('Obserwuj')][0]
    END=LS[obs]
    els,strings,cams,js,creds,BH=board.build(dict(beats=beats),out)
    hp=page.page(els,strings,cams,js,creds,BH,caps(T),'hook.jpg',endtxt,top,endT=END,hook_end=LS[1]-0.2,yt=False)
    hp=hp.replace('if(!p||t>','if(!p||t<%s||t>'%(LS[1]-0.3))
    if endsub: hp=hp.replace('Nowy odcinek w każdą niedzielę o 18:00 · solysol.pl',endsub)
    open(out+'/index.html','w').write(hp)
    json.dump(dict(creds=creds,dur=round(T[-1][2]+1.6,2),LS=LS),open(out+'/meta.json','w'),ensure_ascii=False)
    print(n,'beats',len(beats),'BH',BH,'dur',round(T[-1][2]+1.6,2))
