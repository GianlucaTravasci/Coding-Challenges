with open('input.txt', 'r') as file:
    map_lines = file.read().splitlines()

line_length = len(map_lines[0])


def way_tree_counter(right, down):
    tree_counter = 0
    for i in range(0, int(len(map_lines) / down)):
        step = i * right
        if map_lines[i * down][step % line_length] == '#':
            tree_counter += 1
    return tree_counter


# Part 1
print(f"Part one (right 3, down 1): {way_tree_counter(3, 1)}")

# Part 2
ways = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
multiply_all = 1
for way in ways:
    multiply_all *= way_tree_counter(way[0], way[1])

print(f"Part two: {multiply_all}")
