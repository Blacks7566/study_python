# isinstance():

# isinstance method to used to check whether the object is an instance of particular class or not


# issubclass():

# is used to check whether the class is a sub class of particular class or not






class Parent:

    def f1(self):

        print("F1 fucntion of parent class")


class Child1(Parent):

    def f2(self):
        print("F2 function of Child1 class")


class Child2(Parent):

    def f3(self):
        print("F3 function of Child2 class")


c1 = Child1()
c2 = Child2()


print("isinstance()")
print()


print(isinstance(c1,Child1)) # is the object of 
print(isinstance(c1,Child2))

print(isinstance(c2,Child1))
print(isinstance(c2,Child2))
print()

print("issubclass()")
print()

print(issubclass(Child2,Parent))
print(issubclass(Child1,Parent))
print(issubclass(Child1,Child2))