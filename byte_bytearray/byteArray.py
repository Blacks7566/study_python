x =[10,20,30,40] 

print(x)
print(type(x))
b = bytearray(x) #converting list to bytearray and bytes must be in range (0,256)


print(b)

for i in b:
    print(i)

print(type(b))

b[2]=66 # bytes are mutable

print(b[2]) 