# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-01.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = f[0].split(', ')
    return data


def part1(f):
    data = prep_input(f)    
    x, y = 0, 0
    facing = 0
    for comm in data:
        comm, dist = comm[0], int(comm[1:])
        match comm:
            case 'L': facing = (facing - 1) % 4
            case 'R': facing = (facing + 1) % 4
        match facing:
            case 0: y += dist
            case 1: x += dist
            case 2: y -= dist
            case 3: x -= dist
    return abs(x) + abs(y)


def part2(f):
    data = prep_input(f)
    visited = {(0, 0)}

    x, y = 0, 0
    facing = 0
    for comm in data:
        print(visited)
        comm, dist = comm[0], int(comm[1:])
        match comm:
            case 'L': facing = (facing - 1) % 4
            case 'R': facing = (facing + 1) % 4
        match facing:
            case 0:
                for yy in range(y+1, y+dist+1):
                    if (x, yy) in visited:
                        return abs(x) + abs(yy)
                    else:
                        visited.add((x, yy))
                y += dist
            case 1: 
                for xx in range(x+1, x+dist+1):
                    if (xx, y) in visited:
                        return abs(xx) + abs(y)
                    else:
                        visited.add((xx, y))
                x += dist
            case 2: 
                for yy in range(y-1, y-dist-1, -1):
                    if (x, yy) in visited:
                        return abs(x) + abs(yy)
                    else:
                        visited.add((x, yy))
                y -= dist
            case 3: 
                for xx in range(x-1, x-dist-1, -1):
                    if (xx, y) in visited:
                        return abs(xx) + abs(y)
                    else:
                        visited.add((xx, y))
                x -= dist


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
