from threading import *


def f1():

    print("child thread ")




t = Thread(target=f1)
t.start()

print("Main thread identification number : ",current_thread().ident)
print("Child thread identification number : ",t.ident)