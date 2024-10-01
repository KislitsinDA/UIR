from math import *

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

st1 = abs(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
st2 = abs(sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2))
st3 = abs(sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2))
p = (st3 + st2 + st1)/2
s = sqrt( p * (p - st1) * (p - st2) * (p - st3) )
rad = s/p
print(s)
print(rad)
