#Program to find best of two test average marks out of three test marks acepted from the user 

#Accept three test marks from te user 
a=float(input("Enter First test Marks :"))
b=float(input("Enter Second test Marks :"))
c=float(input("Enter Third test Marks :"))

#Find the sum of the best two Marks by removing the lowest one 

best_two_avg=(a+b+c-min(a,b,c)/2)

#print the result 

print("Best two test average marks :",best_two_avg)