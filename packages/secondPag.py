import sys
from wsgiref.handlers import format_date_time 

sys.path.append("D:\go\packages\package1")


from module1 import *

display()

sys.path.append("D:\go\packages\package1\subpackage")

from Module2 import *


show()