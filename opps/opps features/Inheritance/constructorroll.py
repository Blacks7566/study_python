# constructor Roll in inheritance

class A:

    def __init__(self):

        print("A class constructor")


class B:

    def __init__(self):

         print("B class constructor")


class C(A,B):
    
   ''' def __init__(self):

        print("C class constructor ")'''



c = C()



