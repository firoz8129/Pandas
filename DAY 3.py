import pandas as pd
import numpy as np

data={
    "name": pd.Series(['AAA','BBB','CCC','DDD','EEE']),
    "age":pd.Series([10,20,30,40,50]),
    "rating":pd.Series([.22,12,.2365,.15,.10])
}
df=pd.DataFrame(data)
print(df)
print(df.sum(numeric_only=True))
print(df.transpose())
print(df.rename(columns={"name":'full name',"age":'ages',"rating":'ratings'}
                ,index={0:10,1:20,2:30,3:40,4:50}))

#sort ascending
us_df=pd.DataFrame(np.random.randn(10,3),index=[3,2,1,6,5,4,9,8,7,10],columns=['A','B','C'])
print(us_df)
print(us_df.sort_index())
print(us_df.sort_index(ascending=False))
print(us_df.sort_index(ascending=True))

#pandas str
s=pd.Series(["tom","war","bor",np.nan,"catt","wev"])
print(s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
print(s.str.contains("o"))

#missing data handling
df=pd.DataFrame({
    "Age":["MK","HIO",np.nan,np.nan,"HIO"],
    "B":[20,np.nan,1,np.nan,2],
    "C":[np.nan,np.nan,3,44,"JKL"]
})
print(df)
print('1111\n',df.dropna())
print(df.isnull())
print(df.isnull().sum())
print('///\n',df.fillna("MK"))
print('.....\n',df.fillna(df["B"].mean()))
print(df.fillna(df["B"].median()))
print(df)
print(df.mode())
#fillna 2 methods
#print(df.fillna(method='ffill').fillna(method="bfill"))

#he mode() function returns the most frequent (repeated) value in a column or DataFrame.
#If more than one value appears the same number of times, it returns multiple modes.
data={
    'name':[np.nan,'uvais','musthafa','misriya',  'harshana','neseema'],
    'age':[21,28,49,27,25,46],
    'place':['kallar','kallar','kallar','bedakam',np.nan,np.nan],
    'work':[np.nan,'accountent','hotel','hs wife','hs wife','hs wife'],
}
df =pd.DataFrame(data)
a=df['place']=df['place'].fillna(df["place"].mode()[0])
print(a)
b=df["name"]=df["name"].fillna(df["name"].mode([0]))
print(b)

