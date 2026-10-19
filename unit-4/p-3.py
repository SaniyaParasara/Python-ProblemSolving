# UNIT 4 - Q3: Write a program to illustrate instance variables and class variables.
# SCENARIO: In a school, every student has own name/marks (instance variables)
#           but all share the same school name and student count (class variables).

class Student:
    school = "ABC University"        # class variable (shared)
    count = 0

    def __init__(self, name, marks):
        self.name = name             # instance variables (separate per object)
        self.marks = marks
        Student.count += 1

s1 = Student("Amit", 80)
s2 = Student("Riya", 90)
print(s1.name, s1.marks, s1.school)
print(s2.name, s2.marks, s2.school)
print("Total students:", Student.count)

Student.school = "XYZ University"    # change via class -> affects all
print("After class change:", s1.school, s2.school)

s1.school = "Private School"         # creates instance variable for s1 only
print("s1:", s1.school, "| s2:", s2.school, "| class:", Student.school)
print("s1.__dict__:", s1.__dict__)
