from math import *
x = int(input())
y = int(input())
z = int(input())

a = (2 * cos(x - pi / 6) ** 4) / (0.5 + sin(y) ** 2)
b = 1 + ((z ** 2) / (3 + (z ** 2 / 5)))

print(a)
print(b)
