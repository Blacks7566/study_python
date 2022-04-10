from threading import *
import time


def display (name):


    for i in range(10):

        print("Good morning : ",end="")

        time.sleep(2)
        print(name)


t1 = Thread(target=display,args=("nitin",))

t2 = Thread(target=display,args=("blacks",))

t1.start()
t2.start()



