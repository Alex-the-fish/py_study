
i = []
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
        i.append(num)
        smallest = min(i)
        largest = max(i)
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
