import re



n = input("Enter mail id: ")


m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",n)

if m!=None:
    print("Valid Mail id ")

else:

    print("Invalid Mail id")