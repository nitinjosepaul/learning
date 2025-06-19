#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def navigate_terrain(path_itr, current_lvl):
    start_step = next(path_itr)
    if start_step == 'U':
        current_terrain = 'mountain'
        current_lvl += 1
    else:
        current_lvl -= 1
        current_terrain = 'valley'
    while current_lvl != 0:
        step = next(path_itr)
        current_lvl = current_lvl + 1 if step == 'U' else current_lvl - 1
    else:
        if current_terrain == 'valley':
            return 1, current_lvl
        return 0, current_lvl


def countingValleys(steps, path):
    # Write your code here
    path_iterator = iter(path)
    current_level = 0
    valley_count = 0

    while True:
        try:
            terrain, current_level = navigate_terrain(path_iterator, current_level)
            valley_count += terrain
        except StopIteration:
            break

    return valley_count


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    print(countingValleys(steps, path))