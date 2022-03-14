# reduce(function,sequence)
# it return interger value like single value
# we have to import functools

from functools import reduce







def add(x,y):
    return x+y


l=[1,2,3,4,5,6,7,8,9,10]

result = reduce(add,l)

print(result)


# using lambda

result2=reduce(lambda x,y:x+y,l)

print("This is result 2 : ",result2)




