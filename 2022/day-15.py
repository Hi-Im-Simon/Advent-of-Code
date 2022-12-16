import sys
sys.setrecursionlimit(10000000)

tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-15.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = []
    for line in f:
        line = line.rstrip().split()
        data.append(tuple([int(x.split('=')[1].strip(',').strip(':')) for x in line if '=' in x]))
    return data


def part1(f, line_num):
    data = prep_input(f)
    ans_line = set()
    
    for l in data:
        dist = abs(l[0] - l[2]) + abs(l[1] - l[3])
        if abs(l[1] - line_num) <= dist:
            arm_len = dist - abs(l[1] - line_num)
            ans_line.add(l[0])
            for i in range(1, arm_len + 1):
                ans_line.add(l[0] + i)
                ans_line.add(l[0] - i)
    for l in data:
        if l[3] == line_num and l[2] in ans_line:
            ans_line.remove(l[2])
    return len(ans_line)


def generate(data):
    view = [[0] * 4000000]
    return view


def part2(f):
    data = prep_input(f)
    
    view = generate(data)

    return view


print(f"part 1:\n{ part1(f, 2000000) }")
print(f"part 2:\n{ part2(f) }")
