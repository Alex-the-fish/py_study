fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.strip()
    if line.startswith("From "):
        line = line.split()
    	print(line[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
