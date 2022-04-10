






# a = int(input("Enter num1 : "))
# b = int(input("Enter num2 : "))


# if b==0:
#     print("Secound num can not be zero")

# else:
#     c = a/b

#     print("result is : ",c)


try:
     a = int(input("Enter num1 : "))
     b = int(input("Enter num2 : "))
     c = a/b
     print("Result : ",c)


# except Exception as error:
#     print(error)


# but uses of super class is not good practic in realty because super class cheack all sub class

except ZeroDivisionError as msg:

    print(msg)

except:
    print("Something went worng")