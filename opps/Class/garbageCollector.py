# Gc (Garbage collector):
#-----------------------

# it will provide automatic memory management


# garbage collector call __del__ (distructor)



import gc

# it have some method
# 1. isenabled(): return True if GC enabled
# e. disable()  : to disable GC explicitly
# 3. enable(): to enable Gc explicitly




import time

class Test:

    def __init__(self):

        print("constructor execution")

    def __del__(self):

        print("distructor execution")


t = Test()
time.sleep(3)

print("end of the application")

