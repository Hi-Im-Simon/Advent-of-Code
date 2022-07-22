f = open('2016/inputs/input-11.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip().split().count('a') for x in f]
    return data


def part1_2(f, part):
    items = prep_input(f)
    if part == 2:
        items[0] += 4
        
    moves = 0
    for i in range(len(items) - 1):
        while items[i] != 0:
            moves += 1
            items[i] -= 2
            items[i + 1] += 2
            if items[i] > 0:
                moves += 1
                items[i] += 1
                items[i + 1] -= 1
    return moves


# doesn't work for test inputs, because their input is too small for the algorithm to work
print(f"part 1:\n{ part1_2(f, 1) }")
print(f"part 2:\n{ part1_2(f, 2) }")
