
from threading import Thread

class Mythread:

    def disp(self, a,b):
        print(a,b)
    



t = Mythread()

t = Thread(target=t.disp,args=(20,30))

t. start()