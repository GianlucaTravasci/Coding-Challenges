def get_input_from_file():
    with open('input.txt') as file:
        seats = file.read().splitlines()
        return seats



