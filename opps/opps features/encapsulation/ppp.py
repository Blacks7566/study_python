

class Test:

    x = 100 # public
    _y = 200 # protected
    __z = 300 # private

    def __init__(self) -> None:
        print("whithin the class")
        print(self.x)
        print(self._y)
        print(self.__z)


t = Test()

print()
print("Out side of the class")
print(t.x)
print(t._y)
# print(t.__z) we can not access private variable out side of the class


