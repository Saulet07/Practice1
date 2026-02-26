class Reverse:
    def __init__(self, n):
        self.i = n
        self.n = len(n) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < 0:
            raise StopIteration
        ch = self.i[self.n]
        self.n -= 1
        return ch
    

n = input()
for i in Reverse(n):
    print(i, end="")