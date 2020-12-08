import copy


def parse_to_list(input_file):
    rules = []
    for line in input_file:
        split_line = line.split()
        rules.append([split_line[0], int(split_line[1]), 0])
    return rules


def part1(rules):
    i = 0
    acc = 0
    completed_idx = set()

    while i not in completed_idx and i < len(rules):
        completed_idx.add(i)
        current = rules[i]
        if current[0] == "jmp":
            i += current[1]
            continue
        if current[0] == "acc":
            acc += current[1]

        i += 1

    return (i < len(rules)), acc





if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_file = f.read().splitlines()
    rules = parse_to_list(input_file)
    infinite_loop, acc = part1(rules.copy())
    print(f"Part 1 result: {acc}.")

    part2 = part2(rules)
    print(f"Part 2 result: {part2}. ")