
import numpy as np
import pandas as pd
# #empty series
# s=pd.Series()
# print(s)
# s=pd.Series(dtype="int")
# print(s)
# s=pd.Series(dtype="object")
# print(s)
# s=pd.Series(dtype="float")
# print(s)
# a=pd.Series([1,2,3,4,5],index=[10,11,12,13,15])
# print(a)
# a=pd.Series([1,'mm','jjj',.36])
# print(a)
#
# a=pd.Series([1,2,3,4,5])
# print(a)
# #
# # #dict to series
data={
    "a":1,'b':2,"c":3,"d":4,"e":5
}
s=pd.Series(data)
print(s)
#
# #list to seris
# a=[1,2,3,4,5,100]
# s=pd.Series(a)
# print(s)
# #
# # #arrey to series
# a=np.array([10,203,30,4,0,5,66,2])
# print(a)
# s=pd.Series(a)
# print(s)
# #
# # #reshap index
data={
"a":1,'b':2,"c":3,"d":4,"e":5
}
s=pd.Series(data,index=['b',"c","a","e",'d',"l"])
print(s)
# #
# # #scalar
s=pd.Series(5,index=['b',"c","a","e",'d',"l"])
print(s)
# #
# # #slicing
# s=pd.Series([9,8,7,4,5],index=[1,2,3,4,5])
# print(s)
# print(s[0:2])
# print(s[-2:])
#
# #INDEXING
# s=pd.Series([11,22,33,44,55])
# print(s[[0,3]])
# #
# # #
# stdnt={
#     "name":["firoz",'razi','murshi'],
#     "age":[10,22,30],
#     "mark":[22,55,88]
# }
# print(stdnt)
# s=pd.Series(stdnt)
# print(s)
# s=pd.DataFrame(stdnt)
# print(s)
# #
# #series +,-,*,/,**
# s1=pd.Series([1,2,3,4,5])
# s2=pd.Series([7,8,9,4,5])
# print(s1+s2)
# #
# # #add with i ndex
# a=pd.Series([1,2,3,4,5],index=[111,222,333,444,555])
# b=pd.Series([7,88,99,45,61],index=[111,222,888,555,333])
# print(a+b)
#
#
# #dataframe
# df=pd.DataFrame()
# print(df)
#
# #from list
# List=[[1,2,3,4,5],[7,8,9,4,5]]
# df=pd.DataFrame(List)
# print(df)
#
data=[['firoz',21],['adil',22],['ubi',28]]
df=pd.DataFrame(data)
print(df)
#
# # #dict
# # #Create a DataFrame with two columns: Name, Age.
# data={
#     'name':['firoz','uvais','musthafa','misriya',  'harshana','neseema'],
#     'age':[21,28,49,27,25,46],
#     'place':['kallar','kallar','kallar','bedakam','thiruvattor','kallar'],
#     'work':['student','accountent','hotel','hs wife','hs wife','hs wife'],
# }
# df=pd.DataFrame(data)
# print(df)
#
# #attributes
# print(df.shape)
# print(df.index)
# print(df.size)
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.T)
# print("hhh",df.columns)
# #dct series convert to dataframe
# dict={
#     'name':pd.Series(['FIROZ','abhi','ragav'],
#                            index=['a','b','c']),
#     'age':pd.Series([10,20,30],
#                     index=['a','b','c'])
# }
# df=pd.DataFrame(dict)
# print(df)
#
# # #Create a Series of numbers 1–10.
# s=pd.Series(range(1,11))
# print(s)
# # array to pd data
# a=np.array([[1,2,3,4,5],[5,6,9,7,52]])
# df=pd.DataFrame(a,columns=[10,20,30,40,50])
# print(df)
# #
# # #Rename the columns of a DataFrame
# data={
# 'name':['firoz','uvais','musthafa','misriya',  'harshana','neseema'],
#     'age':[21,28,49,27,25,46],
#
# }
# df=pd.DataFrame(data)
# print(df.rename(columns={'name':'full name','age':'full ege'}))
#
# #Add a new column to a DataFrame that calculates the square of another column.
# data={
#     'number':[1,2,3,4,5,6]
# }
# df=pd.DataFrame(data)
# print(df)
# # #add
# df['age']=[8,9,6,5,7,4]
# df['squre']=df['age']**2
# print(df)
# #
# # #remove
# df.pop("squre")
# del df["age"]
# print(df)
#
# a=[1,2,3]
# print(a)
# print(type(a))
