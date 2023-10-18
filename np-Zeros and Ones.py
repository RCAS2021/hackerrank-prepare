import numpy as np

N, M, P = map(int, input().split())
zeros = []
ones = []

for _ in range(N):
    zeros.append(np.zeros((M, P), dtype=int))
    ones.append(np.ones((M, P), dtype=int))

arr = [*zeros, *ones]
print(*arr, sep="\n")