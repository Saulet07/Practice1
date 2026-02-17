x = int(input())
def k():
    for i in range(0, x + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for i in k():
    print(i, end=" ")