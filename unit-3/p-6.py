# 26. Write a Python program to perform file and directory operations using os and sys modules.

import os
import sys

print("Current directory:", os.getcwd())
os.mkdir("test_folder")                       # Create directory
print("Created:", os.path.exists("test_folder"))
with open("test_folder/sample.txt", "w") as f:
    f.write("Hello")
print("Files:", os.listdir("test_folder"))
print("Is file:", os.path.isfile("test_folder/sample.txt"))
print("File size:", os.path.getsize("test_folder/sample.txt"), "bytes")
os.rename("test_folder/sample.txt", "test_folder/renamed.txt")
os.remove("test_folder/renamed.txt")          # Delete file
os.rmdir("test_folder")                       # Delete directory

# sys module
print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Arguments:", sys.argv)
