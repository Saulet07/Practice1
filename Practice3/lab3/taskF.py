class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
a, b = map(int, input().split())
p1 = Rectangle(a , b)
print(p1.area())