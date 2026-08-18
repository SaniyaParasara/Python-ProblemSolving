# Practical No. 4

# Question:
# Write a program to find the sum of digits
# of a number using a while loop.


# Taking input from the user
num = int(input("Enter a number: "))

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
