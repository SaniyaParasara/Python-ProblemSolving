# 42. Write a Python program to handle exceptions using try, except, else and finally blocks.

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Invalid data type")
    else:
        print("Result:", result)                # Runs only if no exception
    finally:
        print("Execution completed\n")          # Always runs

divide(10, 2)
divide(10, 0)
divide(10, "a")
