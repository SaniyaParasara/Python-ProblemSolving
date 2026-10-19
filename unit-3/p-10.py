# 30. Write a Python program to extract specific information from a text file using regular expressions.

import re
import os

# Create a sample file
with open("data.txt", "w") as f:
    f.write("Name: Saniya, Phone: 9876543210, Email: saniya@gmail.com\n")
    f.write("Name: Rahul, Phone: 9123456780, Email: rahul@yahoo.com\n")

with open("data.txt", "r") as f:
    content = f.read()

print("Phones:", re.findall(r"\b\d{10}\b", content))
print("Emails:", re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", content))
print("Names:", re.findall(r"Name:\s(\w+)", content))
os.remove("data.txt")
