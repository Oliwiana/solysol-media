const E=(a,b,t)=>{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)};
const $=id=>document.getElementById(id);const S=CFG.seg,C=CFG.c;const NS='http://www.w3.org/2000/svg';
function rnd(i){let x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x)}
function mk(par,tag,at){const e=document.createElementNS(NS,tag);for(const k in at)e.setAttribute(k,at[k]);$(par).appendChild(e);return e}

const cp0=[];for(let i=0;i<=40;i++){const u=i/40;const x=1000-1000*u;const y=170+560*u+28*Math.sin(u*9)+18*Math.sin(u*23);cp0.push([x,y])}
function off(d,u0,u1){const pts=[];for(let i=0;i<cp0.length;i++){const u=i/40;if(u<u0-1e-6||u>u1+1e-6)continue;const a=cp0[Math.max(0,i-1)],b=cp0[Math.min(40,i+1)];let dx=b[0]-a[0],dy=b[1]-a[1];const L=Math.hypot(dx,dy);const nx=dy/L,ny=-dx/L;pts.push([cp0[i][0]+nx*d,cp0[i][1]+ny*d])}
 let p='M'+pts[0][0].toFixed(1)+' '+pts[0][1].toFixed(1);for(let i=1;i<pts.length;i++)p+=' L'+pts[i][0].toFixed(1)+' '+pts[i][1].toFixed(1);return p}
document.getElementById('coast').setAttribute('d',off(0,0,1));
document.getElementById('seaP').setAttribute('d',off(0,0,1)+' L0 820 L1000 820 Z');
document.getElementById('a7').setAttribute('d',off(-45,0.03,0.97));
document.getElementById('ap7').setAttribute('d',off(-190,0.06,0.97));
document.getElementById('tr').setAttribute('d',off(-18,0.36,0.97));
function cpt(u,d){const i=Math.round(u*40);const a=cp0[Math.max(0,i-1)],b=cp0[Math.min(40,i+1)];let dx=b[0]-a[0],dy=b[1]-a[1];const L=Math.hypot(dx,dy);return [cp0[i][0]+dy/L*d,cp0[i][1]-dx/L*d]}
[['MÁLAGA',0.03,-20,-150,-28],['FUENGIROLA',0.35,-20,30,-90],['MARBELLA',0.95,-20,0,40]].forEach(([n,u,d,ox,oy])=>{const [x,y]=cpt(u,d);const g=document.getElementById('cities');
 const c=document.createElementNS('http://www.w3.org/2000/svg','circle');c.setAttribute('cx',x);c.setAttribute('cy',y);c.setAttribute('r',11);c.setAttribute('fill','#F4EFE7');c.setAttribute('stroke','#161412');c.setAttribute('stroke-width',4);g.appendChild(c);
 const tx=document.createElementNS('http://www.w3.org/2000/svg','text');tx.setAttribute('x',Math.min(820,Math.max(10,x+ox)));tx.setAttribute('y',y+oy);tx.setAttribute('class','city');tx.textContent=n;g.appendChild(tx)});
{const [x,y]=cpt(0.6,-45);document.getElementById('lab7').setAttribute('transform','translate('+(x-170-30)+','+(y+20-600)+')');}
{const [x,y]=cpt(0.45,-190);document.getElementById('labp').setAttribute('transform','translate('+(x-230-120)+','+(y-80-340)+')');}
{const [x,y]=cpt(0.75,-18);document.getElementById('labt').setAttribute('transform','translate('+(x-200)+','+(y+40-690)+')');}
const c7=[],cp=[],bl=[],gf=[];
for(let i=0;i<34;i++)c7.push(mk('cars7','circle',{r:7,fill:'#fff',filter:'url(#gl)'}));
for(let i=0;i<8;i++)cp.push(mk('carsp','circle',{r:7,fill:'#fff',filter:'url(#gl)'}));
const A7=$('a7'),AP=$('ap7'),CO=$('coast'),LA=A7.getTotalLength(),LP=AP.getTotalLength(),LC=CO.getTotalLength();
for(let i=0;i<30;i++){const u=0.08+0.84*rnd(i);const p=A7.getPointAtLength(LA*u),q=CO.getPointAtLength(LC*u);const k=0.25+0.5*rnd(i+50);
 const x=p.x+(q.x-p.x)*k,y=p.y+(q.y-p.y)*k;const s=10+10*rnd(i+9);bl.push([mk('blds','rect',{x:x-s/2,y:y-s,width:s,height:s,fill:'#E9884B',stroke:'#161412','stroke-width':2,opacity:0}),0.05*i])}
