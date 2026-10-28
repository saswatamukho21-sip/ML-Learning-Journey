import matplotlib.pyplot as plt   # 'plt' is the universal nickname
import numpy as np
import pandas as pd

rahul_marks = [85, 78, 92, 88, 95]
priya_marks = [90, 82, 88, 94, 91]
exams = [1, 2, 3, 4, 5]

plt.plot(exams, rahul_marks, color="blue",  label="Rahul", marker="o")
plt.plot(exams, priya_marks, color="red",   label="Priya", marker="s")

plt.title("Exam Performance")
plt.xlabel("Exam Number")
plt.ylabel("Marks")
plt.legend()    # Shows the color labels (Rahul, Priya)
plt.grid(True)
plt.show()
