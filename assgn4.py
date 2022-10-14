name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d={}
li=[]
for line in handle:
    if line.startswith('From '):
        sp = line.split()
        d[sp[1]] = d.get(sp[1], 0) + 1


maxkey = None
maxvalue = None
for k,v in d.items():
    if maxkey is None or v>maxvalue:
        maxkey = k
        maxvalue = v

print(maxkey,maxvalue)
//Mateus
