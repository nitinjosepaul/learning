import sys


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    # here we get the \n also in each line
    for line in f:
        print(line, end='')
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])