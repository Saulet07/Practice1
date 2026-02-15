e=[12, 32, 31, 24, 13]
mx = 0
for i in e:
    if i > mx:
        mx = i
e.sort(reverse = True)
print(e[1])