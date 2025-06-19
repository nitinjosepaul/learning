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
    positive = zero = negative = 0
    total = len(arr)

    for number in arr:
        if number == 0:
            zero += 1
        elif number > 0:
            positive += 1
        else:
            negative += 1
    print(f'{positive/total: .6f}')
    print(f'{negative/total: .6f}')
    print(f'{zero / total: .6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)