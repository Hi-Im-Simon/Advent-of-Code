tf = [list(map(int, list(x.strip()))) for x in open('2021/inputs/input-00.txt').readlines()]
f = [list(map(int, list(x.strip()))) for x in open('2021/inputs/input-11.txt').readlines()]


def prep_input(f):
    for i, line in enumerate(f):
        f[i] = [-2] + line + [-2]
    f.insert(0, [-2 for _ in range(len(f[0]))])
    f.append([-2 for _ in range(len(f[0]))])
    return f


def rec(x, y):
    global oct_map
    if oct_map[y][x] in [-2, -1]:
        return
    elif oct_map[y][x] == 9:
        oct_map[y][x] = -1
        global flashes, sync_flashes
        flashes += 1
        sync_flashes += 1
        for xy in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
            rec(x + xy[0], y + xy[1])
    else:
        oct_map[y][x] += 1
        
    

def part1_and_2(steps):
    global oct_map, sync_flashes
    if steps == '?':
        steps = 9999999999
    for i in range(steps):
        sync_flashes = 0
        for y in range(1, len(oct_map)-1):
            for x in range(1, len(oct_map[y])-1):
                rec(x, y)
        for y in range(len(oct_map)):
            for x in range(len(oct_map[y])):
                if oct_map[y][x] == -1:
                    oct_map[y][x] = 0
        if sync_flashes == 100:
            return i + 1
    return flashes


oct_map = prep_input(f)
oct_map_cop = [x.copy() for x in oct_map.copy()]
flashes, sync_flashes = 0, 0

print(f"part 1:\n{ part1_and_2(steps=100) }")
oct_map = oct_map_cop
print(f"part 2:\n{ part1_and_2(steps='?') }")
