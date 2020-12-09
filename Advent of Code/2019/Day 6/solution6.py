orbits = {
    'COM': {
        'parent': None,
        'children': [],
        'count': 0
    }
}


def input_reader():
    with open("input.txt", 'r') as file:
        line = file.readline().strip()
        while line:
            parent, child = line.split(")")
            if parent in orbits:
                orbits[parent]['children'].append(child)
            else:
                orbits[parent] = {
                    'children': [child]
                }
            if child in orbits:
                orbits[child]['parent'] = parent
            else:
                orbits[child] = {
                    'parent': parent,
                    'children': []
                }
            line = file.readline().strip()
    return orbits


input_reader()




print(part1())
print(part2())