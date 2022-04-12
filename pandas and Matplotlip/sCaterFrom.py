from matplotlib import pyplot as plt


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='scatter' , color='r',s=80,marker="o")

plt.xlabel("X")
plt.ylabel("Y")

plt.title("ScatterPlot")

plt.show()