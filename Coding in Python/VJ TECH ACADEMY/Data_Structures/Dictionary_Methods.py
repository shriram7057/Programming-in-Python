# 1) len() This method is used to find out the how many items (key:value pairs) present in dictionary. 
  
a = {1:'Pune', 2:'Solapur', 3:'Tuljapur', 4:'Thane'} 
print("Length of Dictionary=",len(a)) 

# 2) del() The del keyword is used to delete the specified key name or it can also delete the complete dictionary 
b = {1:'Pune', 2:'Solapur', 3:'Tuljapur', 4:'Thane'} 
del a[1] 
print("list after deleting key 1 =", b) 

#if you want to delete complete dictionary 
# del a

# 3) pop() & popitem() :- The pop() method is used to remove the specified key value from the dictionary. 
# The popitem() method is used to remove the last inserted element from the dictionary.
#  
c = {1:'Pune', 2:'Solapur', 3:'Tuljapur', 4:'Thane'} 
c.pop(1) 

print("Dictionary after removing key 1=", a) 
a.popitem() 

print("Dictionary after removing last element=", a)

# 4) clear() this method is used to make an empty list

d = {1:'Pune', 2:'Solapur', 3:'Tuljapur', 4:'Thane'} 
d.clear() 
print("Elements of Dictionary=",d) 

# 5) copy() this method is used copy all elements of one dictionary to another dictionary

e = {1:'Pune', 2:'Solapur', 3:'Tuljapur', 4:'Thane'} 
f=e.copy(); 
print("Copied dict b elements =", b) 

# 6) min() :- This method is used to find out the minimum key element in the dictionary.

g = {1:'Pune', 2:'Solapur', 3:'Tuljapur', 4:'Thane'} 
print("Minimum key element =", min(g))

# 7)  max() :- This method is used to find out the maximum key element in the dictionary.

h={1:"MUMBAI",2:"DEHLII",3:"PUNE",4:"KOLHAPUR"}
print("Maximum key element =",max(h))

# 8) get() this method is used to returns the value for the specified key if key is in dictionary.

i={1:"SHRIRAM",2:"SITAA",3:"LAXAMAN"}
print("Value of 3 is ",i.get(3))

# 9) update() this method is used to update the dictionary . if key value is already present then its corresponding value 
# will get chnaged . if value not present then it will add new entry in the dectionary .

j={1: "one", 2: "three"}
k={2:"TWO"}
 
# updates the value of key 2 

j.update(k)
print("Updated Dictionary:",j)

j1={3:"THREE"}
j.update(j1)
print("updated Dictionary",j)

# 10) keys & Values()  the key Method display list of all keys in the dictionary , the values () method display list of 
# all values in the dictionary

l={1:"SHRIRAM",2:"DATTATRAY",3:"LAHANE"}
print("All keys in the Dictionary :",l.keys())
print("All Values in the Disctionary :",l.values())