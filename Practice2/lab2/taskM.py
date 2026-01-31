a = int(input())
prime = True
if a <= 1:
    print("NO")
for i in range(2, a):
    if a % i == 0:
        prime = False
        break
if prime:
    print("YES")
else:
    print("NO")


