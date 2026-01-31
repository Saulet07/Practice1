a = int(input())
b = list(map(int, input().split()))

max = -1000000
indx = 0
for i in range(a):
    if b[i] > max:
        max = b[i]
        indx = i
print(indx + 1)
