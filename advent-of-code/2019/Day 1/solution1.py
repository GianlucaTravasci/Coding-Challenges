def calculate_fuel_needed(total_module_fuel):
    return total_module_fuel // 3 - 2





def get_input_from_file():
    with open('input.txt') as file:
        values = [int(line) for line in file.readlines()]
        return values


if __name__ == "__main__":
    modules = get_input_from_file()
    print('solution 1: ', compute(modules)[0])
    print('solution 2: ', compute(modules)[1])
