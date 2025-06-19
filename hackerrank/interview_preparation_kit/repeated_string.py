#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    whole_repetition = n // len(s)
    remaining = n % len(s)
    a_count = s.count('a') * whole_repetition + s[:remaining].count('a')
    return a_count

if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    print(repeatedString(s, n))
