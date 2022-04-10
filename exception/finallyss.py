
import os



try:
    print("try block")
    os._exit(0)  # pvm stpp itself  (pvm python vertual machin)


except:
    print("except block")
    os._exit(0)

finally:
    print("finally block")


