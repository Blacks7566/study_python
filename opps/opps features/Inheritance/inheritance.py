 # Implementing Inheritance
 #--------------------------



class Branch:

    def get_branch_data(self):

        self.bcode=int(input("Enter branch code : "))
        self.bname=input("Enter branch name : ")
        self.baddress = input("Enter branch adddress : ")
    

    def display_branch_data(self):

        print("Branch code is : ",self.bcode)
        print("Branch Name is : ",self.bname)
        print("Branch Address is : ",self.baddress)



class Employee(Branch): # Branch class inherited by Employee class

    def get_emp_data(self):

        self.eid = int(input("Enter employee id : "))
        self.ename = input("Enter employee name : ")
        self.eaddress = input("Enter employee address : ")

    
    def display_emp_data(self):

        print("Employee id is : ",self.eid)
        print("Employee Name is : ",self.ename)
        print("Employee Address is : ",self.eaddress)


em1 = Employee()


em1.get_branch_data()
em1.get_emp_data()

print()

em1.display_branch_data()
em1.display_emp_data()