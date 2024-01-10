import numpy as np

n, m = map(int, input().split()) #Gets value for rows and columns

lis = np.array([input().split() for _ in range(n)], dtype = int) #Makes matrix

print(np.transpose(lis)) #Gets array transposition EX: [[a0b0], [a1b1]]
print(lis.flatten()) #Creates a copy with one dimension