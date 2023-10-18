import numpy as np

n = int(input())
p = []
k = []

for _ in range(n):
    k = np.array(list(map(float, input().split())))
    p.append(k)

print (round(np.linalg.det(p), 2))