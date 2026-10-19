# 37. Write a Python program to illustrate method resolution order and magic methods.

class A:
    def show(self): print("A")
class B(A):
    def show(self): print("B")
class C(A):
    def show(self): print("C")
class D(B, C):
    pass

D().show()
print("MRO:", [cls.__name__ for cls in D.__mro__])

# Magic methods
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __len__(self):
        return 2

p1, p2 = Point(1, 2), Point(3, 4)
print(p1 + p2)
print("Equal:", p1 == p2)
print("Length:", len(p1))
