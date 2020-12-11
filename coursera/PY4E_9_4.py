name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = {}
mails = []

for line in handle:
    if not line.startswith("From "): 
        continue
    words = line.split()
    mails.append(words[1])      


for mail in mails:
    sender[mail] = sender.get(mail, 0) +1

bigcount = None
bigword = None
for mail, count in sender.items():
    if bigcount is None or count > bigcount:
        bigword = mail
        bigcount = count
print(bigword, bigcount)
    
