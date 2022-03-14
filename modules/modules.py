# modules in python
#------------------------------
# in python every .py file act as module

# module is for reusability of entire the program code

#1. user defined modules
#2. builtin modules


# import module1 
# import module1 sd m1 
# import module1 ,module2
# from module1 import *
# from module1 import member1
# from module1 import member1 as m1
# from module1 import member1,member2
# from module1 import member1 as m1,member2 as m2


























import sample
import sample1


print(sample.a)

sample.add(10,15)
sample.sub(102,67)


print()
import sample as s # module aliasing

s.add(15,96)
s.sub(205,86)
print(s.a)

print()

from sample import *  # import all of the member form sample.py

print(a)
add(86,21)
sub(56,32)

print()

from sample import sub, a as b # we can member aliasing

sub(89,5)

print(b)

print()

print(sample1.a)

sample1.mul(12,3)
sample1.div(12,3)