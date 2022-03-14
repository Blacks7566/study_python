# 

A = {1,2,3,4,5,6}

B = {4,5,6,7,8,9}

print("A : ",A)
print("B : ",B)
print()

print("A union B : ",A|B) # A U B 
print("A union B : ",A.union(B)) # A U B 
print()



print("A intersecion B",A.intersection(B))


print()

print("A diffrence B : ",A-B)
print("A diffrence B : ",A.difference(B))

print()

print("A Semetric differnce B : ",A^B)
print("A Semetric differnce B : ",A.symmetric_difference(B)) # 