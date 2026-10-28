import pandas as pd
data = {
    "Name":       ["Rahul","Priya","Amit","Sneha","Raj","Meera","Arjun"],
    "Maths":      [85, 92, 35, 78, 60, None, 88],
    "Science":    [78, 95, 42, 82, 55, 90,   None],
    "English":    [88, 91, 50, 75, 70, 85,   92],
    "Attendance": [90, 95, 60, 88, 72, 91,   85]
}
df=pd.DataFrame(data)
print(df)
print(df.shape)
print(df.info())
print(df.isnull().sum())
df["Maths"]=df["Maths"].fillna(df["Maths"].mean())
df["Science"]=df["Science"].fillna(0)
df["Total"]=df["Maths"]+df["Science"]+df["English"]
df["Percentage"]=(df["Total"]/300)*100
top=df[df["Percentage"]>=70]
print(top)
df_sorted=df.sort_values("Percentage",ascending=False)
print(df_sorted)
print(df["Percentage"].mean())


