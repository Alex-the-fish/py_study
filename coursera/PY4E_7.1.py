# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    line = line.rstrip()
    num = float(line[pos+1:])+ num
    count+=1
    a = num/count
print("Average spam confidence:", a)
