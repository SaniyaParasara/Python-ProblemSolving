# 43. Write a Python program to define and raise user-defined exceptions.

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 60"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. Given: {age}")

def check_age(age):
    if age < 18 or age > 60:
        raise InvalidAgeError(age)
    print("Valid age:", age)

for a in (25, 10):
    try:
        check_age(a)
    except InvalidAgeError as e:
        print("Custom exception caught:", e)
