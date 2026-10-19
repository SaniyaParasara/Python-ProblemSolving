# 36. Write a Python program to demonstrate method overriding and polymorphism.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l, self.b = l, b
    def area(self):                             # Overriding
        return self.l * self.b

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):                             # Overriding
        return 3.14 * self.r ** 2

# Polymorphism: same method name, different behaviour
for shape in [Rectangle(4, 5), Circle(3), Shape()]:
    print(type(shape).__name__, "area =", shape.area())
