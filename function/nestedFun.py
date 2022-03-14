# nested function:
# a function  which is having one or more function within it is called nested function


def f1():
    print("hello")


    def f2():
        print("hey")


        def f3():
            print("Go to hell i am f3() ")
    
        f3() # here calling function f3()

    f2() # here calling function f2()



f1()


