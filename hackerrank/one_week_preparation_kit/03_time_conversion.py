#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
# Write your code here
    meridiem = s[-2:]
    hour, minute, second = s[:-2].split(':')
    if meridiem == 'AM':
        if int(hour) == 12:
            hour = '00'
    else:
        if int(hour) < 12:
            hour = str(int(hour) + 12)

    return ':'.join([hour, minute, second])


if __name__ == '__main__':

    s = input()

    print(timeConversion(s))
