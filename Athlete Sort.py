import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0]) #athlete quantity

    m = int(first_multiple_input[1]) #number of attributes

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    arr.sort(key = lambda x: x[k], reverse = False)

    for i in range(len(arr)):
        print(*arr[i])