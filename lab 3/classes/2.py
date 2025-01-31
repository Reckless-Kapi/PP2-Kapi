class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area (self):
        return self.length **2
    
square_length = int( input("length: "))
square = Square (square_length)
print("area: ", square.area())