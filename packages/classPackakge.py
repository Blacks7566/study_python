import sys
from turtle import st

from packageClass.emp import Employee
from packageClass.stude import Student


sys.path.append("D:\go\packages\packageClass")

from emp import *
from stude import *


em = Employee()
st = Student()

em.display()


print()

st.stData()