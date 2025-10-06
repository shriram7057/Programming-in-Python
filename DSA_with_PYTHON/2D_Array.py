print("Accessing Values using 2D array")
print()
from array import *
T=[[11,12,5,2],[15,6,10],[10,8,12,2],[12,15,8,6]]
print(T[0])
print(T[1][0])
print()

print("all 2D array using loop")

from array import *
S=[[11,12,5,2],[15,6,10],[10,8,12,2],[12,15,8,6]]
for i in S:
    for j in i:
        print(j,end=" ")
    print()
print()
print("Inserting Values")

from array import *

T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

T.insert(2, [0, 5, 11, 13, 6])

for r in T:
    for c in r:
        print(c, end=" ")
    print()
print()
print("Updating Values")

from array import *

T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

T[2] = [11, 9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c, end=" ")
    print()