from functools import reduce


def get_input_from_file():
    with open('input.txt', 'r') as file:
        record = file.read().split('\n\n')
    return record


def count_total_yes(record):
    clear_newline = lambda entry: entry.replace('\n', '')
    batch = list(map(clear_newline, record))
    groups = []
    for answares in batch:
        cache = {}
        for answare in answares:
            if answare not in cache:
                cache[answare] = answare
        groups.append(len(cache))
    counter = 0
    for group in groups:
        counter += group
    return counter


def count_all_yes(record):
    batch = map(str.split, record)
    groups = []
    for group_answers in batch:
        group_answers = list(map(set, group_answers))
        all_yes = reduce(set.intersection, group_answers)
        groups.append(all_yes)
    return sum([len(group) for group in groups])


if __name__ == "__main__":
    a = get_input_from_file()
    print('solution 1:', count_total_yes(a))
    print('solution 2:', count_all_yes(a))
