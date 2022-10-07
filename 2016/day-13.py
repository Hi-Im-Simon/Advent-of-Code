tf = [open('2016/inputs/input-00.txt').readlines(), (7, 4)]   # you can put an example input data here
f = [open('2016/inputs/input-13.txt').readlines(), (31, 39)]    # your input data

ans1 = float('inf')
fav_num = 0
end_point = (0, 0)
ans2 = 0
global_visited = set()


def prep_input(f):  # edit to adjust how the program reads your files
    global fav_num, end_point
    fav_num = int(f[0][0])
    end_point = f[1]


def rec(x, y, steps, visited):
    global ans1
    if (
        (x, y) in visited
        or
        x < 0 or y < 0
        or
        steps >= ans1
        or
        bin((((x + 3) * x + (2 * x * y) + (y + 1) * y) + fav_num)).count('1') % 2
    ):
        return
    steps += 1
    if (x, y) == end_point:
        if steps < ans1:
            ans1 = steps
        return
    visited.add((x, y))
    
    global global_visited, ans2
    if (x, y) not in global_visited and steps <= 50:
        global_visited.add((x, y))
        ans2 += 1
        
    
    rec(x + 1, y, steps, visited.copy())
    rec(x, y + 1, steps, visited.copy())
    rec(x - 1, y, steps, visited.copy())
    rec(x, y - 1, steps, visited.copy())
    
    
def part1(f):
    prep_input(f)    
    rec(1, 1, -1, set())
    return ans1


def part2(f):
    return ans2


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
