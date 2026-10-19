# UNIT 5 - Q2: Write a program to handle exceptions using try, except, else
#               and finally blocks.
# SCENARIO: A file-reading / division tool must never crash: show a friendly
#           message on error, run extra code on success (else) and always close
#           resources (finally).

import sys, os
from io import StringIO

def divide():
    try:
        a = int(input("Enter numerator  : "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("Please enter integers only")
    except ZeroDivisionError:
        print("Denominator cannot be zero")
    except Exception as e:
        print("Unexpected:", e)
    else:
        print("Result =", result)              # only if no exception
    finally:
        print("Done (finally always executes)\n")

def read_file(name):
    f = None
    try:
        f = open(name)
        print("First line:", f.readline().strip())
    except FileNotFoundError:
        print(name, "not found")
    finally:
        if f:
            f.close()
            print("File closed")

if sys.stdin.isatty():
    divide()
else:                                           # demo values when not interactive
    for data in ("10\n2\n", "10\n0\n", "ten\n2\n"):
        sys.stdin = StringIO(data)
        divide()
read_file("notfound.txt")
with open("t.txt", "w") as f: f.write("Hello file\n")
read_file("t.txt")
os.remove("t.txt")
