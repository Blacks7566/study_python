import re

s = input("Enter pattern to cheack : ")


m = re.fullmatch(s,"blackSoul")

if m!= None:

    print("fully match is available at the begining of traget string")

else:

    print("fully match is not available at the begining of traget string")
