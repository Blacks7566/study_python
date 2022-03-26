from numpy import *


A = array([[10,20,30,40,50],
           [60,70,80,85,95],
           [56,75,84,96,32]])


print(A)

print()
# if i want to acesse the value 80 then the index is 

print(A[1][2])

print("max vlaue : ",A.max())
print("min vlaue : ",A.min())
print()

print("row wise max value :",A.max(axis=1))
print("row wise min value :",A.max(axis=1))

# axis 1 represent row
# axis 0 represent colom

print("colom wise max value :",A.max(axis=0))
print("colom wise min value :",A.max(axis=0))


# A.flatten() method marge in one dimention all dimention