a = int(input())
b = list(map(int, input().split()))
n = 0
for i in range(a):
    if b[i] > 0:
        n += 1
print(n)
