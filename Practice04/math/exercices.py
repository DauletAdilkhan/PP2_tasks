### 1: Write a Python program to convert degree to radian.

import math
d= int(input("Input degree: "))
print("In radian:",(math.radians(d)))


### 2: Write a Python program to calculate the area of a trapezoid.

import math

h=int(input("height: "))
fv=int(input("first base: "))
sv=int(input("second base: "))
print("Area is:",(fv+sv)/2*h)


### 3:Write a Python program to calculate the area of regular polygon.

import math 

nos=int(input("Input number of sides:"))
tloas=int(input("Input the length of a side:"))
print("Area of the polygon is:",int(nos*pow(tloas,2)/(4*math.tan(math.pi/nos))))


### 4:Write a Python program to calculate the area of a parallelogram.
import math

l=int(input("Length of base: "))
h=int(input("Height of parallelogram: "))
print("the area of a parallelogram:",l*h)