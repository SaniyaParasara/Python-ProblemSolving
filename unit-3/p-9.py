# 29. Write a Python program to use re module functions such as match, search and findall.

import re

text = "Python is easy. Python is powerful. Learn Python 3."

# match() - checks only at the beginning
m = re.match(r"Python", text)
print("match:", m.group() if m else None)

# search() - first occurrence anywhere
s = re.search(r"powerful", text)
print("search:", s.group(), "at", s.span())

# findall() - all occurrences
print("findall:", re.findall(r"Python", text))
print("Numbers:", re.findall(r"\d+", text))

# split() and sub()
print("split:", re.split(r"\.\s*", text))
print("sub:", re.sub(r"Python", "Java", text))
