from socketserver import ThreadingTCPServer
from threading import *

import time


def consume(c):

    c.acquire()
    print("Consumer waiting fo updation")
    c.wait()
    print("consumer got notification and consuming the itme ")
    c.release()




def producer(c):

    c.acquire()

    print("Producer producing item")
    print("Producer giving notification ")
    c.notify()
    c.release()




c = Condition()

t1 = Thread(target=consume, args=(c,))
t2 = Thread(target=producer, args=(c,))
t1.start()
t2.start()