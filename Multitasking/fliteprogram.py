from threading import Thread , current_thread
from zoneinfo import available_timezones


class Flight:

    def __init__(self,available_seat):

        self.available_seat = available_seat

    def reserve(self,need_seat):

        print("Available Seats : ",self.available_seat)

        if (self.available_seat >= need_seat):

            name = current_thread().name

            print(f'{need_seat} seat is alloted for {name}')

            self.available_seat -=need_seat
        
        else:

            print('Sorry! All seats has alloted')




av = int(input("Enter total availabel seats : "))


p = Flight(av)

t1 = Thread(target=p.reserve , args=(1,), name="Nitin")
t2 = Thread(target=p.reserve , args=(1,), name="Blacks")

t1.start()
t2.start()







