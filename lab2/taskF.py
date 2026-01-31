a = int(input())
b = list(map(int, input().split()))

max = -1000000
for i in range(a):
    if b[i] > max:
        max = b[i]
print(max)