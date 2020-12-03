def calculate_fuel_needed(total_module_fuel):
    return total_module_fuel // 3 - 2


def compute(modules):
    first = 0
    second = 0
    for i in range(0, len(modules)):
        first += calculate_fuel_needed(modules[i])
        second += total(modules[i])
    return first, second


def total(module):
    internal_sum = 0
    fuel_needed = calculate_fuel_needed(module)
    while fuel_needed > 0:
        internal_sum += fuel_needed
        fuel_needed = calculate_fuel_needed(fuel_needed)
    return internal_sum


def get_input_from_file():
    with open('input.txt') as file:
        values = [int(line) for line in file.readlines()]
        return values


if __name__ == "__main__":
    modules = get_input_from_file()
    print('solution 1: ', compute(modules)[0])
    print('solution 2: ', compute(modules)[1])
