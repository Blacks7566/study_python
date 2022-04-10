class ToooldException(Exception):

    def __init__(self,arg):

        self.msg = arg


class TooyoungException(Exception):

    def __init__(self,arg):

        self.msg = arg
try:

    age = int(input("Enter your age "))


    if age>60:
        raise ToooldException("Age should not exceed 60")

    elif age < 16:
        raise TooyoungException("Age should not under 16")

    else:
        print("You are eligible to take policy")

except (ToooldException,TooyoungException ,ValueError) as msg:

    print(msg)


# we also do this in the place of (ToooldException,TooyoungException ,ValueError) =  except: Exception as mag :