# 1) len() - this method is used to find out how many items presents in list

a=[10,20,30,40,50,60]
print("Length of the list=",len(a))      #Syntax-> print Method,len(var_name)

# 2) append() - To add an item to the end of the list we use the append method 

b=[11,22,33,44,55,66]

b.append(70)                    #Syntax-> var_Name.append(element)
print("All items in list after perform append method=",b)

# 3) extend() - to add number of items to the end of the list we use the extend Method

c=[0,1,2,3,4]
c.extend([5,6,7,8])            #Syntax-> var_name.append([elements of list])
print("All items in the list after perform the extend Method=",c)

# 4) insert()- To add an iteam to the specified index we use the insert method 

d=[12,13,14,15]
d.insert(2,86)      #Syntax-> var_name.insert(index,element)
print("All items after perform the insert operation",d)

# 5) del()- the del keyword is used to delete a specified index value or it can also be delete the complete list

e=[13,23,33,44,55]
del(e[3])           #Syntax-> del(var_name[element])
print("All items after perform the del operation",e) 

# 6) remove()- this method is used to remove the specified iteam from the list

f=[66,77,88,99,00]
f.remove(77)        #Syntax-> var_name.remove(element)
print("All items After perform a remove Method=",e)

# 7) pop()- this method is used to remove the specified index value from the list or it will remove the last value if the index is not specified!

g=[33,44,55,66,77]
g.pop(2)                #Synatx-> var_name.pop(element)
print("list after perform pop method=",g)

g.pop()
print("List after removing last value=",g)

# 8) clear() this method is used to make an empty list

h=[22,44,66,00,99]
h.clear()           #Syntax-> var_name.clear()
print("Empty list=",h)

# 9) index()  This method finds the given element in a list and returns its index number
              #If the same element is present more than once, the method returns the index of the first occurrence of the element. 

i=[30,40,50,60,90]
print("Index of 40 element is",i.index(40))     #Syntax  print_statement(,var_name.index(element))

# 10) count() - This method counts how many times an element present in a list and returns it. 

j = [10,20,30,40,50,30,30] 
print("Count of 30 =", j.index(30)) #Synatx-> print_Statement(,var_name.index(ele))

# 11) sort() This method sorts the elements of a given list in a specific order - Ascending or Descending.

k = [10,20,30,40,50,30,30] 
k.sort()                         #Syntax-> var_name.sort()
print("Sort the element in Ascending order =", k) 

l = [10,20,30,40,50,30,30] 
l.sort(reverse=True) 
print("Sort the element in Descending order =", l) 

# 12) reverse()  This method is used to reverses the elements of given list.

m = [10,20,30,40,50] 
m.reverse()                  #Syntax-> var_name.reverse()
print("Reverse the list elements =", m) 

# 13) copy () This method is used to copy elements of one list into another list

n=[10,20,00,66,44]
o=n.copy()                     #Syntax-> var_name=list_var_name.copy()
print("Copied list Elements=",o)

# 14) min () this method is used to findout the minimum element in the list
p=[90,67,44,33,2]
print("Minimum element in the list=",min(p))        #Syntax-> print_Statement(,min(var_name))

# 15) max()  This method is used to find out the maximum element in the list. 
q = (10,20,30,40,50,30,30) 
print("Maximum element in the list=",max(q))        #Syntax-> print_Statement(,max(var_name))


