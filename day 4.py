import pandas as pd
import numpy as np
data={
    'name':['firoz','uvais','musthafa','misriya',  'harshana','neseema'],
    'age':[21,28,49,27,25,46],
    'place':['kallar','kallar','kallar','bedakam',np.nan,np.nan],
    'work':['student','accountent','hotel','hs wife','hs wife','hs wife'],
}
df=pd.DataFrame(data)
a=df["place"]=df["place"].fillna(df["place"].mode()[0])
print(a)


#
# dct={
#     "name":["aaa","bbb",'ccc','ddd','eee'],
#     "age":[50,20,30,50,66],
#     "salary":[2000,3000,2000,1000,8000]
# }
# df=pd.DataFrame(dct)
# print(df)
# print(df.sort_values('age'))
# print(df.drop_duplicates('salary'))
#
# print('\n',df.query('salary>2000'))
# print('\n',df.sort_values('salary'))
# print("\n",df.sum())
# print("???\n",df["age"].mean(),df["salary"].mean())
# #Get descriptive statistics using describe()
# print("\n",df.describe())
# #Calculate column-wise sum.
# print("\n",df["salary"].sum())
# #Get the maximum value of the Age column.
# print("\n",df["age"].max())
# #Find the average salary of employees.
# print('\n',df["salary"].min())
# #Sort by multiple columns (Department, then Salary)
# print("\n",df.sort_values(['salary','age']))
# #Find the top 3 highest salaries using sorting.
# print("\n",df.sort_values('salary',ascending=False).head(3))