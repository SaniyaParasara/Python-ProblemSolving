# Practical No. 10

# Question:
# Write a program to generate a sequence of numbers
# using generator functions and the yield keyword.

# Generator Function
def numbers():

    # Generate numbers from 1 to 5
    for i in range(1, 6):
        yield i

# Create generator object
gen = numbers()

print("Generated Numbers:")

# Print generated values
for value in gen:
    print(value)
