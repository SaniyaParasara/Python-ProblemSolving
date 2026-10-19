# 31. Write a Python program to create a class and object in Python.

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name, "| Roll No:", self.roll_no)

s1 = Student("Saniya", 101)
s2 = Student("Rahul", 102)
s1.display()
s2.display()
