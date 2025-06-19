import sys


def convert(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError,TypeError) as e:
        print ("Conversion error : {}".format(str(e)), file=sys.stderr)
        raise


def sqrt(x):
    if x < 0:
        raise ValueError("Cannot find square root for negative number : {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x/guess)/2.0
        i += 1
    return guess

def check_finally(fail=False):
    try:
        if fail:
            raise ValueError("Parameter 'fail' is {}".format(fail))
    except ValueError as e:
        print("Exception is {}".format(str(e)))
        print("Exception type is {}".format(str(type(e))))
        raise
    finally:
        print("Printed Finally!")

# convert("ola")
# print(sqrt(-9))
# print(sqrt(2))
check_finally(False)
print("Outside check_finally")