import numpy

def arrays(arr):
    arr.reverse()
    arr = numpy.array(arr, dtype=float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)