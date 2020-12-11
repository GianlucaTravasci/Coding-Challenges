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


def check_valid_seat(i, j):
    if i < 0 or j < 0 or i >= row or j >= col:
        return False
    return True


def check_adjacent_seats(i, j, grid, part):
    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [1, 1, 1, 0, 0, -1, -1, -1]
    occupied = 0
    for k in range(8):
        adj_i = i + x[k]
        adj_j = j + y[k]
        while check_valid_seat(adj_i, adj_j) and grid[adj_i][adj_j] == '.' and part == 2:
            adj_i += x[k]
            adj_j += y[k]
        if check_valid_seat(adj_i, adj_j) and grid[adj_i][adj_j] == '#':
            occupied += 1
    return occupied




solve(seats, 1) # Part 1
solve(seats, 2) # Part 2
