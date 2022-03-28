# constructor Roll in inheritance

class A:

    def __init__(self):

        print("A class constructor")


class B(A):

    ''' def __init__(self):

         print("B class constructor") '''


class C(B):
    
   ''' def __init__(self):

        print("C class constructor ")'''



c = C()



