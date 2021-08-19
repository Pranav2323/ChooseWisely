import pandas as pd

data=pd.read_excel('business management.xlsx')
result=[]
for index,row in data.iterrows():
    temp=[row['college'],row['location']]
    result.append(temp)

print(result)
