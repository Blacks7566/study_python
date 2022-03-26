

class Test:

    a = 100 # static variable

    def __init__(self):

        print("Inside the constructor")
        print(self.a)
        print(Test.a)
    

    def m1(self):

        print("Inside the instance method")
        print(self.a)
        print(Test.a)

    
    @classmethod

    def m2(cls):

        print("Inside the class method")
        print(cls.a)
        print(Test.a)




t=Test()

print("outside of the  class")
print(t.a)

t.m1()
t.m2()
print()
print("we can delete static variables any where ")