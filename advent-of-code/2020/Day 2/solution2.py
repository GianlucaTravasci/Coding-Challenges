import re
import operator

with open('input.txt', 'r') as file:
    lines = file.read()
    regex = r"(?P<lower>\d+)-(?P<upper>\d+) (?P<char>\w): (?P<password>\w+)"
    matches = re.findall(regex, lines)



