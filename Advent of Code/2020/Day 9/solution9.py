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




if __name__ == "__main__":
    a = get_input_from_file()
    first_invalid = find_first_invalid(a)
    print('solution 1:', first_invalid)
    print('solution 2:', find_encryption_weaknes(a, first_invalid))
