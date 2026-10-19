# UNIT 5 - Q4: Write a program to demonstrate the use of assert statement.
# SCENARIO: A marks / payroll function must never receive invalid values;
#           assert stops the program during development if a condition that
#           "must be true" is false. (Disabled with: python -O file.py)

def average(marks):
    assert len(marks) > 0, "marks list cannot be empty"
    assert all(0 <= m <= 100 for m in marks), "each mark must be between 0 and 100"
    return sum(marks) / len(marks)

def discount(price, percent):
    assert price > 0, "price must be positive"
    assert 0 <= percent <= 100, "percent must be 0-100"
    return price - price * percent / 100

print("Average :", average([80, 90, 70]))
print("Discount:", discount(1000, 20))

for func, args in ((average, ([],)), (average, ([50, 150],)), (discount, (-5, 10))):
    try:
        func(*args)
    except AssertionError as e:
        print("AssertionError ->", e)

x = 10
assert x == 10                      # passes silently
print("assert x == 10 passed")
try:
    assert isinstance(x, str), "x must be a string"
except AssertionError as e:
    print("AssertionError ->", e)