for(let i=0;i<18;i++){const u=0.08+0.84*rnd(i+200);const p=A7.getPointAtLength(LA*u),q=AP.getPointAtLength(LP*u);const k=0.25+0.5*rnd(i+300);
 const x=p.x+(q.x-p.x)*k,y=p.y+(q.y-p.y)*k;const g=mk('golf','g',{opacity:0});
 const ln=document.createElementNS(NS,'line');ln.setAttribute('x1',x);ln.setAttribute('y1',y);ln.setAttribute('x2',x);ln.setAttribute('y2',y-30);ln.setAttribute('stroke','#fff');ln.setAttribute('stroke-width',3);g.appendChild(ln);
 const pl=document.createElementNS(NS,'path');pl.setAttribute('d',`M${x} ${y-30} L${x+20} ${y-23} L${x} ${y-16}Z`);pl.setAttribute('fill','#7ED957');g.appendChild(pl);
 const el=document.createElementNS(NS,'ellipse');el.setAttribute('cx',x);el.setAttribute('cy',y);el.setAttribute('rx',14);el.setAttribute('ry',5);el.setAttribute('fill','#3f8f3a');g.insertBefore(el,ln);gf.push([g,0.08*i])}
const fmt=n=>Math.round(n).toLocaleString('pl-PL').replace(/ /g,' ');
function count(id,a,v,t,suf){const k=E(a,1.3,t);$(id).textContent=fmt(v*k)+(suf||'')}
function scene(i,t){const el=$('s'+i);const a=S[i],b=i<9?S[i+1]:CFG.endc;const out=E(b-0.35,0.35,t);el.style.opacity=t>=a-0.05?1-out:0;el.style.transform='translateY('+(-50*out)+'px)';
 let n=0;for(const ch of el.children){if(ch.classList.contains('st')||ch.classList.contains('stamp')||ch.classList.contains('tape'))continue;const d=a+0.07*n;const k=E(d,0.45,t);ch.style.opacity=k;ch.style.transform='translateY('+(46*(1-k))+'px)';ch.style.clipPath='inset(0 0 '+(100*(1-k))+'% 0)';n++}}
function popEl(el,a,t,sc0,rot){const k=E(a,0.3,t);el.style.opacity=k;el.style.transform='rotate('+rot+'deg) scale('+(sc0+(1-sc0)*k)+')'}
let HITS=[];
function caps(t){const c=$('cap');let p=null;for(const q of CFG.caps){if(t>=q[0]&&t<=q[1]+0.15)p=q}
 if(!p||t<S[1]-0.1||t>=S[8]){c.style.opacity=0;return}
 const words=p[2].split(' ');const span=Math.max(0.4,p[1]-p[0]);let tot=words.reduce((a,w)=>a+w.replace(/<\/?y>/g,'').length+2,0),acc=0;let html='',yl=false;
 for(const w of words){if(w.includes('<y>'))yl=true;const cl=w.replace(/<\/?y>/g,'');const ta=p[0]+span*0.92*acc/tot;acc+=cl.length+2;const k=E(ta,0.12,t);const act=t>=ta&&t<p[0]+span*0.92*acc/tot+0.05;
  html+='<span class=w style="opacity:'+k+';transform:translateY('+(12*(1-k))+'px) scale(1);color:'+(act?'#E9884B':(yl?'#F2D36B':'#F4EFE7'))+'">'+cl+'</span>';if(w.includes('</y>'))yl=false}
 c.innerHTML=html;c.style.opacity=E(p[0],0.15,t)}
