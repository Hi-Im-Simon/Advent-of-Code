# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-10.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    actions, values = {}, {}
    for line in f:
        line = line.split()
        if line[0] == 'value':
            if int(line[-1]) not in values:
                values[int(line[-1])] = set()
            values[int(line[-1])].add(int(line[1]))
        else:
            if int(line[1]) not in actions:
                actions[int(line[1])] = [0, 0]
            if line[5] == 'bot':
                actions[int(line[1])][0] = int(line[6])
            else:
                actions[int(line[1])][0] = -int(line[6]) - 1
            if line[10] == 'bot':
                actions[int(line[1])][1] = int(line[11])
            else:
                actions[int(line[1])][1] = -int(line[11]) - 1
    return actions, values


def part1_and_2(f, x=0, y=0, flag=False):
    actions, values = prep_input(f)
    DONE = False
    while not DONE:
        DONE = True
        for val in list(values):
            if len(values[val]) == 2:
                if not flag and x in values[val] and y in values[val]:
                    return val
                DONE = False
                if actions[val][0] not in values:
                    values[actions[val][0]] = set()
                values[actions[val][0]].add(min(values[val]))
                if actions[val][1] not in values:
                    values[actions[val][1]] = set()
                values[actions[val][1]].add(max(values[val]))
                del values[val]
    return min(values[-1]) * min(values[-2]) * min(values[-3])


print(f"part 1:\n{ part1_and_2(f, x=61, y=17) }")
print(f"part 2:\n{ part1_and_2(f, flag=True) }")
