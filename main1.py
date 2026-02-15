x = int(input())
arr = input().split()

v = {}
for i in arr:
    if i not in v:
        v[i] = 1
    else:
        v[i] += 1
mx = 0
ans = 0
for i in v:
    if v[i] > mx or (v[i] == mx and i < ans):
        mx = v[i]
        ans = i
print(ans)