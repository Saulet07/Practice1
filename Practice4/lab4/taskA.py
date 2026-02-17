x = int(input())
def square():
    for i in range(1, x + 1):
        yield i*i
    
for i in square():
    print(i)