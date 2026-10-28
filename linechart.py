import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rahul_marks=[85,34,35,56,56]
sagar_marks=[90,45,56,89,23]
exam=[1,2,3,4,5]

plt.plot(exam,rahul_marks,color="blue",label="Rahul",marker="o")
plt.plot(exam,sagar_marks,color="red",label="Sagar",marker="^")

plt.title("Exam performance")
plt.xlabel("Exam Number")
plt.ylabel("Marks obtained")
plt.legend()
plt.grid(True)
plt.show()
