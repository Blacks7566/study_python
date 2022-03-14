
# Type of variables:

# 1. Local variables 
#     The variables which are declare inside the functions and that are available to 
#     only that particular fuction in called local variables
#  
#     Locla variales can not access outside of the funtions
# 
# 2. Global variables 
#    The variales which are declare outside the functions and that are available to 
#    all functions in the program is called global variable
#   
#     Global variables can access out side of the function 


def f1():
    a=10  # local variable declare

    print(a)

def f2():
    b=50  # local variable declare

    print(b)


f1()
f2()


# pirnt(a) we can not acces the local  variable out side of the function


