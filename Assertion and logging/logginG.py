import logging

logging.basicConfig(filename='log.txt',level=logging.INFO)

logging.info('A new request came')



try:

    x = int(input("Enter number 1 :"))
    y = int(input("Enter number 1 :"))

    print("result is : ",x/y)


except ZeroDivisionError as msg:

    print("cannot divide with zero")
    logging.exception(msg)

except ValueError as msg:

    print("Enter only inter valuse")
    logging.exception(msg)