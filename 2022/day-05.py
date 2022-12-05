tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-05.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    stacks, commands = [], []
    break_flag = False
    for line in f:
        if not break_flag:
            if line.strip() == '': break_flag = True
            else:
                if not line[1] == '1':
                    for i in range(len(line) // 4):
                        if len(stacks)-1 < i: stacks.append([])
                        if line[i*4+1] != ' ':
                            stacks[i] += line[i*4+1]
        else:
            line = (line.strip().replace('move ', '').replace(' from ', ' ').replace(' to ', ' ').split(' '))
            commands.append([int(line[0]), int(line[1]) - 1, int(line[2]) - 1])
    return stacks, commands


def part1(f):
    stacks, commands = prep_input(f)
    for com in commands:
        for _ in range(com[0]):
            stacks[com[1]], stacks[com[2]] = stacks[com[1]][1:], stacks[com[1]][:1] + stacks[com[2]]
    return ''.join([stack[0] for stack in stacks])


def part2(f):
    stacks, commands = prep_input(f)
    for com in commands:
        stacks[com[1]], stacks[com[2]] = stacks[com[1]][com[0]:], stacks[com[1]][:com[0]] + stacks[com[2]]
    return ''.join([stack[0] for stack in stacks])


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
