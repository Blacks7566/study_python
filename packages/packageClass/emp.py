

class Employee():

    def __init__(self):

        self.ename = input("Enter Employee name : ")
        self.eid = int(input("Enter Employee Id : "))
        self.esalary = int(input("Enter Employee salary : "))
        self.eaddre = input("Enter Employee address : ")

    

    def display(self):

        print("Employee id is : ",self.eid) 
        print("Employee name is : ",self.ename) 
        print("Employee salary is : ",self.esalary) 
        print("Employee address is : ",self.eaddre) 

