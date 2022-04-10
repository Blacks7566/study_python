import re



s = "Learning python is very easy"

m = re.search("^Learn",s)

e = re.search("easy$",s)


if m!=None:

    print("Target string starts with Learn")

else:

    print("Target string not starts with Learn")


if e!=None:

    print("Target string ends with easy")

else:

    print("Target string not ends with easy")