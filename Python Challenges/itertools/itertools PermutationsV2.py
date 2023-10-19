from itertools import permutations

S = input()

lis = sorted(list(permutations(S.upper(), len(S))))

for j in lis:
    print("".join(j), sep="\n")