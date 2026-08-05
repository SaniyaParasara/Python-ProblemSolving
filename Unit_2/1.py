# Practical No. 1
# Question:
# Write a program to demonstrate conditional statements using
# if, if-else and if-elif-else.

# Definition:
# Conditional statements are used to make decisions in a program.
# if -> Executes a block only when the condition is True.
# if-else -> Executes one block if the condition is True,
#            otherwise executes another block.
# if-elif-else -> Checks multiple conditions one by one.

# Taking input from user
num = int(input("Enter a number: "))

# if statement
if num > 0:
    print("Positive Number")

# if-else statement
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# if-elif-else statement
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
