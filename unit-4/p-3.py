# 33. Write a Python program to illustrate instance variables and class variables.

class Employee:
    company = "TechSoft"                        # Class variable (shared)

    def __init__(self, name, salary):
        self.name = name                        # Instance variable
        self.salary = salary

e1 = Employee("Saniya", 50000)
e2 = Employee("Rahul", 45000)
print(e1.name, e1.salary, e1.company)
print(e2.name, e2.salary, e2.company)

Employee.company = "NewTech"                    # Changing the class variable
print("After change:", e1.company, e2.company)
