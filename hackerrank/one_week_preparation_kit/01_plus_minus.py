#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
# Write your code here
    positive = negative = zero = 0
    size = len(arr)
    for item in arr:
        if item > 0:
            positive += 1
        elif item < 0:
            negative += 1
        else:
            zero += 1
    print("{:6f}".format(positive/size))
    print("{:6f}".format(negative/size))
    print("{:6f}".format(zero/size))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
