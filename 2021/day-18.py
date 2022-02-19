tf = open('2021/inputs/input-00.txt')   # you can put an example input data here
f = open('2021/inputs/input-18.txt')    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    datas = [list(x.strip()) for x in f.readlines()]
    for data in datas:
        for i, char in enumerate(data):
            if char.isdigit():
                data[i] = int(char)
    return datas


def action_explode(data):
    depth = -1
    for i, char in enumerate(data):
        if char == ',':
            continue
        elif char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
            
        if depth == 4:
            start = i
            left, right = data[i+1], data[i+3]
            data[i] = 0
            del data[i+1:i+5]
            
            i -= 1
            while i > 0:
                if type(data[i]) == int:
                    data[i] += left
                    break
                i -= 1
            i = start + 1
            while i < len(data):
                if type(data[i]) == int:
                    data[i] += right
                    break
                i += 1
            break
    return data


def action_split(data):
    depth = -1
    for i, char in enumerate(data):
        if char == ',':
            continue
        elif char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        else:
            if char > 9:
                if char % 2 == 0:
                    data = data[:i] + ['[', data[i] // 2, ',', data[i] // 2, ']'] + data[i+1:]
                else:
                    data = data[:i] + ['[', data[i] // 2, ',', data[i] // 2 + 1, ']'] + data[i+1:]
                break
    return data


def to_snailfish(data):
    new, last = action_explode(data), ''
    while last != new:
        while last != new:
            last = new.copy()
            new = action_explode(new)
        last = new.copy()
        new = action_split(new)
    return new


def rec(data):
    if type(data[0]) == list:
        data[0] = rec(data[0])
    if type(data[1]) == list:
        data[1] = rec(data[1])
    return 3 * data[0] + 2 * data[1]
                

def part1(f):
    datas = prep_input(f)
    for _ in range(20):
        main_data = datas[0]
        
        i = 1
        while i < len(datas):
            # print('\t', ''.join([str(x) if type(x) == int else x for x in main_data]))
            # print('+\t', ''.join([str(x) if type(x) == int else x for x in datas[i]]))
            main_data = ['['] + main_data + [','] + datas[i] + [']']
            main_data = to_snailfish(main_data)
            # print('=\t', ''.join([str(x) if type(x) == int else x for x in main_data]))
            # print('\n')
            i += 1
        data = eval(''.join([str(x) if type(x) == int else x for x in main_data]))
        
        data = rec(data)
    
    return data


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
