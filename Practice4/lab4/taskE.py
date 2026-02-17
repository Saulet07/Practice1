x = int(input())
def k(x):
    while x >= 0:
        yield x
        x -= 1
for i in k(x):
    print(i)