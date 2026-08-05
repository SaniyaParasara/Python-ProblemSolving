# Practical No. 4

# Question:
# Write a program to find the sum of digits
# of a number using a while loop.

# Definition:
# A while loop executes a block of code repeatedly
# as long as the given condition is True.
# In this program, the while loop is used to
# extract each digit of a number and calculate
# the sum of all digits.

# Taking input from the user
num = int(input("Enter a number: "))

# Variable to store the sum
sum = 0

# Loop runs until the number becomes 0
while num > 0:

    # Get the last digit
    digit = num % 10

    # Add the digit to the sum
    sum = sum + digit

    # Remove the last digit
    num = num // 10

# Display the result
print("Sum of digits =", sum)
