from threading import *


def f1():

    print("child Thread")



t = Thread(target=f1)

t.start()


print("main thread identification number : ",current_thread().ident)
print("child thread identification number : ",t.ident)