F='file:///home/claude/tools/node_modules/@fontsource'
def ff(fam,path,w,st='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{path.replace('X',s)})}}" for s in ['latin','latin-ext'])
CSS=ff('O','oswald/files/oswald-X-600-normal.woff2',600)+ff('O','oswald/files/oswald-X-500-normal.woff2',500)+ff('S','cormorant-garamond/files/cormorant-garamond-X-500-italic.woff2',500,'italic')+ff('S','cormorant-garamond/files/cormorant-garamond-X-600-normal.woff2',600)+ff('I','inter/files/inter-X-600-normal.woff2',600)+ff('I','inter/files/inter-X-400-normal.woff2',400)+'''
html,body{margin:0;width:1080px;height:1350px;overflow:hidden;background:#0d0d0f;color:#f4f1ea}
.bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15) brightness(.78)}
.tint{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,14,30,.15) 0%,rgba(10,14,30,.05) 35%,rgba(8,10,20,.82) 72%,rgba(8,10,20,.95) 100%)}
.grain{position:absolute;inset:0;opacity:.22;mix-blend-mode:overlay}
.scrap{position:absolute;background:#efe9dc;padding:14px 14px 40px;box-shadow:0 18px 40px rgba(0,0,0,.55)}
.scrap img{display:block;filter:grayscale(1) contrast(1.1)}
.lab{display:inline-block;font-family:I;font-weight:600;font-size:34px;line-height:1.05;padding:6px 14px 8px;letter-spacing:-.01em}
.blue{background:#5b7cff;color:#fff}.yel{background:#f2e35b;color:#2f45c9}
.h{font-family:O;font-weight:600;font-size:104px;line-height:.98;letter-spacing:-.025em;text-transform:none;margin:0}
.h u{text-decoration-thickness:6px;text-underline-offset:12px}
.h em{font-family:S;font-style:italic;font-weight:500;letter-spacing:-.01em;font-size:1.02em}
.sub{font-family:S;font-style:italic;font-size:46px;line-height:1.15;opacity:.92;margin-top:26px}
.brand{position:absolute;left:64px;top:56px;font-family:S;font-weight:600;font-size:36px;letter-spacing:.08em}
.brand i{color:#f2e35b}
.cr{position:absolute;right:28px;bottom:22px;font-family:I;font-weight:400;font-size:17px;opacity:.6}
.foot{position:absolute;left:64px;bottom:58px;font-family:I;font-weight:600;font-size:22px;letter-spacing:.14em;text-transform:uppercase;opacity:.75}
'''
GR='<svg class=grain width=1080 height=1350><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/></filter><rect width=100% height=100% filter=url(#n)/></svg>'
def page(body): return f'<!DOCTYPE html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>'
P='file:///tmp/pod/sc/'
A=page(f'''<div class=bg style="background-image:url({P}banus2.jpg)"></div><div class=tint></div>{GR}
<div class=brand>SOL <i>y</i> SÓL</div>
<div class=scrap style="right:70px;top:170px;transform:rotate(4deg)"><img src="{P}aerial.jpg" style="width:330px;height:230px;object-fit:cover"></div>
<div style="position:absolute;left:64px;top:330px"><span class="lab blue">Zagadki Costa del Sol</span><br><span class="lab yel" style="margin-top:8px">odcinek #1</span></div>
<div style="position:absolute;left:64px;right:64px;bottom:150px">
<h1 class=h>James Bond<br><u>kontra</u> Marbella.</h1>
<div class=sub>5 domów. 72 apartamenty.<br>I śledztwo, które nazwano „Goldfinger”.</div></div>
<div class=foot>Podcast · nowy odcinek w niedzielę 18:00</div><div class=cr>Fot. kallerna, Adam Cli / Wikimedia Commons, CC BY-SA 4.0</div>''')
B=page(f'''<div class=bg style="background-image:url({P}mclub.jpg)"></div><div class=tint></div>{GR}
<div class=brand>SOL <i>y</i> SÓL</div>
<div style="position:absolute;left:64px;right:64px;bottom:150px">
<span class="lab yel">Michelin ocenia też hotele</span>
<h1 class=h style="margin-top:22px">Tylko jeden hotel<br>na wybrzeżu ma<br><em>dwa</em> <u>Klucze</u>.</h1>
<div class=sub>Który? I co to właściwie znaczy.</div></div>
<div class=foot>Luksus · przesuń →</div><div class=cr>Fot. Zarateman / Wikimedia Commons, CC0</div>''')
C=page(f'''<div class=bg style="background-image:url({P}ayto.jpg)"></div><div class=tint></div>{GR}
<div class=brand>SOL <i>y</i> SÓL</div>
<div class=scrap style="left:600px;top:150px;transform:rotate(-5deg)"><img src="{P}crane.jpg" style="width:340px;height:250px;object-fit:cover"></div>
<div style="position:absolute;left:64px;right:64px;bottom:150px">
<span class="lab blue">Wieczór na wybrzeżu · 22.11</span>
<h1 class=h style="margin-top:22px">Tego ratusz<br><em>nie</em> ogłosił<br>na <u>konferencji</u>.</h1>
<div class=sub>Marbella i jeszcze 4 sprawy z wybrzeża.</div></div>
<div class=foot>8:00 · 19:00 · przesuń →</div><div class=cr>Fot. Zarateman, Wikideas1 / Wikimedia Commons, CC0 · zdjęcie ilustracyjne</div>''')
for n,h in [('a',A),('b',B),('c',C)]: open(f'/tmp/nstyle/{n}.html','w').write(h)
