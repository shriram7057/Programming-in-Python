"""
    1 
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""
import math
n = 5

for i in range (n):
    for j in range(n-i-1):

        print(" ",end="")
    for j in range(i+1):
        print(str(math.comb(i,j))+ " ",end= "")
    print()
