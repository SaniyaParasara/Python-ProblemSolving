# UNIT 3 - Q9: Write a program to use re module functions such as match(),
#               search() and findall().
# SCENARIO: Validating and searching user input on a website - check if a
#           string starts with a pattern, find the first date, list all numbers.

import re

text = "Order 4521 placed on 15-08-2025 by amit@gmail.com. Order 4522 on 16-08-2025."

# match() - checks only at the BEGINNING of the string
print("match Order  :", re.match(r"Order", text) is not None)
print("match placed :", re.match(r"placed", text))

# search() - first occurrence anywhere
m = re.search(r"\d{2}-\d{2}-\d{4}", text)
print("search date    :", m.group(), "| span:", m.span())

# findall() - list of ALL occurrences
print("findall orders :", re.findall(r"Order (\d+)", text))
print("findall dates  :", re.findall(r"\d{2}-\d{2}-\d{4}", text))
print("findall email  :", re.findall(r"[\w.]+@[\w.]+\.\w+", text))

# finditer() - positions of every match
for mt in re.finditer(r"\d{4}", text):
    print("  4-digit", mt.group(), "at", mt.start())

# Validate input
for phone in ("9876543210", "12345", "98765abcde"):
    print(phone, "->", "valid" if re.fullmatch(r"[6-9]\d{9}", phone) else "invalid")
