import numpy as np

a = int(-300)
h = int(25)
for x in range(325, 575, h):
    f = ((x ** 0.5) / ((x + a) ** 0.5)) + 0.5 * x
    print(f/100)
