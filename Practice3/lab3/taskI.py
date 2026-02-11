class Cyrcle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pi = 3.14159
        return (self.radius ** 2) * pi
    
r = int(input())
p1 = Cyrcle(r)
print(f"{p1.area():.2f}")
