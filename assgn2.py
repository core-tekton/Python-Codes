fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    l = line.split()
    for a in l:
        if a not in lst:
            lst.append(a)
lst.sort()
print(lst)



