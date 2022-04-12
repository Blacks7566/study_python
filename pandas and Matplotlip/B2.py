from cProfile import label
from matplotlib import pyplot as plt

x = [5,10,8]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]


plt.plot(x,y,'g',label="Line one",linewidth=3)
plt.plot(x2,y2,'c',label="Line one",linewidth=5)

plt.title("Blacks")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.legend() 

plt.grid(True,color='r')

plt.show()
