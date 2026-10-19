# UNIT 4 - Q2: Write a program to demonstrate constructor and destructor usage.
# SCENARIO: A database-connection object opens a connection when created
#           (constructor) and closes it automatically when destroyed
#           (destructor) so resources are never leaked.

class DBConnection:
    def __init__(self, name):                       # constructor
        self.name = name
        print(f"[OPEN]  Connection to {self.name} opened")

    def query(self, sql):
        print(f"  Running: {sql}")

    def __del__(self):                               # destructor
        print(f"[CLOSE] Connection to {self.name} closed")

class Rectangle:                                     # parameterized / default ctor
    def __init__(self, l=1, b=1):
        self.l, self.b = l, b
    def area(self):
        return self.l * self.b

c = DBConnection("college_db")
c.query("SELECT * FROM student")
del c                                                # destructor called here
print("After delete")
print(Rectangle().area(), Rectangle(4, 5).area())
