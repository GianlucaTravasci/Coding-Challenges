from itertools import combinations


def get_input_from_file():
    with open('input.txt', 'r') as file:
        record = file.read().split('\n')
        input = []
        for i in record:
            input.append(int(i))
    return input


def check_sum(target_value, list_of_values):
    for a, b in combinations(list_of_values, 2):
        if a + b == target_value:
            return True


def find_first_invalid(xmas):
    for i in range(25, len(xmas)):
        if not check_sum(xmas[i], xmas[i - 25:i]):
            return xmas[i]


def find_encryption_weaknes(xmas, target):
    for i in range(len(xmas)):
        current_index = i
        batch = []
        while sum(batch) < target:
            batch.append(xmas[current_index])
            current_index += 1

        if sum(batch) == target:
            return min(batch) + max(batch)


if __name__ == "__main__":
    a = get_input_from_file()
    first_invalid = find_first_invalid(a)
    print('solution 1:', first_invalid)
    print('solution 2:', find_encryption_weaknes(a, first_invalid))
