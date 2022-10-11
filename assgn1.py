# Use the file name mbox-short.txt as the file name
count=0
value=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count+=1
    line=line.rstrip()
    value = float(value) + float(line[19:])
    print("value:",value)
avg = value/count
print("Average spam confidence:",avg)
