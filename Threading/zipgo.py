from zipfile import *

f = ZipFile("thread.zip","w")

f.write("thread.txt")
f.write("active_conuntM.py")
f.write("conditionObj.py")
f.write("interthread.py")
f.write("isAliveM.py")
f.write("joinM.py")
f.write("queues.py")
f.write("synchroniation.py")
f.write("tafic.py")
f.write("Thread5.py")

print("Done ....")

f.close()