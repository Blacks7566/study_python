from threading import Thread , current_thread



def disp():

    print("Default Child Thread name : ",current_thread().name)

    current_thread().name = "New Child Thread"

    print("new Child Thread name : ",current_thread().name)



t = Thread(target=disp)

t.start()


print("Default main Thread name : ",current_thread().name)

current_thread().name = "New main thread"

print("New main Thread name : ",current_thread().name)

