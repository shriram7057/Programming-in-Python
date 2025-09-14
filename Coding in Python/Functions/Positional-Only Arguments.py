#  You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#  •To specify that a function can have only positional arguments, add  , / after the arguments:
def my_fun(x,/):
    print(x)

my_fun(3)


# Without the , / you are actually allowed to use keyword arguments even if the function expects 
# positional arguments:

def myfunction(x):
    print(x)
myfunction(x=3)


# But when adding the , / you will get an error if you try to send a keyword argument:
def my_function(x, /):
    print(x)

my_function(x=3)