T = int(input())

for i in range(0, T):
    S = str(input())
    even = ""
    odd = ""
    for i in range(len(S)):
        if (i % 2 == 0):
            even += S[i]
        else:
            odd += S[i]
    print(even, odd)