# One important thing to note is, in Python every variable name is a 
# reference. When we pass a variable to a function, a new reference to the 
# object is created. Parameter passing in Python is the same as reference 
# passing in Java. To confirm this Python’s built-in id() function is used in the 
# below example

def myfunction(x):
    print("Value Received :",x,"id",id(x))

#Driver Code 
x=12
print("Value Passed",x,"id",id(x))

myfunction(x)