# UNIT 4 - Q7: Write a program to illustrate method resolution order (MRO)
#               and magic methods.
# SCENARIO: In a university app a TeachingAssistant is both a Student and a
#           Staff member; MRO decides which parent method runs. Magic methods
#           let Money objects work with + and print().

class A:
    def show(self): print("A")
class B(A):
    def show(self): print("B")
class C(A):
    def show(self): print("C")
class D(B, C):
    pass

D().show()
print("MRO via __mro__ :", [c.__name__ for c in D.__mro__])
print("MRO via mro()   :", D.mro())

class Money:
    def __init__(self, amt): self.amt = amt
    def __str__(self):        return f"Rs.{self.amt}"
    def __repr__(self):       return f"Money({self.amt})"
    def __add__(self, o):     return Money(self.amt + o.amt)
    def __eq__(self, o):      return self.amt == o.amt
    def __lt__(self, o):      return self.amt < o.amt
    def __len__(self):        return self.amt
    def __call__(self, x):    return self.amt * x

m1, m2 = Money(100), Money(250)
print(m1 + m2, "|", repr(m1), "|", m1 == m2, "|", m1 < m2)
print("len:", len(m1), "| call:", m2(3))
