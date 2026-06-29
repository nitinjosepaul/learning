import pytest

def fizzBuzz(value):
    """
    Args:
        value: Integer
    Returns:
    "1" when value is 1
    "2" when value is 2
    "Fizz" when value is 3 or any multiple of 3
    "Buzz" when value is 5 or any multiple of 5
    "FizzBuzz" when value is 15 or any multiple of 3 and 5
    """
    if type(value) != int:
        return 'Only int can be passed in'
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(value, 5):
        return "Buzz"
    return str(value)

def isMultiple(value, mod):
    return value % mod == 0

def checkFizzBuzz (value, expectedRetVal):
    retval = fizzBuzz(value)
    assert retval == expectedRetVal

def test_returns1WhenPassedIn1():
    checkFizzBuzz(1, "1")

def test_returns2WhenPassedIn2():
    checkFizzBuzz(2, "2")

def test_returnsFizzWhenPassedIn3():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWhenPassedIn5():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWhenPassedIn6():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWhenPassedIn10():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWhenPassedIn15():
    checkFizzBuzz(15, "FizzBuzz")

def test_handlesFloat():
    checkFizzBuzz(3.0, 'Only int can be passed in')

def test_handlesString():
    checkFizzBuzz('3.0', 'Only int can be passed in')
