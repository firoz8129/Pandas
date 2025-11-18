import pandas as pd
import numpy as np

dict={
    "name":["firoz","uvais","rashid","naimu","kannappi","noora"],
    "department":["data",'hr','desiner','it',"it","mngr"],
    "salary":[80000,60000,3000,10000,55000,25000]
}
df=pd.DataFrame(dict)
print(df)
print('\n',df["salary"]>20000)
print('\n',df['salary'])
print('//\n',df['department'].isin(['it',"data"]))
# print('....\n',df[df['department'].isin(['data', 'it'])])
# print('\n',df[df['department'].isin(['hr','desiner'])])
#
# print('\n',df[df["salary"].between(20000,60000)])
# print('////\n',df.query('salary>20000'))
# #combine  str
# print('\n',df[df['name'].str.startswith(("f","n"))])

#combine
#Concatenate two DataFrames.
dict={
    "name":["firoz","uvais","rashid","naimu","kannappi","noora"],
    "department":["data",'hr','desiner','it',"it","mngr"],
    "salary":[80000,60000,3000,10000,55000,25000]
}
dict1={
    "full name":["adil","uvais","rashid","naimu","kannappi","noora"],
    "department":["data",'hr','desiner','mtr',"it","mngr"],
    "salary":[80000,60000,3000,10000,55000,25000]
}
# df=pd.DataFrame(dict)
# df1=pd.DataFrame(dict1)
# print("\n",pd.concat([df,df1],axis=1))
# print("\n",pd.concat([df,df1],axis=0))

#Merge two DataFrames on a common column.
# print("\n",pd.merge(df,df1,on=["salary",'department']))
s=df[df['name'].str.startswith(('u','r'))]
print(s)
print('?????0\n',df[df['name'].str.startswith(('n','u'))])
#
#groupe
data1={
    "department":["HR",'DATA','HR','IT','IT','HR'],
    'name':['aaa','bbb','ccc','ddd','eee','fff'],
    'salary':[80000,60000,3000,10000,55000,25000],
    'bonus':[10000,55000,25000,30000,45000,35000],
}
df=pd.DataFrame(data1)
print('\n',df)
#single group
print('\n',df.groupby('department')['name'].sum())

print('\n',df.groupby('department')['salary'].agg(['sum','mean','max']))
#2 group
print('\n',df.groupby('department')[["salary","bonus"]].sum())
print('5555\n',df.groupby("department").first())
#
# #use get_group() to retrieve (select) all rows that belong to a specific group
# print("\n",df.groupby('department').get_group('HR'))


# df=pd.read_csv("data1.csv")
# print(df)
