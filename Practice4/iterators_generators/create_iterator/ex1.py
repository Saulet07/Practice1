class SimpleCounter:
    def __init__(self):
        self.i = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <= 3:
            x = self.i
            self.i += 1
            return x
        raise StopIteration
for i in SimpleCounter():
    print(i)
        
    