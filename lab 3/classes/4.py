import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

x1 = int(input("x1: "))
y1 = int(input("y1: "))

x2 = int(input("x2: "))
y2 = int(input("y2: "))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print(f"Distance between points: {p1.dist(p2):.2f}")
