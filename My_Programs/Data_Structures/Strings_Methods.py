a="PYTHON"
b="LANGUAGE"

print("First String=",a)
print("Second String=",b)

# 1) len() this function returns number of characters in the string 
print("Length of First String",len(a))
print("Length of Second String",len(b))

# 2)min() Functio returns the smallest character in a String (Chronological oreder as per ASCII)
print("Smallest Character in First String=",min(a))
print("Smallest Character in Second String=",min(b))

# 3)max() Functio returns the largest character in a String (Chronological oreder as per ASCII)
print("Largest Character in First String=",max(a))
print("Largest Character in Second String=",max(b))

# 4)del This keyword is used to delete the entire String
# del a
# print("Deleted String=",a) # op  NameError: name ‘a' is not defined

# 5) String concatenation and multiplication 
# a+b
print("Concatinated String=",(a+b))

print("After perform the a*3 operation=",(a*3))


# Traversing a string
for ch in a:
    print(ch,end="")

#Strings are immutable

a[2]="z"         # Give an TypeError: 'str' object does not support item assignment because strings are immutable


#  ‘in’ and ‘not in’ operator.
#  String slicing.
#  String comparison.
