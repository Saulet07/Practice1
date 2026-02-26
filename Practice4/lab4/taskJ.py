arr = input().split()
times = int(input())
def k():
    i = 0
    while i < times:
        yield from arr
        i += 1
for i in k():
    print(i, end=" ")
