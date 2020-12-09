fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('Cannot find the file ',fname)
    quit()

for line in fh :
    line = line.upper()
    line = line.rstrip()
    print(line)
