# UNIT 4 - Q9: Write a program to read and write data into a file using
#               different file modes.
# SCENARIO: A diary / log app creates a file, appends a new entry every day and
#           reads everything back; a copy tool uses binary mode for images.

import os

with open("diary.txt", "w") as f:                 # w: create / overwrite
    f.write("Day 1: Started Python\n")
    f.writelines(["Day 2: Learned files\n", "Day 3: Learned OOP\n"])

with open("diary.txt", "a") as f:                 # a: append
    f.write("Day 4: Exceptions\n")

print("---- read() ----")
with open("diary.txt", "r") as f:                 # r: read
    print(f.read())

with open("diary.txt") as f:
    print("readline :", f.readline().strip())
    print("readlines:", [l.strip() for l in f.readlines()])

try:
    with open("diary.txt", "x") as f:             # x: error if file exists
        pass
except FileExistsError:
    print("x mode -> file already exists")

with open("diary.txt", "r+") as f:                # r+: read + write
    print("r+ first line:", f.readline().strip())

with open("data.bin", "wb") as f:                 # wb: binary write
    f.write(bytes([65, 66, 67, 68]))
with open("data.bin", "rb") as f:                 # rb: binary read
    print("Binary:", f.read())

for fn in ("diary.txt", "data.bin"):
    os.remove(fn)
