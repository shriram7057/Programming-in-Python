#  • We can have both normal and keyword variable numbers of 
# arguments.
#  • The special syntax *
#  args in function definitions in Python is used to pass a 
# variable number of arguments to a function. It is used to pass a non
# keyworded, variable-length argument list.
#  • The special syntax **kwargs in function definitions in Python is used to pass a 
# keyworded, variable-length argument list. We use the name kwargs with the 
# double star. The reason is that the double star allows us to pass through 
# keyword arguments (and any number of them).

def myfun1(*argv):
    for age in argv:
        print(argv)

def myfun2(**kwargs):
    for key,values in kwargs.items():
        print("%s==%s"%(key,values))

#Driver code 
print("Result of *args:")

myfun1('Hello','Welcome','to','Geeks for Geeks')

print("/nResult of **kwargs")

myfun2(first='Geeks',mid='for',last='Geeks')