#  We used thePosition argument
#  during the function call so that the first argument (or value) is assigned to 
# name and the second argument (or value) is assigned to age. By changing the position, or if you forget the 
# order of the positions, the values can be used in the wrong places, as shown in the Case-2 example below, 
# where 27 is assigned to the name and Suraj is assigned to the age

def nameAge(name,Age):
    print("Hi am ",name)
    print("My age is ",Age)

#You will get correct output Because arguments is Given in Oreder 

print("Case-1:")
nameAge("Shriram",20)

#You will Get incorrect output Because arguments is not in order 

print("/nCase2:")
nameAge(20,"Shriram")