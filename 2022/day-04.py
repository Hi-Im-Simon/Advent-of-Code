tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-04.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [[tuple(map(int, y.split('-'))) for y in x.strip().split(',')] for x in f]
    return data


def part1(f):
    data = prep_input(f)
    ans = 0
    
    for line in data:
        if ((
            line[1][0] <= line[0][0] <= line[1][1]
            and
            line[1][0] <= line[0][1] <= line[1][1]
            ) or (
            line[0][0] <= line[1][0] <= line[0][1]
            and
            line[0][0] <= line[1][1] <= line[0][1]
        )):
            ans += 1
    return ans


def part2(f):
    data = prep_input(f)
    ans = 0
    
    for line in data:
        if ((
            line[1][0] <= line[0][0] <= line[1][1]
            or
            line[1][0] <= line[0][1] <= line[1][1]
            ) or (
            line[0][0] <= line[1][0] <= line[0][1]
            or
            line[0][0] <= line[1][1] <= line[0][1]
        )):
            ans += 1
    return ans


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
