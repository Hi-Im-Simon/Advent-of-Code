tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-13.txt').readlines()]


def prep_input(f):
    dots, folds = [], []
    wr = 0
    for line in f:
        if line == '':
            wr = 1
        elif wr:
            temp = line.split()[2].split('=')
            folds.append(tuple([temp[0], int(temp[1])]))
        else:
            dots.append(tuple([int(x) for x in line.split(',')]))
    return dots, folds


def part1_and_2(f, num_of_folds='all'):
    dots, folds = prep_input(f)
    paper_size_x, paper_size_y = max([x[0] for x in dots]) + 1, max([x[1] for x in dots]) + 1
    instr = [[0 for _ in range(paper_size_x)] for _ in range(paper_size_y)]
    if num_of_folds != 'all':
        folds = folds[:num_of_folds]
    for d in dots:
        instr[d[1]][d[0]] = 1
    for fold in folds:
        if fold[0] == 'y':
            if len(instr[fold[1]+1:]) == len(instr[:fold[1]]):
                to_fold = [x.copy() for x in instr[fold[1]+1:]][::-1]
            else:
                to_fold = [x.copy() for x in instr[fold[1]+1:]][::-1]
                to_fold.insert(0, [0 for _ in range(len(to_fold[0]))])
            instr = instr[:fold[1]]
        elif fold[0] == 'x':
            if len(instr[0][fold[1]+1:]) == len(instr[0][:fold[1]]):
                to_fold = [x[fold[1]+1:].copy()[::-1] for x in instr]
            else:
                to_fold = [[0] + x[fold[1]+1:].copy()[::-1] for x in instr]
            instr = [x[:fold[1]] for x in instr]
        for y in range(len(instr)):
            for x in range(len(instr[y])):
                instr[y][x] += to_fold[y][x]
    
    ans = 0
    for line in instr:
        for dot in line:
            if dot > 0:
                ans += 1
    if num_of_folds == 'all':
        for y in range(len(instr)):
            for x in range(len(instr[y])):
                if instr[y][x] == 0:
                    instr[y][x] = '.'
                else:
                    instr[y][x] = '#'
        return instr
    return ans


print(f"part 1:\n{ part1_and_2(f, 1) }")
print(f"part 2:")
[print(''.join(x)) for x in part1_and_2(f)]
