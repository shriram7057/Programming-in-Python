# 1) len() :- This method is used to find out the how many items present in list.  
 
a = {10,20,30,40,50} 
print("Length of set=",len(a))

# 2) add() :- To add new item to the set, we use the add() method 

a = {10,20,30,40,50} 
a.add(60) 
print("All elements of set=", a) 

# 3) update() :- To add multiple items to the set, we use the update() method.

a = {10,20,30,40,50} 
a.update([60,70,80]); 
print("All elements of set=", a) 

# 4) del :- The del keyword is used to delete the set completely.  

# a = {10,20,30,40,50} 
# del a 
# print(a)  # NameError: name 'a' is not defined

# 5) remove() :- This method is used to remove the specified item from the set.
  
a = {10,20,30,40,50} 
a.remove(40) 
print("Set after removing 40 value=", a) 

# 6) pop() :- This method is used to remove remove the last item. Remember that sets are unordered, so 
# you will not know what item that gets removed. The return value of the pop() method is the removed item.
  
a = {10,20,30,40,50} 
print("Removed Element=", a.pop()) 

# 7) clear() :- This method is used to make an empty list.

a = {10,20,30,40,50} 
a.clear() 
print("Set elements=",a)

# 8) union() :- This method return a set that contains all items from both sets, duplicates are removed. 

a = {10,20,30,40,50} 
b={20,60,70} 

c=a.union(b) 
print("Union set=",c) 

# 9) difference() :- This method return set that contains the items that only exist in set a, and not in set b.

a = {10,20,30,40,50} 
b={20,60,70} 

c=a.difference(b) 
print("Difference set=",c)

# 10) intersection() :- This method return a set that contains the items that exist in both set a and b.
  
a = {10,20,30,40,50} 

b={20,60,70,40}

c=a.intersection(b) 
print("Intersection set=",c) 