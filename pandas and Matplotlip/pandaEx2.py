import pandas as pd



data = { 'a':101,'b':103,'c':105,'d':108}


s = pd.Series(data, index=['a','b','c','d','f'])
g = pd.Series([10,14,15,78,69], index=['a','b','c','d','f'])

print(s)
print(g)


print(g['c'])