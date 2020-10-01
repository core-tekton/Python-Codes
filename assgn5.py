name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
li = []
dic = {}
for line in handle:
    if line.startswith('From '):
        line = line.split()
        print(line)
        l = line[5]
        dic[l[:2]] = dic.get(l[:2], 0) + 1
        #dic[l] = dic.get(l, 0) + 1
        print(l)
        #li.append(l[:2])
        #print(li)
#for i in li:
 #   dic[i] = dic.get(i, 0)+1
for key, value in sorted(dic.items()):
    print(key, value)