class Student:
    
    def __init__(self,id,name,address): # constractor in python programming is allways __name__
        self.sid=id
        self.name=name
        self.address=address
    

    def displayData(self):

        print("Student id is : ",self.sid)
        print("Student name is : ",self.name)
        print("Student address is : ",self.address)
    



s1=Student(101,"nitin","rewa")
s2=Student(102,"Ashis","rewa")
s1.displayData()
print()
s2.displayData()