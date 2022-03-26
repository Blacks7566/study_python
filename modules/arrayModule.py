# array index starts with 0 and ends with size-1
#      0  1  2  3
#     -4  -3 -2 -1         
# A = [10,20,30,40]

# 1. single dimension array : an array which contain only one row and one column is 

#10
#20
#30
#40

# 2. two dimension array: an array which contain more than one row and more than one column
 
# 10 20 30
# 40 50 60
# 60 70 80



# import array as arr

from array import *


A = array('i',[10,20,30,40,45,65,21])


# type code i = interger
# type code u = unicode
# type code f = float

print(A)

print(type(A))
print(A.typecode)

print(A[0])


for i in range(len(A)):
    print(A[i])



B = array('i',[i*2 for i in A]) # copy elements in B with the mul 2 of the vlaues

print(B)