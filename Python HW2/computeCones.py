#Maciej Sudol
#Python Program to find Volume and Surface Area of a Cone
#computeCones


import math

print("This program takes a number input from the user and calculates the surface area and the volume of a cone")

radius = float(input('Please Enter the Radius of a Cone(a non-negative number): '))
height = float(input('Please Enter the Height of a Cone(a non-negative number): '))

#Calcullate length of side (slant)

a = math.sqrt(radius * radius + height * height)

# Calculate the Surface Area

Surface_Area = math.pi * radius * (radius + a)

# Calculate the Volume

Volume = (1.0/3) * math.pi * radius * radius * height

print("The height of the cone is: " ,height)
print("The raius of the radius of the cone is: " ,radius)
print("The Surface Area of a Cone = %.2f: " %Surface_Area)
print("The Volume of a Cone = %.2f: " %Volume);


