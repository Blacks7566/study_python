import re



n = input("Enter mail id: ")


m = re.fullmatch("\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",n)

if m!=None:
    print("Valid Mail id ")

else:

    print("Invalid Mail id")