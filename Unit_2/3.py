# Practical No. 3

# Question:
# Write a program to generate a multiplication table
# using a for loop.

# Definition:
# A for loop is used to execute a block of code
# repeatedly for a fixed number of times.
# In this program, the for loop generates the
# multiplication table of a given number.

# Taking input from the user
num = int(input("Enter a number: "))

# Using for loop to print multiplication table
for i in range(1, 11):

    # Print the multiplication table
    print(num, "x", i, "=", num * i)
