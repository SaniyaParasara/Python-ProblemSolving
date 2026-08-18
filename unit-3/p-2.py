# Q2. Write a program to demonstrate different import mechanisms in Python


import math
print(math.sqrt(16))

import math as m
print(m.factorial(5))

from math import pow
print(pow(2, 3))


from math import *
print(sin(0))