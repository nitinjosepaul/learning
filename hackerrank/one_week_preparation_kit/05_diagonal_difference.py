#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    size = len(arr)
    lr_diagonal_sum = 0
    rl_diagonal_sum = 0
    for index in range(size):
        lr_diagonal_sum += arr[index][index]
        rl_diagonal_sum += arr[index][size-1-index]
    return abs(lr_diagonal_sum - rl_diagonal_sum)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(diagonalDifference(arr))