# creating list form user input values


l=[]


# item1=int(input("Enter integer value:"))
# item2=input("Enter string value:")
# item3=float(input("Enter float value:"))

# l.append(item1)
# l.append(item2)
# l.append(item3)

# print(l)

n = int(input("Enter the length of list : "))


for i in range(n):

    x = int(input("Enter the value : "))
    l.append(x)

print(l)
print()

print("creating list using range fuction")

print()

print(list(range(2,10,2))) # start, stop, step: