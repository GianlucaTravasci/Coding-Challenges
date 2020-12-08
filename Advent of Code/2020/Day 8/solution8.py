import copy


def parse_to_list(input_file):
    rules = []
    for line in input_file:
        split_line = line.split()
        rules.append([split_line[0], int(split_line[1]), 0])
    return rules




if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_file = f.read().splitlines()
    rules = parse_to_list(input_file)
    infinite_loop, acc = part1(rules.copy())
    print(f"Part 1 result: {acc}.")

    part2 = part2(rules)
    print(f"Part 2 result: {part2}. ")