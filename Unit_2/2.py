# Practical No. 2

# Question:
# Write a program to check whether a number is
# Positive, Negative or Zero using nested conditions.

# Definition:
# Nested if means writing one if statement inside another if statement.
# It is used when one condition depends on another condition.
# In this program, we first check whether the number is
# greater than or equal to zero.
# If yes, we again check whether it is zero or positive.
# Otherwise, the number is negative.

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
