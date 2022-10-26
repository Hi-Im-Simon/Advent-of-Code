tf = open('2019/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2019/inputs/input-05.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [list(map(int, x.strip().split(','))) for x in f][0]
    return data


def part1(f, ID):
    data = prep_input(f)
    print(data)
    i = 0
    
    mode0, mode1 = 0, 0
    while data[i] != 99:
        print(data)
        if mode0: val0 = data[i+1]
        else: val0 = data[data[i+1]]
        if mode1: val1 = data[i+2]
        else: val1 = data[data[i+2]]
        
        if data[i] == 1:
            data[data[i+3]] = val0 + val1
            i += 4
        elif data[i] == 2:
            data[data[i+3]] = val0 * val1
            i += 4
        elif data[i] == 3:
            data[data[i+1]] = ID
            i += 2
        else:
            code = str(data[i])
            mode0, mode1 = int(code[1]), int(code[0])
            data[i] = int(code[3]) #NOPE
            continue
        mode0, mode1 = 0, 0
    return data[0]


def part2(f):
    for i in range(0, 100):
        for j in range(0, 100):
            if part1(f, i, j) == 19690720:
                return 100 * i + j


print(f"part 1:\n{ part1(f, 1) }")
# print(f"part 2:\n{ part2(f) }")
