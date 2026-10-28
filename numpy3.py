import numpy as np
a=np.arange(10,70,10)
print(a.reshape(2,3))
print(a.reshape(3,2))
print(a*3)
b=a.reshape(2,3)
print(b[0,1])
print(b[1,2])
