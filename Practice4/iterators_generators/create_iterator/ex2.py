class Counter:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        raise StopIteration
    
for i in Counter(5):
    print(i)