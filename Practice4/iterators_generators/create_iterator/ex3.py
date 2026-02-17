class Even:
    def __init__(self, n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i <= self.n:
            val = self.i
            self.i += 2
            return val
        raise StopIteration
x = int(input())
    
for i in Even(x):
    print(i)
    