#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    arr = s.split()
    c = []
    for i in range(len(arr)):
       c.append(arr[i].capitalize())
    return c

if __name__ == '__main__':
    s = input()

    text = solve(s)

    print(*text)