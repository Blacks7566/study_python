# Locla variables (method level):-
# -------------------------------

# The variable which is declare inside a particular method and that   variable is only to that method is called local or method level variables.


# local variable can not access outside of the methods

# these variables are also called as temporary variables.

# as soon as method execution starts then these variable will be create one 
# method execution completes then these will be distroy



class Test:

    def m1(self):

        self.a=10 # instance variable

        
        b=20      # this is local variable

        print(b)

    
    def m2(self):
        print(self.a)

        # print(b) we can not access  local variables


t = Test()


t.m1()
t.m2()