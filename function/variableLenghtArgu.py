

# 4. variable length arguments
#-------------------------------
#   def f1(*n):
#      code..

# what is *args and **kwargs ?

# *args allows us to pass no of values to the fuction
# *args will store all no of values is th form of tuple

# **kwargs allow us to pass numbers of keyword arguments
# it store allow number of keyword arguments in the form of disct




def f1(*n):
    print(n)


f1()
f1(5,2)
f1(6,2,3)
f1(12.2,32.0,56,8)
f1(452,45)


def add(*args):

    s=0

    for i in args:
        s=s+1

    print("Sum is :",s)    

print()

add(12,35)
add(12,35,56,7)
add(12,35,56,7,89)
add(12,35,56,7,89,8)


print()

def fun(**kwargs):

    for k ,v in kwargs.items():  # here k for key and v = values
        print(k," = ",v)
    

fun(eid=1001,ename="blacks",eaddress="rewa")
