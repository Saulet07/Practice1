import math
class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def show1(self):
        print(f"({self.x1}, {self.y1})")
    def move(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
    def show2(self):
        print(f"({self.x2}, {self.y2})")
    def res(self, x3, y3):
        self.x3 = x3
        self.y3 = y3
    def resshow(self):
        k = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        print(f"{k:.2f}")

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

p1 = Point(x1, y1)
p1.show1()
p1.move(x2, y2)
p1.show2()
p1.res(x3, y3)
p1.resshow()
