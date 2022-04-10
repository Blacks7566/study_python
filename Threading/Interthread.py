from threading import *

import time
from tkinter import EventType

def producer():

    time.sleep(5)

    print("Producer thread producing items")
    print("Producer thread giving notification by setting event")

    event.set()


def consumer():
    print(" Consumer thread is waiting for undation ")
    event.wait()

    print("Consumer thread got notification and consuming items")




event = Event()

t1=Thread(target=producer)
t2=Thread(target=consumer)

t1.start()
t2.start()