# UNIT 4 - Q10: Write a program to perform file pointer operations using
#                seek() and tell() methods.
# SCENARIO: Reading a large log or fixed-size record file: jump directly to
#           the required position instead of reading everything from the start.

import os

with open("sample.txt", "w+") as f:
    f.write("Python Programming for MCA Students")
    print("After write, tell() :", f.tell())

    f.seek(0)                                   # go to start
    print("Read 6 chars        :", f.read(6), "| tell:", f.tell())

    f.seek(7)                                   # absolute position
    print("From position 7     :", f.read(11), "| tell:", f.tell())

    f.seek(0, 2)                                # 2 = end of file
    print("File size (end)     :", f.tell())

    f.seek(0)
    f.write("JAVA  ")                           # overwrite at start
    f.seek(0)
    print("After overwrite     :", f.read())

# binary mode: relative seeks allowed
with open("sample.txt", "rb") as f:
    f.seek(-8, 2)                               # 8 bytes before end
    print("Last 8 bytes        :", f.read())
    f.seek(7)
    f.seek(3, 1)                                # 3 forward from current
    print("Position            :", f.tell())
os.remove("sample.txt")
