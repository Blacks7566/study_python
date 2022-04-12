import pandas as pd


df1 = pd.DataFrame({'Name':['pransu','nikki','sudeep','nikhil'],

                    'Age':['18','22','23','24']

                        },
                        
                        index=[0,1,2,3])


df2 = pd.DataFrame({'Name':['Rony','rocky','plane'],
                    'Age':['25','56','23']
                    },
                    
                        index=[4,5,6]    )




df_concat = pd.concat([df1,df2])

print(df_concat)