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


def recursive_combat(deck1, deck2):
    previous_games = set()

    player1 = deck1.copy()
    player2 = deck2.copy()

    winner = None
    while not winner:
        if (tuple(player1), tuple(player2)) in previous_games:
            winner = "p1"
        else:
            previous_games.add((tuple(player1), tuple(player2)))

            card1 = player1.pop(0)
            card2 = player2.pop(0)

            if card1 <= len(player1) and card2 <= len(player2):
                result = recursive_combat(player1[:card1], player2[:card2])[0]

                if result == "p1":
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)
            else:
                if card1 > card2:
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)

            if len(player1) == 0:
                winner = "p2"
            elif len(player2) == 0:
                winner = "p1"

    return winner, player1, player2




if __name__ == "__main__":
    with open('input.txt') as file:
        data = file.read().strip().split('\n\n')

    player_one = list(map(int, data[0].split('\n')[1:]))
    player_two = list(map(int, data[1].split('\n')[1:]))

    print('Solution for part one:', part_one(player_one, player_two))
    print('Solution for part one:', part_two(player_one, player_two))