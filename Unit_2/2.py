# Practical No. 2

# Question:
# Write a program to check whether a number is
# Positive, Negative or Zero using nested conditions.

# Taking input from the user
num = int(input("Enter a number: "))

# First (Outer) if condition
if num >= 0:

    # Nested (Inner) if condition
    if num == 0:
        print("The number is Zero.")
    else:
        print("The number is Positive.")

# Outer else block
else:
    print("The number is Negative.")
