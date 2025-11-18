import pandas as pd

data = {
    'name': ['Firoz', 'Naseema', 'Musthafa'],
    'age': [25, 45, 50],
    'place': ['Kozhikode', 'Malappuram', 'Kasargod']
}

df = pd.DataFrame(data)
print(df)
print(df.info())
print(df['name'].astype(str))
print(df['age'].astype(float))
print(df.dtypes)
# df.to_csv("data.csv",index=False)
# df2=pd.read_csv('data.csv')
# print('\n',df2)
#
# #map()
# df['name']=df['name'].map(str.upper)
# print(df)
#
#
data={
    'math':[10,25,36,20],
    'science':[10,20,30,40]
}
df=pd.DataFrame(data)

def total_marks(row):
    return row["math"]+ row["science"]

df['total_marks']=df.apply(total_marks,axis=1)
print(df)
