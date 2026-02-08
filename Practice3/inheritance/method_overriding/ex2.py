class Shape:
    def area(self):
        print("Area")

class Square(Shape):
    def area(self):
        print("Square area")

Square().area()