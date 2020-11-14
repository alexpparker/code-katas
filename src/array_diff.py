"""6 kyu https://www.codewars.com/kata/523f5d21c841566fde000009/train/python"""


def array_diff_func(a, b):
    return [item for item in a if item not in b]
