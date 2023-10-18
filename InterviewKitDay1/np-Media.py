import numpy as np
n = int(input())

arr = np.array(input().split(), dtype=int)
arr.sort()

middle = len(arr)//2
print(arr[middle])