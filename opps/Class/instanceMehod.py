class Student:

    def __init__(self,m1,m2,m3):

        self.m1=m1
        self.m2=m2
        self.m3=m3

    
    def avg(self):   # this is instance method
        return (self.m1+self.m2+self.m3)/3



s1 = Student(10,45,23)

print(s1.avg())