import re


def get_input_from_file():
    lines = []
    with open('input.txt') as f:
        for line in f.readlines():
            if line != '/n':
                lines.append(line)
    return lines


def format_array(lines):
    passports = []
    passport = {}
    for i in range(len(lines)):
        if ord(lines[i][0]) == 10:
            passports.append(passport)
            passport = {}
        else:
            fields = lines[i].split()
            for f in range(len(fields)):
                (k, v) = fields[f].split(':')
                passport[k] = v
    passports.append(passport)
    return passports


def compute_first(passports):
    valid_counter_first = 0
    valid_counter_second = 0
    for i in range(len(passports)):
        p = passports[i]
        if 'byr' in p and 'iyr' in p and 'eyr' in p and 'hgt' in p and 'hcl' in p and 'ecl' in p and 'pid' in p:
            valid_counter_first += 1
            
    return valid_counter_first, valid_counter_second


if __name__ == "__main__":
    unordered_list = get_input_from_file()
    list_of_passports = format_array(unordered_list)
    print(list_of_passports)
    print('solution 1: ', compute_first(list_of_passports)[0])
    print('solution 2: ', compute_first(list_of_passports)[1])
