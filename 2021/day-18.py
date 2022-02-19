from math import ceil
from shlex import join


tf = open('2021/inputs/input-00.txt')   # you can put an example input data here
f = open('2021/inputs/input-18.txt')    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    datas = [list(x.strip()) for x in f.readlines()]
    val_datas = []
    for i in range(len(datas)):
        depth = 0
        val_datas.append([])
        for char in datas[i]:
            if char == ',':
                continue
            elif char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            else:
                val_datas[i].append([depth, int(char)])
    return val_datas


def action_explode(data):
    for i, num in enumerate(data):
        if num[0] == 4:
            if i > 0:
                data[i-1][1] += data[i][1]
            if i + 1 < len(data) - 1:
                data[i+2][1] += data[i+1][1]
            data[i] = [data[i][0]-1, 0]
            del data[i+1]
            return data
    return 0


def action_split(data):
    for i, num in enumerate(data):
        if num[1] >= 10:
            data.insert(i+1, [num[0]+1, ceil(num[1] / 2)])
            data[i] = [num[0]+1, int(num[1] / 2)]  
            return data
    return 0


def to_snailfish(d1, d2):
    data = d1 + d2
    while True:
        out = action_explode(data)
        if type(out) == int:
            out = action_split(data)
            if type(out) == int:
                return data


def rec(data):
    for val in range(3, -1, -1):
        for i, el in enumerate(data):
            if el[0] == val:
                data[i] = [val-1, data[i][1] * 3 + data[i+1][1] * 2]
                del data[i+1]
    return data[0][1]
    
                

def part1(f):
    datas = prep_input(f)

    for _ in range(10):
        main_data = [x.copy() for x in datas[0]]
        for i in range(1, len(datas)):
            if i > 1:
                for j in range(len(main_data)):
                    main_data[j][0] += 1
            main_data = to_snailfish(main_data, [x.copy() for x in datas[i]])
            
    return rec(main_data)


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(tf) }")
print(f"part 2:\n{ part2(f) }")
