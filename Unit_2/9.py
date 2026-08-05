# Practical No. 9

# Question:
# Write a program to demonstrate
# iterators and iterables in Python.

# Definition:
# An iterable is an object that can be
# traversed using a loop.
# An iterator is an object that returns
# one element at a time using next().

# Creating an iterable (List)
numbers = [10, 20, 30, 40]

print("Iterable:")
print(numbers)

# Converting iterable into iterator
it = iter(numbers)

print("\nIterator Output:")

# Accessing elements one by one
print(next(it))
print(next(it))
print(next(it))
print(next(it))
