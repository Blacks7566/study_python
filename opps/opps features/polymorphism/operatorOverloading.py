class Book:

    def __init__(self,pages):

        self.pages=pages

    
    def __add__(self,other):  # this is magic fucntions to add objects 


        return self.pages+other.pages





b1 = Book(100)
b2 = Book(200)


# print(b1+b2) # we can not add to object with out adding magic functions

print(b1+b2)