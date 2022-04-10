from threading import Thread

def disp():
    pass


t = Thread(target=disp)

print("Default : ",t.name)

t.name = "Playing "

print("New name  is : ",t.name)

t2 = Thread(target=disp,name = "going")

t2.start()

print("t2 thread name is ",t2.name)