#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lis = map(lambda x: x.capitalize(), s.split(" "))
    return " ".join(lis)

if __name__ == '__main__':
    s = input()

    text = solve(s)

    print(text)
