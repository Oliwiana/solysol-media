const E=(a,b,t)=>{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)};
const $=id=>document.getElementById(id);
const S=CFG.seg; // start times of segments 0..9
const typ=(id,txt,a,dur,t)=>{const n=Math.floor(txt.length*Math.max(0,Math.min(1,(t-a)/dur)));const el=$(id);el.style.opacity=t>=a?1:0;el.textContent=txt.slice(0,n)+(t>=a&&t<a+dur+0.6&&Math.floor(t*3)%2?'_':'')};
function pop(id,a,t,sc0){const el=$(id);const k=E(a,0.35,t);el.style.opacity=k;const base=el.dataset.tr||(el.dataset.tr=el.style.transform||'');el.style.transform=base+' scale('+(sc0+(1-sc0)*k)+')'}
function str(id,a,dur,t){const p=$(id);const L=p.getTotalLength();p.style.strokeDasharray=L;p.style.strokeDashoffset=L*(1-E(a,dur,t))}
const HITS=[]; // impact times (stamps)
const P=[0,-60,-700,-1380,-1560,-2200,-3000,-3850,-4560,-4580];
function cam(t){let y=0;for(let i=1;i<P.length;i++){if(t>=S[i]-0.6){y=P[i-1]+(P[i]-P[i-1])*E(S[i]-0.6,0.7,t)}}
 let sh=0;for(const h of HITS){const d=t-h;if(d>=0&&d<0.3)sh+=(1-d/0.3)*14*Math.sin(d*90)}
 const z=1.03+0.03*Math.sin(t*0.22), r=0.4*Math.sin(t*0.17);
 $('board').style.transform='translate('+(sh*0.6)+'px,'+(y+sh)+'px) scale('+z+') rotate('+r+'deg)';
 let f=0;for(const h of HITS){const d=t-h;if(d>=0&&d<0.25)f=Math.max(f,0.35*(1-d/0.25))}$('flash').style.opacity=f;}
function caps(t){const c=$('cap');let p=null;for(const q of CFG.caps){if(t>=q[0]&&t<=q[1]+0.15)p=q}
 if(!p||t<S[1]-0.1||t>=S[9]){c.style.opacity=0;return}
 const words=p[2].split(' ');const span=Math.max(0.4,(p[1]-p[0]));let tot=words.reduce((a,w)=>a+w.replace(/<\/?y>/g,'').length+2,0),acc=0;
 let html='';let yl=false;
 for(const w of words){let ww=w;if(ww.includes('<y>'))yl=true;const clean=ww.replace(/<\/?y>/g,'');
  const ta=p[0]+span*0.92*acc/tot;acc+=clean.length+2;const k=E(ta,0.12,t);
  const active=t>=ta&&t<p[0]+span*0.92*acc/tot+0.05;
  html+='<span class=w style="opacity:'+k+';transform:translateY('+(12*(1-k))+'px) scale('+(active?1.08:1)+');color:'+(yl?'#F6C343':(active?'#fff':'#e9e2cf'))+'">'+clean+'</span>';
  if(ww.includes('</y>'))yl=false;}
 c.innerHTML=html;c.style.opacity=E(p[0],0.15,t);}
const YRS=[[1,1991],[2,2002],[3,2003],[4,2003],[5,2006],[6,2013],[7,2013],[8,2024]];
function year(t){let y=1991;for(const[i,v] of YRS)if(t>=S[i])y=v;let prev=1991;for(const[i,v] of YRS)if(t>=S[i]-0.0){}
 $('year').textContent=y;$('year').style.opacity=t<S[1]?0:1;$('yearl').style.opacity=t<S[1]?0:.7;
 const fr=(y-1991)/(2024-1991);const el=$('tlf');const cur=parseFloat(el.dataset.v||0);const nv=cur+(fr-cur)*0.12;el.dataset.v=nv;el.style.width=(nv*100)+'%';$('tld').style.left=(nv*100)+'%';
 const vis=t>=S[1]&&t<S[9]-0.3?1:0;$('tl').style.opacity=vis;}
let seed=1;function grain(t){const cv=$('grain'),x=cv.getContext('2d');const im=x.createImageData(540,960);seed=Math.floor(t*30)*9301+49297;let r=seed;
 for(let i=0;i<im.data.length;i+=4){r=(r*1103515245+12345)&0x7fffffff;const v=r>>23&255;im.data[i]=im.data[i+1]=im.data[i+2]=v;im.data[i+3]=255}x.putImageData(im,0,0);
 $('light').style.opacity=0.85+0.15*Math.sin(t*7.3)*Math.sin(t*3.1);}
function intro(t){const a=CFG.intro;const ov=$('intro');
 ['i1','i2','i3'].forEach((id,n)=>{const el=$(id);const k=E(a[n],0.18,t);el.style.opacity=k;el.style.transform='scale('+(1.6-0.6*k)+')';});
 $('isub').style.opacity=E(a[2]+0.6,0.4,t);
 const out=E(S[1]-0.5,0.5,t);ov.style.opacity=1-out;ov.style.transform='scale('+(1+0.15*out)+')';ov.style.display=out>=1?'none':'flex';}
window.setT=function(t){
 HITS.length=0;HITS.push(...CFG.intro,CFG.c.stb,CFG.c.sto,CFG.c.stz,CFG.c.sts);
 cam(t);caps(t);year(t);grain(t);intro(t);
 const s1=S[1];typ('t1','MARBELLA',s1+0.1,0.7,t);typ('t2','1991',s1+0.9,0.5,t);
 pop('pa',s1+1.6,t,1.15);pop('ca',CFG.c.ca,t,1.1);
 str('s1',S[2]-0.6,0.5,t);pop('cb',S[2],t,1.1);pop('stb',CFG.c.stb,t,2.2);
 str('s2',S[3]-0.6,0.5,t);pop('cc',S[3],t,1.1);pop('cd',CFG.c.cd,t,1.5);pop('nw',CFG.c.nw,t,1.3);
 pop('sto',CFG.c.sto,t,2.4);
 str('s3',S[5]-0.6,0.5,t);pop('fold',S[5],t,1.1);
 ['r1','r2','r3'].forEach((id,n)=>{$(id).style.width=(1-E(CFG.c.red+n*0.25,0.35,t))*600+'px';});
 pop('stz',CFG.c.stz,t,2.4);pop('dz',CFG.c.dz,t,1.6);
 str('s4',S[6]-0.6,0.5,t);pop('pc',S[6],t,1.15);pop('cw',S[6]+0.5,t,1.15);pop('pt',CFG.c.pt,t,1.6);
 str('s5',S[7]-0.6,0.5,t);pop('cl',S[7],t,1.1);pop('pe',S[7]+0.8,t,1.15);pop('sts',CFG.c.sts,t,2.4);
 str('s6',S[8]-0.6,0.5,t);pop('fin',S[8],t,1.1);
 const en=$('end');en.style.opacity=E(S[9],0.4,t);en.style.transform='translateY('+(80*(1-E(S[9],0.4,t)))+'px)';}
