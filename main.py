b = list(map(int, input().split()))
mn = 0
for x in b:
    if x < mn and x >= 0:
        mn = x
    else:
        print(-1)
print(mn)