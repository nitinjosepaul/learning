#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pair_count = 0
    color_count = {}
    for color_integer in ar:
        try:
            color_count[color_integer] += 1
            if color_count[color_integer] % 2 == 0:
                pair_count += 1
                color_count[color_integer] = 0
        except KeyError:
            color_count[color_integer] = 1
    return pair_count

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    print(sockMerchant(n, ar))
