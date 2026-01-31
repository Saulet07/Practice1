x, y, z = map(int, input().split())
b = list(map(int, input().split()))

for i in range((z - y + 1)//2):
    b[y + i - 1] = b[y - i - 1]
for i in b:
    print(i, end=" ")