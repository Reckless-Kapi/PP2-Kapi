class Shape:
    def area(self):
        return 0 
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rectangle_length = float(input("length: "))
rectangle_width = float(input("width: "))
rectangle = Rectangle(rectangle_length, rectangle_width)
print("area: ", rectangle.area())