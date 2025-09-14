"""
    1
   2 2
  3   3
 4     4
5       5
"""
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,2*i):
        if j == 1 or j == 2*i-1:
            print(i,end="")
        else:
            print(" ",end="")
    print()