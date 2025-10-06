"""
FOR DESIGNING A HOLLOW SQUARE PATTERN WE USED THE TWO FOR LOOPS AND IF ELSE STAEMENT ALSO
*********
*       *
*       *
*       *
*       *
*       *
*       *
*       *
********* 
"""
b = 9 #Global variable Declaration 

for i in range(b):
    for j in range(b):
        if i == 0 or i == b-1 or j == 0 or j == b-1 :
            print("*",end="")
        else:
            print(" ",end="")
    print()

n = 3
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 :
            print("*",end="")
        else:
            print(" ",end="")
    print()