from collections import defaultdict


def get_input_from_file():
    with open('input.txt', 'r') as file:
        record = list(map(lambda x: int(x), file.read().splitlines()))
    record.sort()
    record.append(record[-1] + 3)
    return record


def part1(adapters):
    init = one = three = 0
    for adapter in adapters:
        diff = adapter - init
        if diff == 1:
            one += 1
        if diff == 3:
            three += 1
        init = adapter
    return one * three


def part2(adapters):
    options = defaultdict(int)
    options[0] = 1
    for i in adapters:
        options[i] = sum([options[i - d] for d in [1, 2, 3]])
    return options[adapters[-1]]


if __name__ == "__main__":
    adapters = get_input_from_file()
    print('solution 1:', part1(adapters))
    print('solution 2:', part2(adapters))
