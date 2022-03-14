#1. filter (): is used to filter the vlaues from given sequence based on condition

# syntax : filter(fucntion,sequence)

# here first parameter is a function for condtional check
# here second parameter is a sequence (list,tuple,set)


def iseven(x):
    if x%2==0:
        return True
    else:
        return False
    



l = [1,2,3,4,5,6,7,8,9,10]
print("This l list ",l)

l2 =list(filter(iseven,l))

print("This l2 list ",l2)

# using labmda

l3 = list(filter(lambda n : n%2==0 ,l))
print("This l3 list ",l3)
