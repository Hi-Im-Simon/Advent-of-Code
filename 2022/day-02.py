tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-02.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [tuple(x.strip().split(' ')) for x in f]
    return data


def part1(f):
    data = prep_input(f)
    ans = 0
    for round in data:
        if round[1] == 'X':
            ans += 1
            if round[0] == 'A': ans += 3
            elif round[0] == 'C': ans += 6
        elif round[1] == 'Y':
            ans += 2
            if round[0] == 'B': ans += 3
            elif round[0] == 'A': ans += 6
        elif round[1] == 'Z':
            ans += 3
            if round[0] == 'C': ans += 3
            elif round[0] == 'B': ans += 6
    return ans


def part2(f):
    data = prep_input(f)
    ans = 0
    for round in data:
        if round[1] == 'X':
            if round[0] == 'A': ans += 3
            elif round[0] == 'C': ans += 2
            elif round[0] == 'B': ans += 1
        elif round[1] == 'Y':
            ans += 3
            if round[0] == 'C': ans += 3
            elif round[0] == 'B': ans += 2
            elif round[0] == 'A': ans += 1
        elif round[1] == 'Z':
            ans += 6
            if round[0] == 'B': ans += 3
            elif round[0] == 'A': ans += 2
            elif round[0] == 'C': ans += 1
    return ans


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
