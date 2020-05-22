'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.width * self.length
        print(area)

    def perimeter(self):
        perimeter = (2 * self.width) + (2 * self.length)
        print(perimeter)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        print(area)

    def circumference(self):
        circumference = 2 * (math.pi * self.radius)
        print(circumference)


rec = Rectangle(2, 3)
rec.area()
rec.perimeter()

cir = Circle(5)
cir.area()
cir.circumference()
