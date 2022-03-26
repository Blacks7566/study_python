# inner class :
#----------------

# sometime we can declare a class inside the other class is called inner class

# a class within a class



# class Car:
    
     
#      class Engin:




class Outer:

    def __init__(self):

        print("Outer class constuctor")

    class Inner:

        def __init__(self):

            print("inner class constuctor")
        

        def m1(self):
            print("inner class method")



# obj = Outer()

# inn = obj.Inner()  # here create object for inner class


i = Outer().Inner() # we also do this

# and direct we can do 


print()

Outer().Inner().m1()