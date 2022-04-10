from threading import *
import time


def display ():


    for i in range(10):

        print("Child Thread")

        time.sleep(2)


t = Thread(target=display)
t.start()

t.join()


for i in range(10):
    print("Main Thread")