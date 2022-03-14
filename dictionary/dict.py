# dict a is collection of items
# in dict each item contains key and value pair
# dict can be create by using {}
# in dict keys are immutable and must be unique
# to create a empty dict using by empty {}
# in dict key and vlaues can be any datatype

d ={1:"black",2:"go",'name':"Nitin",'age':23}

print(d)

print(d[1])

d["age"] = 24

print(d.get("name"))
print(d.get("age"))

# d["salary"] it will return key error

# print(d.get("salary")) if key is there it return value else none
print(type(d))



