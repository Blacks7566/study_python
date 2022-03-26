

class Parent:

    x = 100 # public
    _y = 200 # protected
    __z = 300 # private


class Child(Parent):

    print(Parent.x)
    print(Parent._y)
    # print(Parent.__z) we can not access private variables


c = Child()