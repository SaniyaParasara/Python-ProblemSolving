# 32. Write a Python program to demonstrate constructor and destructor usage.

class Demo:
    def __init__(self, name):                   # Constructor
        self.name = name
        print("Constructor called for", self.name)

    def __del__(self):                          # Destructor
        print("Destructor called for", self.name)

obj = Demo("Object1")
print("Using object:", obj.name)
del obj                                         # Triggers destructor
