d = {'id':1,'name':"blacksoul",'age':23,'address':"Rewa",'salary':5678}

d1 =d

print(d)
print(d1)

print()
print("After udate the value in d ")
print()

d['id'] = 3
print(d)
print(d1)


d2 =d.copy()

print()
print("After udate the value in d ")
print()

d['id'] = 5
print(d)
print(d2)


