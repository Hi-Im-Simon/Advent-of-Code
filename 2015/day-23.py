#tf = open('2015/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2015/inputs/input-23.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.split() for x in f]
    for line in data:
        if len(line) == 3:
            line[1], line[2] = line[1].strip(','), int(line[2])
        elif line[1][0] in ['+', '-']:
            line[1] = int(line[1])
    return data


def part1_and_2(f, a=0, b=0):
    data = prep_input(f)
    
    regs = {'a': a, 'b': b}
    i = 0

    while i < len(data):
        match data[i][0]:
            case 'inc':
                regs[data[i][1]] += 1
            case 'hlf':
                regs[data[i][1]] //= 2
            case 'tpl':
                regs[data[i][1]] *= 3
            case 'jmp':
                i += data[i][1]
                continue
            case 'jie':
                if not regs[data[i][1]] % 2:
                    i += data[i][2]
                    continue
            case 'jio':
                if regs[data[i][1]] == 1:
                    i += data[i][2]
                    continue
        i += 1
    return regs['b']


print(f"part 1:\n{ part1_and_2(f) }")
print(f"part 2:\n{ part1_and_2(f, 1, 0) }")
