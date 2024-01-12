#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#
import numpy as np

def weightedMean(X, W):
    print(np.average(X, weights=W))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)

#average https://numpy.org/doc/stable/reference/generated/numpy.average.html