import numpy as np

N, M = map(int, input().split())

A = np.array([input().split() for _ in range(N)], dtype=int)

result = np.min(A, axis=1)

print(np.max(result))