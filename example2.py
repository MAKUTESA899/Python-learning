import math


class Shape:
    def area(self):
        raise NotImplementedError("subclasses should impliment this method")
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height=height

    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius
    def area(self):
        return math.pi * (self.radius **2)

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5 * self.base * self.height
def print_area(shape):
    for shape in shapes:
        print(f"the are of the shape is {shape.area()}")
shapes=[Rectangle(10,20),Circle(5),Triangle(10,5)]

print_area(shapes)