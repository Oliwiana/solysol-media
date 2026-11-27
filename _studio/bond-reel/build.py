import json,sys
cfg=json.load(open(sys.argv[1]))
s=open('/tmp/bm/tpl.html').read().replace('/*JS*/','const CFG='+json.dumps(cfg,ensure_ascii=False)+';\n'+open('/tmp/bm/engine.js').read())
open('/tmp/bm/pro.html','w').write(s)
