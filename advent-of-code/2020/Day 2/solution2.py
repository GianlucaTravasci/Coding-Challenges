import re
import operator

with open('input.txt', 'r') as file:
    lines = file.read()
    regex = r"(?P<lower>\d+)-(?P<upper>\d+) (?P<char>\w): (?P<password>\w+)"
    matches = re.findall(regex, lines)


def get_valid_passwords():
    correct = list(filter(lambda match: int(match[0]) <= match[3].count(match[2]) <= int(match[1]), matches))
    return len(correct)


print(get_valid_passwords())



