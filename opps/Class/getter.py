class Employee:

    def setData(self):
        print("Enter employee details ")
        print()
        self.name = input("Enter employee name : ")
        self.id   = input("Enter employee id : ")
        self.mob   = input("Enter employee moble : ")
        self.address   = input("Enter employee address : ")
        self.salary   = input("Enter employee salary : ")
    
    def getData(self):
        print()


        print("Employee id  is : ",self.id)
        print("Employee name is : ",self.name)
        print("Employee address : ",self.address)
        print("Employee mobile no is  : ",self.mob)
        print("Employee salary is  : ",self.salary)


emp1 = Employee()
 
emp1.setData()
emp1.getData()