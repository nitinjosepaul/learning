from itertools import count,islice
import sys


def sequence():
    """
    Generate Recaman's sequence
    """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c <= 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """
    Write Recaman's sequence to a file
    """
    with open(open(filename, mode='wt', encoding='utf-8')) as f:
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(), num + 1))


def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def print_series(filename):
    print(read_series(filename))


if __name__ == '__main__':
    write_sequence(filename=sys.argv[1],
                   num=int(sys.argv[2]))
    print_series(sys.argv[1])