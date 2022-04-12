

def decor(f1):

    def inner(name):

        if name=="blacks":

            print("Pranaam Guru")
        else:

            f1(name)
    
    return inner
        




# decofunction = decor()



@decor
def f1(name):

    print("Hello",name,"Good morning")





f1("nitin")
f1("blacks")

# decofuntion("blacks")