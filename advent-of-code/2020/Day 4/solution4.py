import re


def get_input_from_file():
    lines = []
    with open('input.txt') as f:
        for line in f.readlines():
            if line != '/n':
                lines.append(line)
    return lines




if __name__ == "__main__":
    unordered_list = get_input_from_file()
    list_of_passports = format_array(unordered_list)
    print(list_of_passports)
    print('solution 1: ', compute_first(list_of_passports)[0])
    print('solution 2: ', compute_first(list_of_passports)[1])
