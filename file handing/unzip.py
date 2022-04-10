from zipfile import *

f = ZipFile("files.zip",'r',ZIP_STORED)

names = f.namelist()

print(names)

for name in names :

    print("The file name is : ",name)
    f=open(name,"r")
    print()
    data = f.read()
    print("content of file ")
    print(data)