import random
from operator import index

import pandas as pd
import numpy as np
from numpy.ma.core import arange
from numpy.matlib import randn
# from numpy.random import randint
#
dict= {
    "one":pd.Series([1,2,3,4,5],index=["a",'b','c','d','e']),
    "two":pd.Series([7,8,9,4],index=["a",'b','c','d'])
}
df=pd.DataFrame(dict)
print(df)
print(df['one'])
print(df['two'])
print(df[['one','two']])
#add tree column
df['three']=[10,2,55,66,85]
print(df)
#
# add one and three
# df["four"]=df['one']+df['three']
# print(df)
#
# #
df=pd.DataFrame(randn(5,6),index='A B C D F'.split(),columns='U V W X Y Z'.split())
print('\n',df)
#LOC
print(df.loc['C':'F'])
print('....\n',df.loc['A'])
print(df.loc['C','X'])
print(df.loc['a':'c','v':'y'])

# dct={
#     "name":["firoz",'neseema','musthafa','insha'],
#     'age':[21,46,50,2.5],
#     'sibilings':['uvais','harshana','misriya','seleena']
# }
# df=pd.DataFrame(dct)
# print('\n',df)
# df=pd.DataFrame(dct ,index=['A','B','C','D'])
# df1=df.rename(columns={"name":"aaa","age":"bbb","sibilings":"ccc"})
# print('\n',df1)
#
# #ILOC
# print('\n',df.iloc[1:4,0:3])
print('\n',df.loc['A':'B'])
# print('\n',df.loc['B':'C'])

# #
# df=pd.DataFrame(randn(5,5),columns=['A','B','C','D','E'])
# print(df)
# print(df[df<0])
# print(df[df>0])
#
# print((df["C"]>0))
# print(df[1:2]<0)
#
# data=np.array(arange(20))
# b=data.reshape(4,5)
# print(b)
# df=pd.DataFrame(b)
# print('....\n',df)
# df.columns=['a','b','c','d','e']
# print('\n',df)

# print(df.iloc[1:3,2:4])
# print(df.iloc[1:3,2:4]>5)

#
# df=pd.DataFrame(randn(5,6),columns=['A','C','B','E','D','F'])
# print(df.set_index("B",drop=True))
# print(df.set_index([   "A","B"]))
# print(df)

#revise
# df=pd.DataFrame([5,2,5,6,9,8,5])
# print(df)

# s=pd.Series(np.random.randn(30))
# print(s.head())
# print(s.tail())
# print(s.describe())
#
# print('.....',s.info())

dict={
    "name":['A','B','C','D','E'],
    "age":[10,20,30,40,50],
    "salary":[1000,2000,5000,4000,6000]
}
df=pd.DataFrame(dict)
print(df)
df1=df[df['salary'].between(2000,5000)]
print(df1)
print(df.head(2))
h=df[df['age']>20]
print(h)