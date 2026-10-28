import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# 1 row, 2 columns of charts, figure size 12x5 inches

# Left chart
axes[0].bar(["Maths", "Science", "English"], [85, 92, 78])
axes[0].set_title("Marks by Subject")

# Right chart
axes[1].plot([1,2,3,4,5], [85,78,92,88,95], marker="o")
axes[1].set_title("Exam Performance")

plt.tight_layout()   # Prevent charts from overlapping
plt.show() 

