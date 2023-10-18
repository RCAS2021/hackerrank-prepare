import numpy as np
np.set_printoptions(legacy='1.13') #Used for formatting

A = np.array(input().split(), dtype=float)

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))