
from zipfile import *

f = ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("file handing.txt")
f.write("rrr.txt")
f.write("write.txt")

print("Zip file is created successfully")
f.close()