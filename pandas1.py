import pandas as pd
data={"Name":["Rahul","Priya","Amit","Sneha","Raj"],
      "Age":[25,28,22,30,26],
      "City":["Delhi","Mumbai","Delhi","Banglore","Mumbai"],
      "Salary":[50000,75000,40000,90000,60000]
    }
df=pd.DataFrame(data)
print(df)

print(df.head(3))
print(df.shape)
print(df[["Name","Salary"]])
print(df[df["City"]=="Mumbai"])
df["Tax"]=df["Salary"]*0.10
print(df)
df["Take_Home"]=df["Salary"]-df["Tax"]
print(df)
df_avg=df["Take_Home"].mean()
print(df_avg)
df_sorted=df.sort_values("Salary",ascending=False)
print(df_sorted)
 
