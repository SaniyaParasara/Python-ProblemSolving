# Practical No. 8

# Question:
# Write a program to illustrate variable scope
# using local, global and nonlocal variables.

# Definition:
# Variable scope is the region where a variable
# can be accessed.
# Local variable    -> Declared inside a function.
# Global variable   -> Declared outside a function.
# Nonlocal variable -> Declared in an outer function
#                      and modified inside an inner function.

# Global Variable
x = 100

# Outer Function
def outer():

    # Local Variable
    y = 50

    # Inner Function
    def inner():

        # Nonlocal Variable
        nonlocal y

        # Modify local variable of outer function
        y = 75

        print("Inside Inner Function =", y)

    # Call inner function
    inner()

    print("Inside Outer Function =", y)

# Call outer function
outer()

# Print global variable
print("Global Variable =", x)
