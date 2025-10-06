#program to find out Whether the input number is perfect number or not 

#Get the input form user
number=int (input("Enter a Number : "))

#Find the sum of divisiors

sum_of_Divisiors=sum(i for i in range(1,number))

if number%i==0 :   # check if the sum of dividiors equals the number

    if sum_of_Divisiors==number:
        print(number,"Number is Perfect Number :")
    else:
        print(number,"Number is Not Perfect :")