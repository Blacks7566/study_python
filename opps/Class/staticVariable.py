# static variables:- 
# ----------------
# if the value of variable is not varied from object then such type of variables are called as static variables.

# for all objects only one copy of static variales will be create

# we can access static variables either by using object reference or class name

# the variable which is decalre outside of the method and inside of the class is called static variables


                              # Example :-




class Test:
    a=10 # this is static variable

    def __init__(self):

        self.b=52 # instance variable



t1=Test()

t2=Test()

print(t1.a,t1.b)
print(t2.a,t2.b)
print()
Test.a=100 # class level variables (static variable value change)

print(t1.a,t1.b)
print(t2.a,t2.b)
print()

t1.b=56
print(t1.a,t1.b)
print(t2.a,t2.b)





