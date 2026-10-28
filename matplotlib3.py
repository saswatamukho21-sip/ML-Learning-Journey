import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
data = {
    "Student":    ["A","B","C","D","E","F"],
    "Maths":      [85, 92, 78, 96, 70, 88],
    "Science":    [80, 88, 82, 90, 75, 85],
    "English":    [75, 80, 90, 72, 85, 78]
}
df=pd.DataFrame(data)
x=np.arange(len(df["Student"]))
width=0.25
plt.bar(x-width,df["Maths"],width,color="Blue")
plt.bar(x,df["Science"],width,color="Green")
plt.bar(x+width,df["English"],width,color="Red")

plt.xticks(x,df["Student"])
plt.title("Comparison in all 3 subjects")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.legend()
plt.show()

plt.figure()

correlation=df[["Maths","Science","English"]].corr()
sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.title("Heatmap")
plt.show()

