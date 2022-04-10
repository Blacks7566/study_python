data = "welcome to black souls house"

f = open("rrr.txt",'w')

f.write(data)


with open("rrr.txt" ,'r+') as f:

    print("current cursor position : ",f.tell())
    text = f.read()
    print(text)
    print("current cursor position : ",f.tell())
    f.seek(15)
    print("current cursor position : ",f.tell())
    f.write("Nitin soni")
    f.seek(0)
    text= f.read()
    print("print data after modification")
    print(text)

    

