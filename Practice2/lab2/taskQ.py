a = int(input())
ava = {}
for _ in range(a):
    x = input().strip()
    if len(x) == 14:
        if x in ava:
            ava[x] += 1
        else:
            ava[x] = 1
hh = 0
for x in ava:
    if ava[x] == 3:
        hh += 1
print(hh)
