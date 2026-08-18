# Q1. Write a program to create and import a user defined module

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

def power(a, b):
    return a ** b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b

def square(a):
    return a * a

def square_root(a):
    return a ** 0.5

def cube(a):
    return a ** 3