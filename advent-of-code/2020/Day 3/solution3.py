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

