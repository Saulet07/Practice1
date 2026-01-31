a = int(input())
b = list(map(int, input().split()))
maxx = -100000
indx = 0
for i in range(a):
    if b[i] > maxx:
        maxx = b[i]
minn = 1000000
for i in range(a):
    if b[i] < minn:
        minn = b[i]
for i in range(a):
    if b[i] == maxx:
        indx = i
        b[indx] = minn
for i in range(a):
    print(b[i], end=" ")