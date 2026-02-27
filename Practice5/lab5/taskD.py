arr = input()
a = []
for x in arr:
    if x.isdigit():
        a.append(x)
if a:
    for x in a:
        print(x, end=" ")
else:
    print(" ")
