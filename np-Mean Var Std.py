import numpy as np

N, M = map(int, input().split())

A = np.array([input().split() for _ in range(N)], dtype=int)

print(np.mean(A, axis=1))
print(np.var(A, axis=0))
print(round(np.std(A), 11)) #round(..., 11) -> 11 decimal place precision