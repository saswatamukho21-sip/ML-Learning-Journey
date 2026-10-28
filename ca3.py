import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

x=np.arange(len(df["Name"]))

plt.bar(x,df["Percentage"],color=["blue","red","green","yellow","orange","pink","violet"])
plt.xticks(x,df["Name"])
plt.title("Percentage Comparison")
plt.xlabel("Names")
plt.ylabel("Percentage")
plt.axhline(y=70,color="red",linestyle="--",label="Pass Line")
plt.legend()
plt.show()

plt.figure()

plt.scatter(df["Maths"],df["Science"],c=range(7),s=100)
plt.title("Maths vs Science")
plt.xlabel("Maths")
plt.ylabel("Science")
plt.show()

plt.figure()

correlation=df[["Maths","Science","English","Attendance"]].corr()
sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.title("Heatmap")
plt.show()
        


