
import re

l = re.sub("[a-z]","*","165sfh*$#hlh*")
ln = re.subn("[a-z]","*","165sfh*$#hlh*")

print("sub() return : ",l)
print("subn() return : ",ln)