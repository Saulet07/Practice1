a = int(input())
b = list(map(int, input().split()))

ava = set()
for x in b:
    if x in ava:
        print("NO")
    else:
        ava.add(x)
        print("YES")
