# Function aliasing:

# giving other name to a function is called function aliasing


def f1():
    print("This is my function")



f = f1 # here we asign f1() into the f

del f1

f() # we can function