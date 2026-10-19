# UNIT 4 - Q6: Write a program to demonstrate method overriding and polymorphism.
# SCENARIO: A drawing app calls area() on any shape - Circle, Rectangle,
#           Triangle - without caring which one it is. Each shape overrides
#           the parent method with its own formula.

import math

class Shape:
    def area(self):
        return 0
    def info(self):
        return f"{self.__class__.__name__} area = {round(self.area(), 2)}"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2         # overriding

class Rectangle(Shape):
    def __init__(self, l, b): self.l, self.b = l, b
    def area(self): return self.l * self.b

class Triangle(Shape):
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h

for s in (Circle(5), Rectangle(4, 6), Triangle(3, 8)):    # polymorphism
    print(s.info())

# super() with overriding
class Animal:
    def speak(self): return "Some sound"
class Dog(Animal):
    def speak(self): return super().speak() + " -> Woof"
print(Dog().speak())

# built-in polymorphism
print(len("hello"), len([1, 2, 3]), 3 + 4, "a" + "b")
