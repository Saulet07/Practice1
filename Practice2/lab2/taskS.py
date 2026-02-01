a = int(input())
ava = {}
for i in range(a):
    name, num = input().split()
    k = int(num)
    if name in ava:
        ava[name] += k
    else:
        ava[name] = k
for x in sorted(ava):
    print(x, ava[x])
