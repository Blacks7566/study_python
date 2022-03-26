

class Car:

    __name = "" #  private variable

    __maxspeed = 0 # private variable

    def __init__(self):

        self.__name="Swift"
        self.__maxspeed=150

        print(self.__name)
        print(self.__maxspeed)


    def drive(self):

        print("Driving")


        self.__maxspeed = 200
        print(self.__maxspeed,"/kmph")



    



c = Car()


# c.__maxspeed=250  We can not change the private variable value (This is encapsulation)

c.drive()