import re


def parse_input(line):
    key, val = line.split(' = ')
    if key == 'mask':
        return key, val
    else:
        return int(re.findall(r'\d+', key)[0]), bin(int(val))[2:]


if __name__ == "__main__":
    with open("input.txt") as file:
        record = [parse_input(line) for line in file.read().splitlines()]

    print("Part one: ", record)
    print("Part two: ")