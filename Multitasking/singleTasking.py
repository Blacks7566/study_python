
from threading import Thread
import time



class MyExam:

    def solve_question(self):

        self.q1()
        self.q2()
        self.q3()
    
    def q1(self):
        print("Question 1 sloved ")
        time.sleep(3)

    def q2(self):
        print("Question 2 sloved ")
        time.sleep(3)

    def q3(self):
        print("Question 3 sloved ")
        time.sleep(3)


ex = MyExam()

t = Thread(target=ex.solve_question)
t.start()