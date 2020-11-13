"""6 kyu https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python"""


def find_the_odd_int_func(seq):
    return [item for item in seq if seq.count(item) % 2 == 1][0]
