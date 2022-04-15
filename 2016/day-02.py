# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-02.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    return data


def part1(f):
    KEYPAD = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    SIZE = 2
    
    data = prep_input(f)
    x, y = 1, 1
    code = 0
    
    for line in data:
        for comm in line:
            match comm:
                case 'U':
                    y = max(y - 1, 0)
                case 'R':
                    x = min(x + 1, SIZE)
                case 'D':
                    y = min(y + 1, SIZE)
                case 'L':
                    x = max(x - 1, 0)
        code = code * 10 + KEYPAD[y][x]
    return code


def part2(f):
    KEYPAD = [(0, 0, '1', 0, 0), (0, '2', '3', '4', 0), ('5', '6', '7', '8', '9'), (0, 'A', 'B', 'C', 0), (0, 0, 'D', 0, 0)]
    SIZE = 4
    
    data = prep_input(f)
    x, y = 0, 2
    code = ''

    for line in data:
        for comm in line:
            match comm:
                case 'U':
                    yy = max(y - 1, 0)
                    if KEYPAD[yy][x]: y = yy
                case 'R':
                    xx = min(x + 1, SIZE)
                    if KEYPAD[y][xx]: x = xx
                case 'D':
                    yy = min(y + 1, SIZE)
                    if KEYPAD[yy][x]: y = yy
                case 'L':
                    xx = max(x - 1, 0)
                    if KEYPAD[y][xx]: x = xx
        code += KEYPAD[y][x]
    return code


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
