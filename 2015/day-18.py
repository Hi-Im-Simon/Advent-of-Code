# tf = [x.strip() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2015/inputs/input-18.txt').readlines()]


def prep_input(f, stuck=False):
    grid = []
    for y in range(len(f)):
        grid.append([0])
        for x in range(len(f[y])):
            grid[y].append(1) if f[y][x] == '#' else grid[y].append(0)
        grid[y].append(0)
    if stuck:
        grid[0][1] = 1
        grid[0][-2] = 1
        grid[-1][1] = 1
        grid[-1][-2] = 1
    grid.insert(0, [0] * len(grid[0]))
    grid.append([0] * len(grid[0]))
    return grid


def part1_and_2(f, t, stuck=False):
    grid = prep_input(f, stuck)
    for _ in range(t):
        new_grid = [row.copy() for row in grid.copy()]
        for y in range(1, len(grid)-1):
            for x in range(1, len(grid[y])-1):
                neigh_c = sum([grid[y+1][x], grid[y+1][x+1], grid[y][x+1], grid[y-1][x+1], grid[y-1][x], grid[y-1][x-1], grid[y][x-1], grid[y+1][x-1]])
                if grid[y][x]:
                    if neigh_c not in [2, 3] and not (x == 1 and y == 1 or x == len(grid[y])-2 and y == len(grid[y])-2 or x == 1 and y == len(grid[y])-2 or x == len(grid[y])-2 and y == 1):
                        new_grid[y][x] = 0
                else:
                    if neigh_c == 3:
                        new_grid[y][x] = 1
        grid = new_grid
    return sum([sum(line) for line in grid])


print('part 1:\n' + str(part1_and_2(f, 100)))
print('part 2:\n' + str(part1_and_2(f, 100, stuck=True)))
