# function return multiple value

def opp(a,b):

    sum = a+b
    sub = a-b

    return sum,sub



x,y = opp(50,36)

print("Sum is : ",x)
print("Sub is : ",y)


# but this is not good practice 
# good practice is to sperate the functions 


