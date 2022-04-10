from threading import *

import time

class Flight:

    def __init__(self,available_seat):

        self.available_seat = available_seat
        self.l = Lock()


    
    def reserve(self , need_seat):

        self.l.acquire()

        print('Available seats : ',self.available_seat)
        if(self.available_seat >= need_seat):

            name = current_thread().name
            print(f'{self.available_seat} seat is alloted for {name}')

            self.available_seat -= need_seat
            time.sleep(4)

        else:
            print("Sorry! All seats has alloted ")

        self.l.release()


f = Flight(2)


t1 = Thread(target=f.reserve, args=(1,), name='Nitin')

t2 = Thread(target= f.reserve, args=(1,) , name = 'Black')
t3 = Thread(target= f.reserve, args=(1,) , name = 'sudeep')

t1.start()
t2.start()
t3.start()