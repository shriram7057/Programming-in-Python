# 1) len() this method is used to find out how many elements present in the list

a=(10,20,30,40,50,60)
print("Length of the Tuple =",len(a))

# 2) del() this del keyword is used to delete the complete list 

# b=(11,22,33,44,55)
# del b
# print("Tuple after perform the del operation:",b)    #  Error name b is not defined

# 3) index() this method find out the given element in the tuple and returns its index Number , if the same element is 
# present more than once , the method returns the index og the first occurence of the element 

c=(10,20,30,40,50)
print("Index of the Given element is :",c.index(40)) 

# 4) count() this method counts how many items an element present in tuple and returns it.

d=(22,33,44,55,66,77)
print("Counts of 33 element is:",d.index(33))

# 5) min() this method is used to find out minimum element in Tuple 

e=(100,999,333,222,333)
print("Minimum element is Tuple is:",min(e))

# 6) max() this method is used to find out maximum element in Tuple 

f=(100,999,333,222,333)
print("Maximum element is Tuple is:",max(f))




