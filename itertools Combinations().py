from itertools import combinations

S, K = input().split()

S = S.upper()

sort = sorted(S)

for i in range(1, int(K)+1):
    lis = list(combinations(sort, i))
    for j in lis:
        print("".join(j), sep="\n")