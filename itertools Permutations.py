from itertools import permutations

S, K = input().split()

sort = sorted(S)
lis = list(permutations(sort, int(K)))

for j in lis:
    print("".join(j), sep="\n")