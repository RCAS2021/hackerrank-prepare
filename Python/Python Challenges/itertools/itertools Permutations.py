from itertools import permutations

S, K = input().split()

lis = sorted(list(permutations(S.upper(), int(K))))

for j in lis:
    print("".join(j), sep="\n")