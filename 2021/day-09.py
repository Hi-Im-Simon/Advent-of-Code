# tf = [list(map(int, list(x.strip()))) for x in open('2021/inputs/input-00.txt').readlines()]
f = [list(map(int, list(x.strip()))) for x in open('2021/inputs/input-09.txt').readlines()]


def prep_input(heatmap):
    for line in heatmap:
        line.insert(0, 'x')
        line.append('x')
    heatmap.insert(0, ['x' for _ in range(len(heatmap[0]))])
    heatmap.append(['x' for _ in range(len(heatmap[0]))])
    return heatmap


def part1(f):
    ans = 0
    heatmap = prep_input(f)
    for y in range(1, len(heatmap)-1):
        for x in range(1, len(heatmap[y])-1):
            val = heatmap[y][x]
            if heatmap[y-1][x] != 'x' and heatmap[y-1][x] <= val:
                continue
            if heatmap[y][x+1] != 'x' and heatmap[y][x+1] <= val:
                continue
            if heatmap[y+1][x] != 'x' and heatmap[y+1][x] <= val:
                continue
            if heatmap[y][x-1] != 'x' and heatmap[y][x-1] <= val:
                continue
            ans += 1 + val
    return ans


def rec(heatmap, x, y):
    global searched
    if x * 100 + y in searched:
        return 0
    searched.add(x * 100 + y)
    
    size = 1
    if heatmap[y-1][x] not in ['x', 9]:
        size += rec(heatmap, x, y-1)
    if heatmap[y][x+1] not in ['x', 9]:
        size += rec(heatmap, x+1, y)
    if heatmap[y+1][x] not in ['x', 9]:
        size += rec(heatmap, x, y+1)
    if heatmap[y][x-1] not in ['x', 9]:
        size += rec(heatmap, x-1, y)
    return size


def part2(f):
    sizes = []
    heatmap = prep_input(f)
    for y in range(1, len(heatmap)-1):
        for x in range(1, len(heatmap[y])-1):
            if heatmap[y][x] != 9:
                basin = rec(heatmap, x, y)
                if basin > 0:
                    sizes.append(basin)
    ans = 1
    for el in sorted(sizes)[::-1][:3]:
        ans *= el
    return ans


searched = set()

print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
