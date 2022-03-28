class A:

    def f1(Self):
        print("F1 fucntion of Class A")


class B:

    def f2(self):

        print("F2 function of class B")


class C(A,B):

    def f3(self):

        print("F3 function of class C")



c = C()


c.f1()
c.f2()
c.f3()


# it follow MRO (Method Resolution Order)