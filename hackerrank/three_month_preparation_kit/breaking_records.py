#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_count = max_count = 0
    minimum = maximum = scores[0]
    for score in scores[1:]:
        if score < minimum:
            minimum = score
            min_count += 1
        elif score > maximum:
            maximum = score
            max_count += 1
    return [max_count, min_count]

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')
