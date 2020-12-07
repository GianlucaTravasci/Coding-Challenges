def get_input_from_file():
    with open('input.txt', 'r') as file:
        record = file.read().split('\n')
    return record





if __name__ == "__main__":
    a = get_input_from_file()
    cache_one = []
    print('solution 1:', count_bags("shiny gold bag", a, cache_one))
    print('solution 2:', count_individual("shiny gold bag", a))
