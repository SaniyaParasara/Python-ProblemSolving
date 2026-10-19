# 44. Write a Python program to demonstrate the use of assert statement.

def calculate_average(marks):
    assert len(marks) > 0, "Marks list cannot be empty"
    return sum(marks) / len(marks)

print("Average:", calculate_average([80, 90, 70]))

x = 10
assert x > 5, "x must be greater than 5"
print("Assertion passed")

try:
    calculate_average([])
except AssertionError as e:
    print("AssertionError:", e)
