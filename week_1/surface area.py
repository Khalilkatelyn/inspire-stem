#this is a programme to calculate surface areas
#date : 21/02/2024
#name : kate lynn

#surface area of a cylinder

import math

r = int(input("enter the radius of the cylinder : " ))
pi = float(math.pi)
d = int(input("enter the diameter"))
h = int(input("enter the height"))

surface_area = (2 * pi * (r**2)) + (2 * pi * r * h)

print("the surface area of a cylinder is : ",surface_area)




