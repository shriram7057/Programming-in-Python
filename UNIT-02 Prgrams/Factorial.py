#Function to calculate Factorial

def fact(number):
    fact=1
    for i in range(2,number+1):  # loop from 2 to n
        #multiply f by i
        fact*=i
    return fact

#Get User input
number=int(input("Enter a Number :"))

#Print Factorial of the number

print("Factorial of Number=",fact(number))