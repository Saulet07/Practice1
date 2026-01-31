a = int(input())
b = list(map(int, input().split()))
c = b[0]
count = 0
for i in range(a):
    if b[i] == c:
        count += 1
        
