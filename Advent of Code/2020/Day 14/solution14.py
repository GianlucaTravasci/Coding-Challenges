import re
from itertools import zip_longest, product


def parse_input(line):
    key, val = line.split(' = ')
    if key == 'mask':
        return key, val
    else:
        return int(re.findall(r'\d+', key)[0]), bin(int(val))[2:]


def mask_value(mask, val):
    return int(
        ''.join([digit if m == 'X' else m for m, digit in zip_longest(mask[::-1], val[::-1], fillvalue='0')][::-1]), 2)


def part1(record):
    mask = ''
    memory = {}
    for key, val in record:
        if key == 'mask':
            mask = val
        else:
            memory[key] = mask_value(mask, val)
    return sum(memory.values())


if __name__ == "__main__":
    with open("input.txt") as file:
        record = [parse_input(line) for line in file.read().splitlines()]

    print("Part one: ", part1(record))
    print("Part two: ")
