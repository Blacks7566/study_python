# keyword arguments : The arguments which are passed to a function by using keyword or parameters is called keywoed arguments
#                     While working with keyword arguments the order or posistion is not important but keywords or paramenters name are important
#                     we can also use one keyword arguments and one positonal args but make sure that first we have to mention positional args and then agter keyword arguments

def f1(name,msg):

    print("Hello",name,msg)


f1(name="Blacks",msg="Where are you")
f1(msg="Where are you",name="Blacks") # we can change the position but output are not change

# positional args

f1("mohan","goodmoring")
f1("goodmoring","mohan") # out put change 

# one positional and one keyword arguments

f1("Nitin",msg="go to hell")
# f1(name="Nitin","go to hell")             # this will not allow we first mention positionl arguments