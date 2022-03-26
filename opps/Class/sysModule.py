# how to find the no of references of an object
#----------------------------------------------

# sys module contains getrefcount()

#sys.getrefcount(objectrefeerence)

import sys

class Test:
    pass



t1=Test()

t2=t1
t3=t1
t4=t1

print(sys.getrefcount(t1))