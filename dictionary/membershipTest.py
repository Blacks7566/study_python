# membership apply on keys of dict not vlaue of dict

d = {'id':1,'name':"blacksoul",'age':23,'address':"Rewa",'salary':5678}


print(d)
print("name" in d)

print("length of d ", len(d))

# pop method used to delet one perticular key vlaue paire  and it return the deleted value
# popitem is used to delet last item 

d.pop("salary")
print(d)

d.popitem() # and its return deleted key value both
print(d)
