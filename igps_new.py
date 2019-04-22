#!/usr/bin/env python3

from subtask_3 import iGPS, Sound

r1 = int(input("Input r1: "))
r2 = int(input("Input r2: "))
r3 = int(input("Input r3: "))
x1 = 6
y1 = -6
x2 = 6
y2 = 114
x3 = 102
y3 = 114

x = (-(y2 - y3)*((y2**2-y1**2)+(x2**2-x1**2)+(r1-r2)) + (y1-y2)*((y3**2-y2**2)+(x3**2-x2**2)+(r2-r3)))/(2*((x1-x2)*(y2-y3) - (x2-x3)*(y1-y2)))
y = (-(x2 - x3)*((x2**2 - x1**2) + (y2**2 - y1**2) + (r1 - r2))+((x1-x2)*((x3**2-x2**2)+(y3**2-y2**2)+(r2-r3))))/(2*((y1-y2)*(x2-x3) - (y2-y3)*(x1-x2)))

print("r1: " + str(r1))
print("r2: " + str(r2))
print("r3: " + str(r3))

print("x: " + str(x))
print("y: " + str(y))
