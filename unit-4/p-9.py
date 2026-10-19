# 39. Write a Python program to read and write data into a file using different file modes.

# Write mode
with open("demo.txt", "w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: Python\n")

# Append mode
with open("demo.txt", "a") as f:
    f.write("Line 3: File Handling\n")

# Read mode
with open("demo.txt", "r") as f:
    print("read():\n" + f.read())

with open("demo.txt", "r") as f:
    print("readline():", f.readline().strip())
    print("readlines():", f.readlines())

# Read + Write mode
with open("demo.txt", "r+") as f:
    f.write("LINE")
    f.seek(0)
    print("r+ mode:", f.read())
