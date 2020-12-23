from _collections import deque


def part_one(deck_one, deck_two):
    player_one = deque(deck_one)
    player_two = deque(deck_two)

    while player_one and player_two:
        card_one = player_one.popleft()
        card_two = player_two.popleft()

        if card_one > card_two:
            player_one.append(card_one)
            player_one.append(card_two)
        else:
            player_two.append(card_two)
            player_two.append(card_one)

    score = 0
    if player_one:
        for index, value in enumerate(player_one):
            score += (50-index) * int(value)
    else:
        for index, value in enumerate(player_two):
            score += (50 - index) * int(value)
    return score




if __name__ == "__main__":
    with open('input.txt') as file:
        data = file.read().strip().split('\n\n')

    player_one = list(map(int, data[0].split('\n')[1:]))
    player_two = list(map(int, data[1].split('\n')[1:]))

    print('Solution for part one:', part_one(player_one, player_two))
    print('Solution for part one:', part_two(player_one, player_two))