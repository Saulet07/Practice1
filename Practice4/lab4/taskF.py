x = int(input())
def k(x):
    for i in range(x):
        yield (i - 1) + (i - 2)
for i in k(x):
    print(i)