#Program to Print Multiplication Table of the Given Number!

#Get the input From User

number=int(input("Enter a Number :"))

#Loop Form 1 to 10 for print the mltiplication Table

for i in range(1,11):
    #print the Multiplication Table
    print(number,"x",i,"=",number*i)