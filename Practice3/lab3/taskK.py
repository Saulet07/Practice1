class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y
                


a1, b1, a2, b2 = map(int, input().split())

p1 = Pair(a1, a2)
p2 = Pair(b1, b2)
print("Result:", p1.sum() , p2.sum())