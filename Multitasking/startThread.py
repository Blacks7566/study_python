

from  threading import Thread

def disp():


    for i in range(5):
        print("Child Running ")


t = Thread(target=disp) # args = only tuple

t.start()

print()

for i in range(5):

    print("Main Thread")
