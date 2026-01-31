a = int(input())
p = 1
print(1, end=" ")
for i in range(a):
    p *= 2
    if p <= a:
        print(p, end=" ")