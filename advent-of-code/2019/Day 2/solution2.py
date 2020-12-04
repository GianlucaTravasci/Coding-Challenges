def process_array(input_arr):
    arr = input_arr[:]

    for index in range(0, len(arr), 4):
        operator = arr[index]
        numberA = arr[arr[index + 1]]
        numberB = arr[arr[index + 2]]
        if operator == 99:
            return arr[0]
        elif operator == 1:
            arr[arr[index + 3]] = numberA + numberB
        elif operator == 2:
            arr[arr[index + 3]] = numberA * numberB

    return arr[0]


if __name__ == "__main__":
    with open('input.txt') as f:
        input = [int(x) for x in f.read().split(',')]

    for noun in range(100):
        for verb in range(100):
            input[1] = noun
            input[2] = verb

            output = process_array(input)

            if output == 19690720:
                print(100 * noun + verb)
                break
