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
    meridiem_str = s[-2:]
    hour, minute, second= s[:-2].split(':')
    if meridiem_str == 'AM':
        hour = '00' if int(hour) == 12 else hour
    elif meridiem_str =='PM':
        hour = hour if int(hour) == 12 else str(int(hour) + 12)
    return f'{hour}:{minute}:{second}'


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)

