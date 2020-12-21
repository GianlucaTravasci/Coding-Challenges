from operator import add, mul


with open('input.txt') as file:
    expressions = [line.replace(' ', '') for line in file.read().splitlines()]


def get_operator(expression, advanced):
    depth = 0
    candidate = None
    for i, symbol in enumerate(reversed(expression)):
        if symbol == '(':
            depth += 1
        if symbol == ')':
            depth -= 1
        if symbol == '*' and depth == 0:
            candidate = mul, len(expression) - i - 1
            break
        if symbol == '+' and depth == 0:
            candidate = add, len(expression) - i - 1
            if not advanced:
                break
    return candidate


