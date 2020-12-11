name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
times = []
counts = {}
list = []

for line in handle:
    if not line.startswith("From ") : continue
    words = line.split()
    times.append(words[5][0:2])
    times = sorted(times)

for hr in times:
    counts[hr] = counts.get(hr, 0) + 1

for hr,count in counts.items():
    list.append((hr,count))
    print(hr, count)
