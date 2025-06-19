from deque import Deque


def check_palindrome(input_string):
    deq = Deque()
    for char in input_string:
        deq.add_rear(char)

    while deq.siz() > 1:
        if deq.remove_front() != deq.remove_rear():
            return False
    return True


check_palindrome("p")
check_palindrome("oo")
check_palindrome("poop")
check_palindrome("polop")
check_palindrome("plop")