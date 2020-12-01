from itertools import combinations


# return the product of two that summed gives 2020

def problem1(values):
    for a, b in combinations(values, 2):
        if a + b == 2020:
            print('matching numbers are: ', a, b)
            return a * b


# return the product of 3 numbers that summed gives 2020

def problem2(values):
    for a, b, c in combinations(values, 3):
        if a + b + c == 2020:
            print('matching numbers are: ', a, b, c)
            return a * b * c


# aux function to grab values from input.txt file and put them in an array

def get_input_from_file():
    with open('input.txt') as file:
        values = [int(line) for line in file.readlines()]
        return values


if __name__ == "__main__":
    values = get_input_from_file()
    print('solution 1 ', problem1(values))
    print('solution2: ', problem2(values))