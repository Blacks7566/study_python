from threading import *

import time

def trafficpolice():

    while True:

        time.sleep(10)
        print("Traffic police giving green signal")
        event.set()

        time.sleep(20)
        print("Traffic police giving RED signals")

        event.clear()
    

def driver():

    num = 0

    while True:

        print("Drivers are waiting for GREEN signal")
        event.wait()
        print("Traffic signal is GREEN ... Vechicles can move")

        while event.is_set():
            num = num+1

            print("Vehicle no : ",num,"Crossing the signal")
            time.sleep(2)
            print("Traffic signal is RED .. Drivers need to wait ")



event = Event()

t1 =Thread(target=trafficpolice)
t2 =Thread(target=driver)
t1.start()
t2.start()