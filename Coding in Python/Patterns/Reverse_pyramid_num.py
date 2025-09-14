"""   
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
"""
for i in range(5,0,-1):
    print(" "*(5-i)+" ".join(str(x) for x in range(1,i+1)))