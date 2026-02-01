a = int(input())
b = list(map(int, input().split()))

ls = {}
for x in b:
    if x in ls:
        ls[x] = ls[x] + 1
    else:
        ls[x] = 1
answer = 0
maxx = 0

for x in ls:
    if ls[x] > maxx or (maxx == ls[x] and x < answer):
        maxx = ls[x]
        answer = x
print(answer)