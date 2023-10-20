#Using list comprehension
def staircase(n):
    print(*[("#"*i).rjust(n) for i in range(1, n+1)], sep="\n")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)