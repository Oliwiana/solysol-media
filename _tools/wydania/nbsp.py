import re,sys,glob
for f in sorted(glob.glob(sys.argv[1]+'/[0-9][0-9].html')):
    s=open(f).read()
    def fix(m):
        t=m.group(1)
        t=re.sub(r'(?<![\w&;])([aiouwzAIOUWZ]) (?=\S)',r'\1&nbsp;',t)
        return '>'+t+'<'
    body=re.sub(r'>([^<>]*)<',fix,s.split('</style>',1)[1]) if '</style>' in s else s
    s=s.split('</style>',1)[0]+'</style>'+body if '</style>' in s else body
    open(f,'w').write(s)
