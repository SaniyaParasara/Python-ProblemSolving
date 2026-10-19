# 41. Write a Python program to demonstrate different types of errors and exceptions in Python.

# Syntax errors are detected before running, e.g.  print("Hi"   (missing bracket)

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

try:
    int("abc")
except ValueError as e:
    print("ValueError:", e)

try:
    print([1, 2, 3][5])
except IndexError as e:
    print("IndexError:", e)

try:
    print({"a": 1}["b"])
except KeyError as e:
    print("KeyError:", e)

try:
    print("5" + 5)
except TypeError as e:
    print("TypeError:", e)

try:
    print(undefined_var)
except NameError as e:
    print("NameError:", e)

try:
    open("no_such_file.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
