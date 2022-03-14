def add(a,b):
    print(a+b)




add(10,20) # positional arguments
add(a=10,b=20) # keyword arguments

# here we can do both method to call function


def add1(a,b,/): # using / this function cal take only positonal argumets
    print(a+b)


add1(10,30) # we can use  only position arguments

#add1(a=10,b=50) we can not call fucntion like this 



def add2(*,a,b): #using * function acept only keyword argumets
    print(a+b)


add2(a=12,b=9)
# add2(2,9) we can not do this




   