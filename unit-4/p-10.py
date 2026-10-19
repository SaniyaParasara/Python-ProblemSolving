# 40. Write a Python program to perform file pointer operations using seek and tell methods.

import os

with open("pointer.txt", "w") as f:
    f.write("Python File Handling")

with open("pointer.txt", "r") as f:
    print("Initial position:", f.tell())
    print("Read 6 chars:", f.read(6))
    print("Position now:", f.tell())
    f.seek(7)                                   # Move pointer to index 7
    print("After seek(7):", f.read(4))
    f.seek(0)                                   # Back to beginning
    print("After seek(0):", f.read())
os.remove("pointer.txt")
os.remove("demo.txt") if os.path.exists("demo.txt") else None
