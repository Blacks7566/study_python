
class Student():

    def __init__(self):

        self.sid = int(input("Enter student id : "))
        self.sname = input("Enter student name : ")
        self.saddre = input("Enter student address : ")
    
    def stData(self):

        print("Student id is : ",self.sid)
        print("Student name is : ",self.sname)
        print("Student address is : ",self.saddre)