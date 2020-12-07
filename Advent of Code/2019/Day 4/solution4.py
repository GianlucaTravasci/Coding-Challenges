def valid_password(digit):
    is_valid = False
    last_digit = '0'
    for i in range(len(digit)):
        if digit[i] < last_digit:
            return False
        if digit[i] == last_digit:
            is_valid = True
        last_digit = digit[i]
    return is_valid


def valid_password_two(digit):
    is_valid = False
    digit_group_started = 1
    last_digit = '0'
    for i in range(len(digit)):
        if digit[i] < last_digit:
            return False
        if digit[i] == last_digit:
            digit_group_started += 1
        else:
            if digit_group_started == 2:
                is_valid = True
            digit_group_started = 1
        last_digit = digit[i]
    if digit_group_started == 2:
        is_valid = True
    return is_valid


if __name__ == '__main__':
    with open('input.txt') as f:
        low, high = [int(x) for x in f.read().split('-')]
    c = 0
    d = 0
    for i in range(low, high + 1):
        if valid_password(str(i)):
            c += 1
        if valid_password_two(str(i)):
            d += 1

    print('solution 1: ', c)
    print('solution 2: ', d)
