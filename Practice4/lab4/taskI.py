x = int(input())
def k(x):
    yield 1
    for i in range(1, x + 1):
        yield 2 ** i
for i in k(x):
    print(i, end=" ")