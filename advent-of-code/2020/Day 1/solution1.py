from itertools import combinations


# return the product of two that summed gives 2020

def problem1(values):
    for a, b in combinations(values, 2):
        if a + b == 2020:
            print('matching numbers are: ', a, b)
            return a * b


# return the product of 3 numbers that summed gives 2020

def problem2(values):
    for a, b, c in combinations(values, 3):
        if a + b + c == 2020:
            print('matching numbers are: ', a, b, c)
            return a * b * c


