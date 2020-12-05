def get_input_from_file():
    with open('input.txt') as file:
        seats = file.read().splitlines()
        return seats


def decode_place(code, row_col):
    for char in code:
        if char == 'F' or char == 'L':
            row_col[0] = row_col[0]
            row_col[1] = (row_col[0] + row_col[1]) // 2
        elif char == 'B' or char == 'R':
            row_col[0] = (row_col[0] + row_col[1]) // 2 + 1
            row_col[1] = row_col[1]
    if code[-1] == 'F' or code[-1] == 'L':
        return row_col[0]
    else:
        return row_col[1]


