# UNIT 4 - Q4: Write a program to demonstrate instance methods, class methods
#               and static methods.
# SCENARIO: An employee system: instance method for salary, class method to
#           change company-wide bonus or build from a string, static method for
#           a utility check that needs no object data.

class Employee:
    bonus_percent = 10

    def __init__(self, name, salary):
        self.name, self.salary = name, salary

    def total_salary(self):                        # instance method (self)
        return self.salary + self.salary * Employee.bonus_percent / 100

    @classmethod
    def set_bonus(cls, p):                         # class method (cls)
        cls.bonus_percent = p

    @classmethod
    def from_string(cls, s):
        n, sal = s.split(",")
        return cls(n, int(sal))

    @staticmethod
    def is_working_day(day):                       # static method
        return day not in ("Sat", "Sun")

e1 = Employee("Amit", 50000)
e2 = Employee.from_string("Riya,60000")
print(e1.name, e1.total_salary())
Employee.set_bonus(20)
print("After bonus change:", e1.total_salary(), e2.total_salary())
print("Mon working?", Employee.is_working_day("Mon"), "| Sun?", e1.is_working_day("Sun"))
