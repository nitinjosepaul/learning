#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def computeSum(arr, row, column):
    s = 0
    for j in range(column, column + 3):
        s = s + arr[row][j] + arr[row + 2][j]
    s += arr[row + 1][column + 1]
    return s


def hourglassSum(arr):
    # Write your code here
    rows = len(arr)
    columns = len(arr[0])
    sums = []
    for i in range(rows - 2):
        for j in range(columns - 2):
            sums.append(computeSum(arr, i, j))
    return max(sums)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
