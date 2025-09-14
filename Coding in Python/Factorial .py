# Factorial calculation using loop
# inout from user 
num=int(input("Enter a Number:"))

#Initialize factorial to 1
factorial=1

#Calculate factorial using a loop
for i in range(1,num+1):
    factorial*=i #Multiply current number with factorial 

#Print the result
print(f"Factorial of {num} is {factorial}")   