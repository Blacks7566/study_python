

class Parent:

    def property(self):

        print("Cash+Gold+Lands")
    
    def car(self):

        print("Alto")


class Child(Parent):

    def car(self):

        super().car()  # it call Parents car method

        print("Audi CAR")




c = Child()

c.property()
c.car()

