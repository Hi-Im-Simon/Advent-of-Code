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


def part2(f):
    data = prep_input(f)
    edges = dict()
    
    def add(coords):
        if 0 <= coords[0] <= 4_000_000 and 0 <= coords[1] <= 4_000_000:
            if coords not in edges:
                edges[coords] = 1
            else:
                edges[coords] += 1
    
    for line in data:
        border_dist = abs(line[0] - line[2]) + abs(line[1] - line[3]) + 1
        for i in range(border_dist):
            dist = (border_dist - i)
            coords = [
                (line[0] + i, line[1] - dist),
                (line[0] - dist, line[1] - i),
                (line[0] - i, line[1] + dist),
                (line[0] + dist, line[1] + i)
            ]
            for coord in coords:
                add(coord)
    choices = set()
    for edge in edges:
        if edges[edge] >= 4:
            choices.add(edge)
            
    for choice in choices.copy():
        for line in data:
            # check if choice is still in set during its iteration
            if choice in choices:
                dist_s_to_b = abs(line[0] - line[2]) + abs(line[1] - line[3])
                dist_s_to_point = abs(line[0] - choice[0]) + abs(line[1] - choice[1])
                if dist_s_to_b >= dist_s_to_point:
                    choices.remove(choice)
            else: break
    ans = list(choices)[0]
    return ans[0] * 4000000 + ans[1]


print(f"part 1:\n{ part1(f, 2000000) }")
print(f"part 2:\n{ part2(f) }")
