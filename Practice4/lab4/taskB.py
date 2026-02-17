x = int(input())
def k(x):
    for i in range(0, x + 1, 2):
        yield i
print(*k(x), sep=",")