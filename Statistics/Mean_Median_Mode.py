import numpy as np

num = int(input())
x = list(map(int, input().split()))

vals, counts = np.unique(x, return_counts=True) #find unique values and their counts
mode = np.argwhere(counts == np.max(counts)) #find mode, argwhere -> return indices of array elements that are non-zero, grouped by element, max-> returns maximum of an array or along an axis

print(np.mean(x)) #print the mean of an array
print(np.median(x)) #print the median of an array
print(*vals[mode[0]]) #print first(smallest one) mode

#mode https://www.statology.org/numpy-mode/
#npargwhere https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html
#npmax https://numpy.org/doc/stable/reference/generated/numpy.max.html