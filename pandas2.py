import pandas as pd
data={
     "Product":["Phone","Laptop","Tablet","Watch","Earphones"],
     "Price":[15000,None,25000,8000,None],
     "Rating":[4.5,4.2,None,4.8,4.1]
     }
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df["Price"]=df["Price"].fillna(df["Price"].mean())
df["Rating"]=df["Rating"].fillna(4.0)
print(df)

 
