from copy import deepcopy

seats = []

with open('input.txt') as file:
    for line in file:
        seats.append(list(line.rstrip()))

row = len(seats)
col = len(seats[0])


def check_valid_seat(i, j):
    if i < 0 or j < 0 or i >= row or j >= col:
        return False
    return True




solve(seats, 1) # Part 1
solve(seats, 2) # Part 2
