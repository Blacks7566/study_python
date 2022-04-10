
import re


mob = input("Enter mobile number : ")

m = re.fullmatch("[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",mob)


if m!=None:
    print("Valid mobile number")

else:

    print("Invalid mobile number")