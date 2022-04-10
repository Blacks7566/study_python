import re

s = input("Enter pattern to cheack : ")


m = re.match(s,"blackSoul")

if m!= None:

    print("match is available at the begining of traget string")

else:

    print("match is not available at the begining of traget string")
