# Program to Generate Student result Accept mark of five subjects and display results according to the following table
# >=75  First class with distinction
# >=60 and <75 First Class
# >=45 and <60 Second class
# >=40 and <45 Pass
# <40 Fail 

# Accept marks for five subjects
marks1 = float(input("Enter marks for subject 1: ")) 
marks2 = float(input("Enter marks for subject 2: ")) 
marks3 = float(input("Enter marks for subject 3: ")) 
marks4 = float(input("Enter marks for subject 4: ")) 
marks5 = float(input("Enter marks for subject 5: "))

# Calculate the total and percentage
total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100

# Display the result based on the percentage
if percentage >= 75:
    print("Result: First class with distinction")

elif percentage >= 60:
    print("Result: First Class")

elif percentage >= 45:
    print("Result: Second class")

elif percentage >= 40:
    print("Result: Pass")

else:
    print("Result: Fail")
