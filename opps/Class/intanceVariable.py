class Test:
    def __init__(self):
        self.a=10 # this is instance variable in constructor
        self.d=65 
        self.f=15  

    
    def m1(self):
        self.b=23 # this is instance variable in method

        print(self.a)
        print(self.d)
        print(self.f)




t =Test()

t.c=30  # this is also instance variables out side of class



print(t.__dict__)


print(t.d) # to access the instance varialbe access by out side the class


# deleting instance variables


del t.c 



