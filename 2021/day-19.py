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
    ref_data = []
    
    for s, scanner in enumerate(data):
        ref_data.append([])
        for i in range(len(scanner) - 1):
            for j in range(i + 1, len(scanner)):
                ref_data[s].append([scanner[j][x] - scanner[i][x] for x in range(3)])
    # we have an array of relative placements of all elements to each other
    cur = 0
    available = [x for x in range(1, len(data))]
    options = [(-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1), (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)]
    order_options = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    
    while len(available):
        for other in available:
            for order_option in order_options:
                for option in options:
                    count = 0
                    for line in ref_data[other]:
                        line = [line[x] for x in order_option]
                        line = [line[i] * option[i] for i in range(3)]
                        if line in ref_data[cur]:
                            print(line)
                            count += 1
                    print(count)
                    if count > 0:
                        return
                
            return
    
    return ref_data


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(tf) }")
print(f"part 2:\n{ part2(f) }")
