import numpy as np
a=np.random.randint(1,100,(4,3))
print(a.shape)
print(a[1,:])
print(a[: ,2])
print(a.mean())
print(np.mean(a))
