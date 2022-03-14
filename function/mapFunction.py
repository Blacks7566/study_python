#2. map() : for every element present in sequence, apply some condition and return the new sequence of elements for this purpose we use map() function.

# map(function,sequence) 


from math import log1p


def dbl(x):
    return x*x


l=[2,3,4,5,6,7,8,9,10]

print("This is list l : ",l)

l1=list(map(dbl,l))
print("This is list l1 : ",l1)

# we can also use lambda

l2=list(map(lambda x : x*x,l))

print("This is list l2 : ",l2)
