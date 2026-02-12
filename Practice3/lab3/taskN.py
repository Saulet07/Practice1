n = int(input())
arr = list(map(int, input().split()))
x = int(input())

for i in range(x):
    p = input().split()
    if p[0] == "abs":
        arr = list(map(lambda q: abs(q), arr))
    elif p[0] == "add":
        v = int(p[1])
        arr = list(map(lambda q: q + v, arr))
    elif p[0] == "multiply":
        v = int(p[1])
        arr = list(map(lambda q: q * v, arr))
    else:
        v = int(p[1])
        arr = list(map(lambda q: q ** v, arr))
for i in arr:
    print(i, end=" ")