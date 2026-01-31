a = int(input())
b = list(map(int, input().split()))

for i in range(a):
    x = b[i] * b[i]
    print(x, end=" ")