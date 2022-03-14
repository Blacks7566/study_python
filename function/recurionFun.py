# recurion is mechanism

# a function that calls every time itsef is called recurion funtion


# factorial(n) = n*factoial(n-1)



# factorial(3) = 3*factorial(2)
#              = 3*2*factorial(1)
#              = 3*2*1*factorial(0)
#              = 3*factorial(2)
#              = 3*2*1*1
#              = 6


from math import factorial


def fact(n):
    if n==0:
        result=1
    else:
        result = n*fact(n-1)
    return result

n = int(input("Enter a number to find factorial : "))

print("Factorial of ",n," is :",fact(n))

import math



print(math.factorial(10)) # we can aslo use math module 