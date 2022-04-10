from threading import Thread , current_thread

def display():
    print(" Default Child Thread name :",current_thread().getName())

    current_thread().setName("Black Thread")

    print(" New Child Thread name :",current_thread().getName())



t = Thread(target=display)
t1 = Thread(target=display)

t.start()
print()
t1.start()

print("Main thread name :  ",current_thread().getName())

current_thread().setName("Nitin")

print(" New Main thread name :  ",current_thread().getName())



