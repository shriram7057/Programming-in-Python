#importing math module to use pi
import math

# input for radius and height
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))

# Calculate the Volume of the Cylinder -> Formula [Volume = π * r² * h]
Volume = math.pi * radius * radius * height

# Calculating surface area of Cylinder -> Formula [Surface Area = 2πr(r+h)]
sur_area = 2 * math.pi * radius * (radius + height)

# Printing the result
print(f"The Volume of a Cylinder is: {Volume:.2f}")

# Printing Surface Area
print(f"The Surface Area of a Cylinder is: {sur_area:.2f}")
