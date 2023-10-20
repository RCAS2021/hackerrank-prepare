M = int(input())

a = list(map(int, input().split()))

N = int(input())
b = list(map(int, input().split()))

a = set(a)
b = set(b)

diff = a.difference(b)
diff2 = b.difference(a)
print(*sorted(diff.union(diff2)), sep="\n")