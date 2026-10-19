# 34. Write a Python program to demonstrate instance methods, class methods and static methods.

class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

    def show(self):                             # Instance method
        print("Student:", self.name, "| College:", self.college)

    @classmethod
    def change_college(cls, new_name):          # Class method
        cls.college = new_name

    @staticmethod
    def is_adult(age):                          # Static method
        return age >= 18

s = Student("Saniya")
s.show()
Student.change_college("XYZ University")
s.show()
print("Is adult (20):", Student.is_adult(20))
