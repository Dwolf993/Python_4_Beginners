#Write a Python program which accepts the radis of a circle from the user and compute the area
from math import pi

print("Please enter the vaule of radius:\n\t\t\t r = ")
radius = float(input())
#print(radius)
Area = (radius ** 2) * pi
print("Area of the circle is: " + str(Area) )
