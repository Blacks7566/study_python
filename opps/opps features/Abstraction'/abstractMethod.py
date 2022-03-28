

from abc import abstractmethod


from abc import ABC,abstractmethod




class Vehicle(ABC):


    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def color(self):
        pass

    def engin(self):
        print("Bs6 engin.")


class Car(Vehicle):
 
    def wheels(self):  # we have to include abstract  method

        print("Car have 4 wheel")

    def color(self): 

        print("car color is black")

class Bike(Vehicle):

    def wheels(self): 

        print("Bike have 2 wheel")

    def color(self): 

        print("Bike color is blue")

# v = Vehicle() we can not create object of abstract clss


c= Car()
b = Bike()

c.wheels()
c.color()
c.engin()
b.wheels()
b.color()
b.engin()
