import numpy as np
a=np.array([i for i in range(1,11)])
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))

numbers=a[a>5]
print(numbers)

