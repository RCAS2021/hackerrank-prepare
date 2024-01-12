#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    res = []
    sumW = 0
    sumRes = 0
    for i in range(n):
        res.append(X[i] * W[i])
        sumW += W[i]
        sumRes += res[i]
    print(round(sumRes/sumW, 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)