"""6 kyu https://www.codewars.com/kata/514b92a657cdc65150000006/train/python"""

def multiples_of_3_or_5_func(number):
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 ==0:
            total += i
    return total
