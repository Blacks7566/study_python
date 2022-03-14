
# 3.default arguments
#---------------------------------
# at the time of calling if you forgott passing the vlaue but function didnot give error fuction give us proper output using his defalt arguments

def fun(course="C++"): # default parameters
    
    print("course is : ",course)


fun("python") # here supply value consider
fun() # here default value consider

print()


def fun1(name,course="C++"): # default parameters with non default parameters
    
    print(name,"course is : ",course)


fun1("nikki","python") # here supply value consider
fun1("nikki") # here we only pass name  default value consider

