f = open('2019/inputs/input-03.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip().split(',').copy() for x in f]
    coords = [[(0, 0, 0)], [(0, 0, 0)]]
    for c in range(len(coords)):
        path_len = 0
        for i, el in enumerate(data[c]):
            path_len += int(el[1:])
            if c == 0 and i == 0:
                orientation0 = 'vert' if el[0] in ['U', 'D'] else 'horiz'
            elif c == 1 and i == 0:
                orientation1 = 'vert' if el[0] in ['U', 'D'] else 'horiz'
            if el[0] == 'U':
                coords[c].append((coords[c][i][0], coords[c][i][1] + int(el[1:]), path_len))
            elif el[0] == 'R':
                coords[c].append((coords[c][i][0] + int(el[1:]), coords[c][i][1], path_len))
            elif el[0] == 'D':
                coords[c].append((coords[c][i][0], coords[c][i][1] - int(el[1:]), path_len))
            elif el[0] == 'L':
                coords[c].append((coords[c][i][0] - int(el[1:]), coords[c][i][1], path_len))
    return coords[0], coords[1], orientation0, orientation1


def part1(f, end_on_first = False):
    ans = float('inf')
    line0, line1, or0, or1 = prep_input(f)
    skip = 0 if or0 == or1 else 1
    
    for i in range(len(line0) - 1):
        skip = not skip
        for j in range(skip, len(line1) - 1, 2):
            if line0[i][0] == line0[i+1][0]:
                if min([line0[i][1], line0[i+1][1]]) <= line1[j][1] <= max([line0[i][1], line0[i+1][1]]) and min([line1[j][0], line1[j+1][0]]) <= line0[i][0] <= max([line1[j][0], line1[j+1][0]]):
                    temp_ans = abs(line1[j][1]) + abs(line0[i][0])
                    if temp_ans > 0:
                        if end_on_first: return line0[i][2] + line1[j][2] + abs(line1[j][1] - line0[i][1]) + abs(line0[i][0] - line1[j][0])
                        if temp_ans < ans: ans = temp_ans
            else:
                if min([line0[i][0], line0[i+1][0]]) <= line1[j][0] <= max([line0[i][0], line0[i+1][0]]) and min([line1[j][1], line1[j+1][1]]) <= line0[i][1] <= max([line1[j][1], line1[j+1][1]]):
                    temp_ans = abs(line1[j][0]) + abs(line0[i][1])
                    if temp_ans > 0:
                        if end_on_first: return line0[i][2] + line1[j][2] + abs(line0[i][0] - line1[j][0]) + abs(line1[j][1] - line0[i][1])
                        if temp_ans < ans: ans = temp_ans
    return ans


def part2(f):
    return part1(f, end_on_first=True)


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
