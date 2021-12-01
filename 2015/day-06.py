tf = open('2015/inputs/input-00.txt').readlines()
f = [line.strip().split(' ') for line in open('2015/inputs/input-06.txt').readlines()]

for i in range(len(f)):
    if f[i][0] == 'turn':
        f[i] = f[i][1:3] + [f[i][4]]
    else:
        f[i] = f[i][:2] + [f[i][3]]


def grid1(f):
    grid = [[0 for _ in range(1000)] for _ in range(1000)] 

    for line in f:
        x1, y1 = [int(a) for a in line[1].split(',')]
        x2, y2 = [int(a) for a in line[2].split(',')]
        
        if line[0] == 'on':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    grid[y][x] = 1
        elif line[0] == 'off':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    grid[y][x] = 0
        else:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if grid[y][x] == 0:
                        grid[y][x] = 1
                    else:
                        grid[y][x] = 0
    return sum([sum(x) for x in grid])

def grid2(f):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in f:
        x1, y1 = [int(a) for a in line[1].split(',')]
        x2, y2 = [int(a) for a in line[2].split(',')]
        
        if line[0] == 'on':
            add = 1
        elif line[0] == 'off':
            add = -1
        else:
            add = 2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if grid[y][x] + add > 0:
                    grid[y][x] += add
                else:
                    grid[y][x] = 0
                
    return sum([sum(x) for x in grid])


print('part 1:\n' + str(grid1(f)))
print('part 2:\n' + str(grid2(f)))
