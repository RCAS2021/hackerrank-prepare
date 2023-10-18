from itertools import groupby

S = input()

for i, j in groupby(S):
    result = len(list(j)), int(i)
    print(result[0])
    print(result, end=" ")