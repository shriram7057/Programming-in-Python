#  • To specify that a function can have only keyword arguments, add *, before the arguments:

def myfunction(*,x):
    print(x)
myfunction(x=3)

#  Without the *, you are allowed to use positionale arguments even if the function expects 
# keyword arguments

def myfunction(x):
    print(x)
myfunction(4)

# But when adding the *, / you will get an error if you try to send a positional argument:

def myfunction(*,x):
    print(x)
myfunction(5)
