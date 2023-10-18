import numpy as np

n = int(input())

A = np.array([input().split() for _ in range(n)], dtype=int)
B = np.array([input().split() for _ in range(n)], dtype=int)

print(np.dot(A, B))