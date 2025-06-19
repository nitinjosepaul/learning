#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    seen = set()
    duplicate = set()
    for element in a:
        if element not in seen:
            seen.add(element)
        else:
            duplicate.add(element)
    return seen.difference(duplicate).pop()

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(lonelyinteger(a))
