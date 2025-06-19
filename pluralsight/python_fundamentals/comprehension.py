from math import sqrt
from pprint import pp

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

pp([item for item in range(101) if is_prime(item)])