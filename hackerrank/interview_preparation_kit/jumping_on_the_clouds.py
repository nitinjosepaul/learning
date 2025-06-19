#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = current_cloud_position = 0

    while current_cloud_position < len(c) - 1:
        if c[current_cloud_position + 1] == 1:
            next_step = current_cloud_position + 2
        else:
            try:
                if c[current_cloud_position + 2] == 0:
                    next_step = current_cloud_position + 2
                else:
                    next_step = current_cloud_position + 1
            except IndexError:
                next_step = current_cloud_position + 1
        jumps += 1
        current_cloud_position = next_step

    return jumps

if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    print(jumpingOnClouds(c))
