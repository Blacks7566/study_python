from threading import *


import time
from unicodedata import name

def f1():

    print(current_thread().getName(),".....strated")
    time.sleep(3)

    print(current_thread().getName(),".....ended")


print("The number of active thread is : ",active_count())


t1 = Thread(target=f1,name="ChildThread1")
t2 = Thread(target=f1,name="ChildThread2")
t3 = Thread(target=f1,name="ChildThread3")

t1.start()
t2.start()
t3.start()
print("The number of active thread is : ",active_count())
time.sleep(5)
print("The number of active thread is : ",active_count())
