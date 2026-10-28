import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
months  = ["Jan","Feb","Mar","Apr","May","Jun"]
revenue = [30000, 45000, 38000, 52000, 48000, 61000]
expenses= [20000, 30000, 25000, 35000, 32000, 40000]
plt.plot(months,revenue,label="Revenue",color="blue",marker="o")
plt.plot(months,expenses,label="Expenses",color="green",marker="s")

plt.title("Details")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.bar(months,revenue,color=["red","black","brown","orange","blue","yellow"])
plt.title("Bar chart revenue")
plt.xlabel("months")
plt.ylabel("Revenue")
plt.show()
 
