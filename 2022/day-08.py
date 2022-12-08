tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-08.txt').readlines()    # your input data


class Point:
    def __init__(self, h):
        self.h = h
        self.vis = [None, None, None, None]
    

def prep_input(f):  # edit to adjust how the program reads your files
    data = [list([Point(int(y)) for y in x.rstrip()]) for x in f]
    
    
    return data


def part1(f):
    data = prep_input(f)
    ans = len(data) * 4 - 4
    
    max_hs = [None, None, None, None]
    
    # set current max heights starting from each side
    for y in range(1, len(data)-1):
        max_hs[3] = data[y][0].h
        max_hs[1] = data[y][-1].h

        for x in range(1, len(data[y])-1):
            # left to right
            if data[y][x].h > max_hs[3]:
                data[y][x].vis[3] = True
                max_hs[3] = data[y][x].h
            else:
                data[y][x].vis[3] = False

            # right to left
            if data[y][-x-1].h > max_hs[1]:
                data[y][-x-1].vis[1] = True
                max_hs[1] = data[y][-x-1].h
            else:
                data[y][-x-1].vis[1] = False

    for x in range(1, len(data)-1):
        max_hs[0] = data[0][x].h
        max_hs[2] = data[-1][x].h

        for y in range(1, len(data[y])-1):
            # top to bottom
            if data[y][x].h > max_hs[0]:
                data[y][x].vis[0] = True
                max_hs[0] = data[y][x].h
            else:
                data[y][x].vis[0] = False

            # bottom to top
            if data[-y-1][x].h > max_hs[2]:
                data[-y-1][x].vis[2] = True
                max_hs[2] = data[-y-1][x].h
            else:
                data[-y-1][x].vis[2] = False
    
    for y in range(1, len(data)-1):
        for x in range(1, len(data[y])-1):
            if True in data[y][x].vis: ans += 1    
    return ans


def part2(f):
    data = prep_input(f)
    ans = 0
    
    for y in range(1, len(data)-1):
        for x in range(1, len(data[y])-1):
            dists = [1, 1, 1, 1]
            
            # check top
            ty = y - 1
            while ty > 0:
                if data[ty][x].h < data[y][x].h: dists[0] += 1
                else: break
                ty -= 1
            # check right
            tx = x + 1
            while tx < (len(data) - 1):
                if data[y][tx].h < data[y][x].h: dists[1] += 1
                else: break
                tx += 1
            # check bottom
            ty = y + 1
            while ty < (len(data) - 1):
                if data[ty][x].h < data[y][x].h: dists[2] += 1
                else: break
                ty += 1
            # check left
            tx = x - 1
            while tx > 0:
                if data[y][tx].h < data[y][x].h: dists[3] += 1
                else: break
                tx -= 1
            ans = max(ans, dists[0]*dists[1]*dists[2]*dists[3])
    return ans


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
