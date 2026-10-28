import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
hours   = np.array([2, 4, 3, 6, 5, 7, 8, 1, 9, 4, 6, 3])
marks   = np.array([55, 70, 62, 82, 75, 88, 91, 45, 95, 68, 80, 60])
plt.scatter(hours,marks,color="blue",s=100)
plt.title("Marks vs hours")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

plt.figure()

plt.hist(marks,bins=5,color="blue",edgecolor="black")
plt.title("Bar Graph")
plt.xlabel("Marks")
plt.ylabel("Number of student")
plt.show()

#More Hour Study=More Marks

