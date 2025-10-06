#Function to calculate area of a square

def Calculate_area(side):
    return side*side         #Formula to calculate Area of Sq. Area=Side*side

#Function to Calculate Perimeter of a Square

def Calculate_perimeter(side):
    return 4*side             #Formula to calculate Perimeter of a Sq.per=4*side

#Taking user input for the side of the square 

side=int(input("Enter the side length of the square:"))

#calculate area and perimeter

area=Calculate_area(side)
perimeter=Calculate_perimeter(side)

#Displaying the result

print("Area of a Square=",area)
print("Perimeter of a Square=",perimeter)