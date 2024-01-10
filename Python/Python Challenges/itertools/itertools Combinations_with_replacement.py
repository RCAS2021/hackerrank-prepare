from itertools import combinations_with_replacement

S, K = input().split()

S = S.upper()

sort = sorted(S)

lis = list(combinations_with_replacement(sort, int(K)))
print(lis)

for j in lis:
    print("".join(j), sep="\n")