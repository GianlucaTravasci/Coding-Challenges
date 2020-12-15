def get_last_spoken(start, turns):
    memory = {n: [i] for i, n in enumerate(start)}
    last_spoken = start[-1]

    for turn in range(len(start), turns):
        history = memory.get(last_spoken)

        if history is None:
            memory[last_spoken] = [turn]
            last_spoken = 0
            continue

        last_spoken = 0 if len(history) == 1 else history[-1] - history[-2]

        if last_spoken in memory:
            memory[last_spoken].append(turn)
        else:
            memory[last_spoken] = [turn]

    return last_spoken


if __name__ == '__main__':
    print('part 1:', get_last_spoken([9, 19, 1, 6, 0, 5, 4], 2020))
    print('part 2:', get_last_spoken([9, 19, 1, 6, 0, 5, 4], 30000000))
