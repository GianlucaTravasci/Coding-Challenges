def get_input_from_file():
    with open('input.txt', 'r') as file:
        record = file.read().split('\n')
    return record


def count_bags(bag, rules, cache):
    for rule in rules:
        x = rule.split(" contain ")
        x[0] = x[0].replace("bags", "bag")
        y = x[1].split(", ")
        if bag in x[1] and x[0] not in cache:
            cache.append(x[0])
            bn = ["".join(y for y in k if y.isalpha() or y == ' ').replace("bags", "bag") for k in y]
            count_bags(x[0], rules, cache)
    return len(cache)





if __name__ == "__main__":
    a = get_input_from_file()
    cache_one = []
    print('solution 1:', count_bags("shiny gold bag", a, cache_one))
    print('solution 2:', count_individual("shiny gold bag", a))
