a, b = map(int, input().split())
def k():
    for i in range(a, b + 1):
        yield i * i
for i in k():
    print(i)