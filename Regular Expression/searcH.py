import re

s = input("Enter pattern to cheack : ")


m = re.search(s,"blackSoul")

if m!= None:

    print("search present")

else:

    print("Search not present ")
