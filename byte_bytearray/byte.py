# bytes -- represents byte numbers 0 upto 256 bytes is immutable , that can not be modify

# bytearray-- represents byte numbers 0 upto 256 bytes is mutable , that can be modify

# bytes bytearray can be create interger numbers only


x =[10,20,30,40] 

print(x)
print(type(x))

b = bytes(x) #converting list to bytes and bytes must be in range (0,256)


print(b)
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(type(b))

b[2]=66

print(b[2]) # bytes are immutable 