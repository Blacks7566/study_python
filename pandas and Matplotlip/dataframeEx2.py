import pandas as pd

data = {'Name':['prashu','nikki','sudeep','ashis'],'Age':[18,22,23,24]}


df = pd.DataFrame(data)


# df.tail(2)
# df.head(1)

print(df)


print(df.head(1))
print(df.tail(1))
