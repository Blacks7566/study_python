
from array import *

A= array('i',[])


l = int(input("Enter lenght of array : "))


for i in range(l):

    x=int(input("Enter element : "))

    A.append(x)

print(A)

s = int(input("Enter the array element for search : "))
print("element present at index : ",A.index(s))

# we use all the fucntion of list 