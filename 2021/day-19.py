from math import sqrt


tf = open('2021/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2021/inputs/input-19.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    out = []
    i = -1
    for line in data:
        if line[0:3] == '---':
            i += 1
            out.append([])
        elif line == '':
            continue
        else:
            out[i].append([int(x) for x in line.split(',')])
    return out


def part1(f):
    data = prep_input(f)
    data_tree = []
    
    for s, scanner in enumerate(data):
        data_tree.append({})
        for i in range(len(scanner)):
            data_tree[s][i] = {}
            for j in range(len(scanner)):
                 if i != j:
                    x, y, z = [abs(scanner[i][t] - scanner[j][t]) for t in range(3)]
                    data_tree[s][i][j] = sqrt(y**2 + sqrt(x**2 + z**2)**2)
    
    # compare each scanner with each
    for s0 in range(len(data_tree) - 1):
        for s1 in range(s0 + 1, len(data_tree)):
            # for each element in scanner 0
            for el0 in data_tree[s0].values():
                # for each element in scanner 1
                for el1 in data_tree[s1].values():
                    count = 0
                    # for each line between 2 points in element 0
                    for line0 in el0.values():
                        # if the same line size exists in element 1
                        if line0 in el1.values():
                            count += 1
                    if count >= 11:
                        print(s0, s1)
                        print(count)
    return


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(tf) }")
print(f"part 2:\n{ part2(f) }")
