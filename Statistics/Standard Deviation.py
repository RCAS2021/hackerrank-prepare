#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
import math

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = (sum(arr)/len(arr))
    
    for i in range(len(arr)):
        arr[i] = (math.pow(arr[i] - mean, 2))
    print(f"{math.sqrt(sum(arr)/len(arr)):.1f}")
        
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)