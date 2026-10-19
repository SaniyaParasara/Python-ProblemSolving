# 35. Write a Python program to implement single, multilevel and multiple inheritance.

# Single inheritance
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

# Multilevel inheritance
class Puppy(Dog):
    def weep(self):
        print("Weeping...")

# Multiple inheritance
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def hobbies(self):
        print("Cooking")

class Child(Father, Mother):
    pass

d = Dog(); d.eat(); d.bark()
p = Puppy(); p.eat(); p.bark(); p.weep()
c = Child(); c.skills(); c.hobbies()
