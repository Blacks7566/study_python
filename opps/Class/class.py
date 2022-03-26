


class Student:
    
    def __init__(self): # constractor in python programming is allways __name__
        self.sid=123
        self.name="nikki"
        self.address="Rewa"
    

    def displayData(self):

        print("Student id is : ",self.sid)
        print("Student name is : ",self.name)
        print("Student address is : ",self.address)


    


s=Student() # creating instance of class

s.displayData()



"""


Constructor:
----------

1. constructor is a special method of class.
2. constructor is used to declare the variables an intialize the values to variables

3. in python constructor name should be __init__(self)
4. self is a special variable and it is the first parameter of constructor
5. using self we can access current class members
6. constructor will execute automatically when we create object to class.
7. we can create any no of object to the class
8. for every object constructor will execute once.


method :
---------
1. mehtod is a reusable piece of code which can be call again and again when it is required
2. inside the method we can any business lagic code.
3. method name can be of any valid name
4. self is a spwcial variable and it is the first parameter of method
5. method will excute only when we call method
6. for every object we can call method many  times

"""