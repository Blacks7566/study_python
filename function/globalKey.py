# global keyword : is used to make the global variable available to a particular function for required modification



def f1():

    global a # we also declare global function inside of the function
    a = 88

    print(a)  # access the global variable 


def f2():

    a = 75

    print(globals()['a']) # access the global variable  becaues local and global variables name are same



f1()
f2()


# here local vaiables get first 










