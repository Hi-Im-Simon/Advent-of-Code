# because otherwise the file gets edited in part1() for absolutely no reason
def read_file():
    return [x.strip().split(' | ') for x in open('2021/inputs/input-08.txt').readlines()]


def part1():
    f = read_file()
    ans = 0
    ts = {8: 'abcdefg', 7: 'acf', 4: 'bcdf', 1: 'cf'}
    # for every line with file
    for line in f:
        line[1] = line[1].split()
        # for every digit after |
        for el in line[1]:
            el_len = len(el)
            for t in ts.values():
                if el_len == len(t):
                    ans += 1
    return ans


def get_info(line):
    info = {1: '', 4: '', 7: ''}
    for el in line:
        if len(el) == 2:
            info[1] = el
        elif len(el) == 4:
            info[4] = el
        elif len(el) == 3:
            info[7] = el
    return info
            
            
def what_digit(el, info):
    if len(el) == 2:
        return '1'
    elif len(el) == 4:
        return '4'
    elif len(el) == 3:
        return '7'
    elif len(el) == 7:
        return '8'
    else:
        for p in info[1]:
            if p not in el: in_1 = False; break
        else: in_1 = True
        for p in info[4]:
            if p not in el: in_4 = False; break
        else: in_4 = True
        for p in info[7]:
            if p not in el: in_7 = False; break
        else: in_7 = True
        
        # 2, 3, 5 - 5
        if len(el) == 5:
            if in_1 == True or in_7 == True:
                return '3'
            to_4 = 0
            for p in info[4]:
                if p not in el:
                    to_4 += 1
            if to_4 == 1:
                return '5'
            else:
                return '2'
            
        # 0, 6, 9 - 6
        elif len(el) == 6:
            if in_4 == True:
                return '9'
            if in_1 == True or in_7 == True:
                to_4 = 0
                for p in info[4]:
                    if p not in el:
                        to_4 += 1
                if to_4 == 0:
                    return '9'
                else:
                    return '0'
            return '6'
        return '0'


def part2():
    f = read_file()
    ans = 0
    # for every line with file
    for line in f:
        line_ans = ''
        info = get_info(line[0].split() + line[1].split())
        line = line[1].split()
        # for every digit after |
        for el in line:
            line_ans += what_digit(el, info)
        ans += int(line_ans)
    return ans


print(f"part 1:\n{ part1() }")
print(f"part 2:\n{ part2() }")
