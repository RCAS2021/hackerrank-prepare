import numpy as np

N, M = map(int, input().split())

A = np.array([input().split() for _ in range(N)], dtype=int)

result = np.sum(A, axis=0)

print(np.prod(result))