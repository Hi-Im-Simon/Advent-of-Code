# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-08.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip().split() for x in f]
    for i, line in enumerate(data):
        if line[0] == 'rect':
            line.append('')
            line[1], line[2] = list(map(int, line[1].split('x')))
        else:
            data[i] = [line[1], int(line[2].split('=')[1]), int(line[4])]
    return data


def part1_and_2(f, flag='sum'):
    SCREEN = [[0] * 50 for _ in range(6)]
    data = prep_input(f)
    
    for line in data:
        match line[0]:
            case 'rect':
                for y in range(line[2]):
                    for x in range(line[1]):
                        SCREEN[y][x] = 1
            case 'row':
                screen_cpy = [i.copy() for i in SCREEN].copy()
                for x in range(len(SCREEN[0])):
                    screen_cpy[line[1]][x] = SCREEN[line[1]][(x - line[2]) % len(SCREEN[0])]
                SCREEN = screen_cpy
            case 'column':
                screen_cpy = [i.copy() for i in SCREEN].copy()
                for y in range(len(SCREEN)):
                    screen_cpy[y][line[1]] = SCREEN[y - line[2] % len(SCREEN)][line[1]]
                SCREEN = screen_cpy
    if flag == 'sum':
        return sum([sum(y) for y in SCREEN])
    elif flag == 'text':
        return SCREEN


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1_and_2(f) }")
print(f"part 2:")
[print(''.join(['O' if y == 1 else ' ' for y in x])) for x in part1_and_2(f, 'text')]
