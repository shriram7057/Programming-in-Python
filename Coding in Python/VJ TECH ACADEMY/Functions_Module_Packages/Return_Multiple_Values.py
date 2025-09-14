# return multiple values 
def Addition():
    a=int (input("Enter First Number"))
    b=int (input("Enter Second Number"))
    c=a+b
    return (a,b,c)
m,n,o=Addition()
print("Addition of ",m,"and",n,"is",o)