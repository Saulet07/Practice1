a = int(input())

ava = {}
for i in range(a):
    x = input().strip()
    if x not in ava:
        ava[x] = i + 1
for x in sorted(ava):
    print(x, ava[x])


