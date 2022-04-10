from threading import Thread

class MyThread(Thread):

    def run(self):

        for i in range(5):
            
            print("Child Thread ")


t = MyThread()
t.start()


for i in range(5):

    print("Main thread")

