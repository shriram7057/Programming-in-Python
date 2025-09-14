#  You can combine the two argument types in the same function.
#  • Any argument before the / , are positional-only, and any argument 
# after the *, are keyword-only

def myfunction(a,b,/,*,c,d):
    print(a+b+c+d)
myfunction(5,6,c=7,d=8)

# op=26

