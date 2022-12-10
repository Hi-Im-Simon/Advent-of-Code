tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-10.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.rstrip().split() for x in f]
    for i in range(len(data)):
        if len(data[i]) > 1:
            data[i][1] = int(data[i][1])
    return data


def part1(f):
    global X, sig_str
    data = prep_input(f)
    
    def add_cycle():
        global cycle, X, sig_str
        cycle += 1
        if (cycle+20) % 40 == 0:
            sig_str += X * cycle
    
    for line in data:
        if len(line) > 1:
            add_cycle()
            X += line[1]
            add_cycle()
        else:
            add_cycle()
    return sig_str


def part2(f):
    global X
    data = prep_input(f)
    
    def add_cycle():
        global cycle, X
        if not cycle % 41:
            cycle %= 40
            print()
        cycle += 1
        if cycle in [X + 1, X + 2, X + 3]:
            print('#', end='')
        else:
            print('.', end='')
    
    for line in data:
        if len(line) > 1:
            add_cycle()
            add_cycle()
            X += line[1]
        else:
            add_cycle()
    print()
    return None


cycle, X, sig_str = 1, 1, 0
print(f"part 1:\n{ part1(f) }")
cycle, X = 1, 1
print(f"part 2:\n{ part2(f) }")
