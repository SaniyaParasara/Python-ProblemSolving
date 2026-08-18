# Practical No. 3

# Question:
# Write a program to generate a multiplication table
# using a for loop.

# Taking input from the user
num = int(input("Enter a number: "))

# Using for loop to print multiplication table
for i in range(1, 11):

    # Print the multiplication table
    print(num, "x", i, "=", num * i)