function grain(t){const cv=$('grain'),x=cv.getContext('2d');const im=x.createImageData(540,960);let r=Math.floor(t*30)*9301+49297;for(let i=0;i<im.data.length;i+=4){r=(r*1103515245+12345)&0x7fffffff;const v=r>>23&255;im.data[i]=im.data[i+1]=im.data[i+2]=v;im.data[i+3]=255}x.putImageData(im,0,0)}
window.setT=function(t){
 HITS=[...CFG.intro,C.st3,C.st6,C.b71,C.b72];let sh=0;for(const h of HITS){const d=t-h;if(d>=0&&d<0.3)sh+=(1-d/0.3)*10*Math.sin(d*90)}
 $('bg').style.transform='scale('+(1.05+0.15*t/S[10])+') translate('+(-20*t/S[10])+'px,'+(sh)+'px)';
 // intro
 ['i1','i2','i3'].forEach((id,n)=>{const el=$(id);const k=E(CFG.intro[n],0.18,t);el.style.opacity=k;el.style.transform='scale('+(1.4-0.4*k)+')'});
 const io=E(S[1]-0.4,0.4,t);$('intro').style.opacity=1-io;$('intro').style.display=io>=1?'none':'flex';
 // wipe at S1 and S8
 let wy=1920;for(const w of [S[8]-0.45]){const d=t-w;if(d>=0&&d<0.9){wy=d<0.45?1920*(1-E(w,0.45,t)):-1920*E(w+0.45,0.45,t)}}$('wipe').style.top=wy+'px';
 for(let i=1;i<=9;i++)scene(i,t);
 // map
 const mv=E(S[2]-0.3,0.5,t)*(1-E(S[7]-0.4,0.4,t));$('mapg').setAttribute('opacity',mv);$('map').style.transform='translate('+sh+'px,0)';
 $('lab7').setAttribute('opacity',E(S[2]+0.3,0.3,t));$('labp').setAttribute('opacity',E(S[3],0.3,t));
 $('a7').setAttribute('stroke-width',t>=S[2]&&t<S[3]?16:12);$('ap7').setAttribute('stroke-width',t>=S[3]&&t<S[4]?16:12);
 c7.forEach((c,i)=>{const u=((i/c7.length)+t*0.012)%1;const p=A7.getPointAtLength(LA*(1-u));c.setAttribute('cx',p.x);c.setAttribute('cy',p.y);c.setAttribute('fill',i%3?'#fff':'#ff4a3a');c.setAttribute('opacity',E(S[2]+0.2+0.02*i,0.2,t))});
 cp.forEach((c,i)=>{const u=((i/cp.length)+t*0.06)%1;const p=AP.getPointAtLength(LP*(1-u));c.setAttribute('cx',p.x);c.setAttribute('cy',p.y);c.setAttribute('opacity',E(S[3]+0.2+0.05*i,0.2,t))});
 bl.forEach(([r,d])=>{r.setAttribute('opacity',E(S[4]+0.3+d,0.2,t))});
 const tr=$('tr');const TL=tr.getTotalLength();tr.setAttribute('opacity',E(S[5],0.2,t));tr.style.strokeDashoffset=0;tr.setAttribute('stroke-dasharray','18 14');tr.style.clipPath='inset(0 0 0 '+(100*(1-E(S[5]+0.2,1.0,t)))+'%)';
 $('labt').setAttribute('opacity',E(S[5]+0.9,0.3,t));
 gf.forEach(([g,d])=>{g.setAttribute('opacity',E(S[6]+0.3+d,0.2,t))});
 // counters & stamps
 count('n2',S[2]+0.2,120000,t);count('n3',S[3]+0.2,40682,t);count('n4',S[4]+0.2,11233,t);
 popEl($('st3'),C.st3,t,2.2,-8);popEl($('tp4'),C.tp4,t,1.4,-4);
 ['l51','l52','l53'].forEach((id,n)=>{const k=E(C['l5'+(n+1)],0.3,t);$(id).style.opacity=k;$(id).style.transform='translateX('+(-40*(1-k))+'px)'});
 popEl($('st6'),C.st6,t,2.4,-8);popEl($('b71'),C.b71,t,2,-8);popEl($('b72'),C.b72,t,2,6);
 caps(t);grain(t);
 const CH=['','KOREK','A-7','AP-7','OSIEDLA','POCIĄG','GOLF','KONCESJE','OPINIA','DLA KUPUJĄCYCH'];let ci=0;for(let i=1;i<=9;i++)if(t>=S[i])ci=i;
 const cv=ci>=1&&t<CFG.endc;$('chap').style.opacity=cv?1:0;$('chapn').textContent=String(ci).padStart(2,'0')+' / 09';$('chapt').textContent=CH[ci];$('chapl').style.width=(60*E(S[ci]||0,0.5,t))+'px';
 $('maptag').style.opacity=E(S[2],0.4,t)*(1-E(S[7]-0.4,0.4,t));
 const bbl=E(S[8]-0.4,0.6,t);$('bg').style.filter='blur('+(8*bbl)+'px) brightness('+(1-0.3*bbl)+')';
 const ec=E(CFG.endc,0.5,t);$('endc').style.opacity=ec;$('endl').style.width=(420*E(CFG.endc+0.3,0.6,t))+'px';
 for(const id of ['top','foot','credit','cap'])if(ec>0)$(id).style.opacity=Math.min(parseFloat($(id).style.opacity||1),1-ec);
$('bar').style.width=(100*Math.min(1,t/S[10]))+'%';
 $('credit').style.opacity=t>=S[1]&&t<S[2]||t>=S[9]?1:0;}
