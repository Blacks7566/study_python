f = open("sample.txt","r")

print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(5))
print(f.tell())
f.seek(15)

print(f.tell())
