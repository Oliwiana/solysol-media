import json,sys
cfg=json.load(open(sys.argv[1]))
s=open('/tmp/kp/tpl.html').read().replace('/*JS*/','const CFG='+json.dumps(cfg,ensure_ascii=False)+';\n'+open('/tmp/kp/engine.js').read())
open('/tmp/kp/pro.html','w').write(s)
