# positional arguments : arguments which are passed to a function in correct positional order is called positonal argument
#                        if we change th order or position then result may change
#                        if we increse or decrease the arguments then we will get error

def sub(a,b):

    print(a-b)


sub(20,10)
sub(10,20) # we change the position of arguments
sub(10,20,4) # we increse the arguments we get error
sub(10) # we decrece the arguments we get error
