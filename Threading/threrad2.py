from threading import *

import time


def f1():

    print(current_thread().getName(),".....started")
    time.sleep(3)
    print(current_thread().getName(),".....ended")




print("The no of active threads : ",active_count())


print()

t1 =Thread(target=f1, name="ChildThread1")
t2 =Thread(target=f1, name="ChildThread2")
t3 =Thread(target=f1, name="ChildThread3")
t4 =Thread(target=f1, name="ChildThread4")
t5 =Thread(target=f1, name="ChildThread5")
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print("The no of active threads : ",active_count())

time.sleep(5)

print("The no of active threads : ",active_count())
