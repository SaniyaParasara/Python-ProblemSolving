# Q4. Write a program to generate random numbers using random module
import random

print("Random float (0-1):", random.random())
print("Random integer (1-100):", random.randint(1, 100))
print("Random from list:", random.choice([10, 20, 30, 40]))

lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print("Shuffled list:", lst)