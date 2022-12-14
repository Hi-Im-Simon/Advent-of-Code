tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-14.txt').readlines()    # your input data


def prep_input(f, add_floor = False):  # edit to adjust how the program reads your files
    data = []
    new_line = [0 for _ in range(1000)]
    for line in f:
        line = [tuple(map(int, x.split(','))) for x in line.rstrip().split(' -> ')]
        for i in range(len(line) - 1):
            while len(data) <= max(line[i][1], line[i+1][1]):
                data.append(new_line.copy())
            xs = sorted([line[i][0], line[i+1][0]])
            xs[1] += 1
            ys = sorted([line[i][1], line[i+1][1]])
            ys[1] += 1
            for x in range(*xs):
                for y in range(*ys):
                    data[y][x] = 1
    if add_floor:
        data.append(new_line.copy())
        data.append([1 for _ in range(1000)])
    return data


def add_sand(data, x, y):
    while y < len(data)-1:
        if not data[y+1][x]:
            y += 1
        elif not data[y+1][x-1]:
            x -= 1
            y += 1
        elif not data[y+1][x+1]:
            x += 1
            y += 1
        else:
            data[y][x] = 1
            return data
    return False


def part1(f):
    data = prep_input(f)
    i = 0
    while add_sand(data, *(500, 0)):
        i += 1
    return i


def part2(f):
    data = prep_input(f, True)
    i = 0
    while not data[0][500]:
        add_sand(data, *(500, 0))
        i += 1
    return i


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
