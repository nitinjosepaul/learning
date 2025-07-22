# This file contains various Python code snippets demonstrating different functionalities.

# How to iterate over a dictionary and print each key-value pair
def iterate_dict():
    d = {'three': 3, 'one': 1, 'two': 2}

    for key, value in d.items():
        print(f"{key} : {value}")

    print('---')

    for key in d:
        print(f"{key} : {d[key]}")

#### How to iterate over two lists simultaneously and print the larger value
def compare_lists():
    l1 = [1, 2, 30, 4, 5, 60]
    l2 = [4, 5, 6, 7, 8, 9]

    for i, j in zip(l1, l2):
        print(max(i, j))


