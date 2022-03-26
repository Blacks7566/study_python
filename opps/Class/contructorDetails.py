class Student:
    
    def __init__(self,id,name,address): # constractor in python programming is allways __name__
        self.sid=id
        self.name=name
        self.address=address

        # this is not good practice  




st1 = Student(1,"nikki","rewa")
st2 = Student(2,"ashish","satna")
st3 = Student(3,"Golu","sidhi")


print(st1.__dict__)  # to print constructor data
print(st2.__dict__)
print(st3.__dict__)


# to get class information


print(st1.__doc__)
print(help(Student))