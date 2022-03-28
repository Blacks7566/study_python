class A:

    def f1(Self):
        print("F1 fucntion of Class A")


class B:

    def f2(self):

        print("F2 function of class B")


class C(A,B):

    def f3(self):

        print("F3 function of class C")


class D(C):


    def f4(self):

        print("F4 function of class D")


d = D()

d.f1()
d.f2()
d.f3()
d.f4()