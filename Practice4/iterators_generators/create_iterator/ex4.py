class Countdown:
    def __init__(self, n):
        self.i = 0
        self.n = n 
    def __iter__(self):
        return self
    def __next__(self):
        if self.n >= self.i:
            val = self.n
            self.n -= 1
            return val
        raise Countdown
x = int(input())
for i in Countdown(x):
    print(i)