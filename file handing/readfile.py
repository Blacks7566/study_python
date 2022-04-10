f = open("sample.txt","r")

print(f.read())



print()
print("we try to access file who's does not exist")
print()


try:

    t = open("new.txt","r")
    data = t.read()
    print(data)

except FileNotFoundError as mas:

    print(mas)

