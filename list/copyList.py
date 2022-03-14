
l = [1,2,3,4,5,6,7,8,9]

l1=l

print(l)
print(l1)

print()

# if we assign a vlaue in a list then it effect both of l and l1 

l[4] = 88

print(l)
print(l1)


l2=l.copy()
print()
print(l)
print(l2)

l[3]=54

print()
print(l)
print(l2)