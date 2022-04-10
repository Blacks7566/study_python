from threading import *
import time
import random
import queue




def producer(q):

    while True:

        item= random.randint(1,100)
        print("Producer producing item : ",item)
        q.put(item)
        print("Producer giving notification")
        time.sleep(5)


def comsumer(q):

    while True:

        print("Consumer waiting for updation")
        print("Consumer consumed the item : ",q.get())

        time.sleep(5)



q = queue.Queue()

t1 =Thread(target=producer,args=(q,))
t2 =Thread(target=comsumer,args=(q,))

t1.start()
t2.start()