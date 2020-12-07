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


def seat_ID_finder(seats_undecoded):
    list_seat = []
    for seat in seats_undecoded:
        rows = decode_place(seat[:7], [0, 127])
        columns = decode_place(seat[7:], [0, 7])
        seat = rows * 8 + columns
        list_seat.append(seat)
    list_seat.sort()
    seat_no = 1
    while seat_no < len(list_seat):
        if list_seat[seat_no] != list_seat[seat_no - 1] + 1:
            return list_seat, list_seat[seat_no] - 1
        seat_no += 1


def find_max_ID(list_of_IDs):
    return max(list_of_IDs)


if __name__ == "__main__":
    values = get_input_from_file()
    list_of_IDs = seat_ID_finder(values)
    print('solution 1: ', find_max_ID(list_of_IDs[0]))
    print('solution 2: ', list_of_IDs[1])
