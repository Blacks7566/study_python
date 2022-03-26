

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

c1.f1()
c2.f1()
c1.f2()
c2.f3()