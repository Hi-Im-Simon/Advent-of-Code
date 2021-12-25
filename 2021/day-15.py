# tf = [list(map(int, list(x.strip()))) for x in open('2021/inputs/input-00.txt').readlines()]
f = [list(map(int, list(x.strip()))) for x in open('2021/inputs/input-15.txt').readlines()]


def prep_input(f):
    risk_map = [[0] + x + [0] for x in f]
    risk_map.insert(0, [0 for _ in range(len(risk_map[0]))])
    risk_map.append([0 for _ in range(len(risk_map[0]))])
    risk_map[1][1] = 0
    return risk_map


def part1(f):
    risk_map = prep_input(f)
    y, x = 1, 1
    min_paths = {(y, x): 0}
    while x != len(risk_map) - 2 or y != len(risk_map) - 2:
        for yx in [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]:
            val = risk_map[yx[0]][yx[1]]
            if val > 0:
                if yx in min_paths:
                    min_paths[yx] = min(min_paths[(y, x)] + val, min_paths[yx])
                else:
                    min_paths[yx] = min_paths[(y, x)] + val
        del min_paths[(y, x)]
        risk_map[y][x] = 0
        y, x = min(min_paths, key=min_paths.get)
    return min_paths[(y, x)]


def part2(f): 
    size = len(f)
    [f.append([]) for _ in range(size * 4)]
    for m in range(1, 5):
        for y in range(size):
            f[size * m + y] = [el + m if el + m < 10 else el + m - 9 for el in f[y][:size]]
    new_size = len(f)
    for y in range(new_size):
        for x in range(4):
            f[y] += [i + x + 1 if i + x + 1 < 10 else i + x - 8 for i in f[y][:size]]
    return part1(f)


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }") # part 2 takes a few seconds
