from operator import add, mul


with open('input.txt') as file:
    expressions = [line.replace(' ', '') for line in file.read().splitlines()]


