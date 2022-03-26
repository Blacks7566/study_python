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


class Empsalary(Employee):

    def get_sal(self):
        self.bacis=int(input("Enter basic salary : "))

    def calculate(self):

        self.DA = self.bacis*0.5
        self.HRA = self.bacis*0.10

        self.Gross=self.bacis+self.DA+self.HRA

    def display_sal(self):

        print("Basic salary is : ",self.bacis)
        print("DA is : ",self.DA)
        print("HRA is : ",self.HRA)
        print("Gross is : ",self.Gross)
    




sl = Empsalary()


sl.get_branch_data()
sl.get_emp_data()
sl.get_sal()

sl.calculate()


print()

sl.display_branch_data()
sl.display_emp_data()
sl.display_sal()



