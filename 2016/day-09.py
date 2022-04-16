tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-09.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    return f[0]


def part1(f):
    data = prep_input(f)
    ans, i = 0, 0
    while i < len(data):
        if data[i] == '(':
            i += 1
            marker = ''
            while data[i] != ')':
                marker += data[i]
                i += 1
            x, y = map(int, marker.split('x'))
            ans += x * y
            i += x
        else:
            ans += 1
        i += 1
    return ans


def part2(f):
    data = prep_input(f)
    ans, i = 0, 0
    multips = []
    while i < len(data):
        if data[i] == '(':
            for m in multips: m[0] = max(m[0] - 1, 0)
            i += 1
            marker = ''
            while data[i] != ')':
                for m in multips: m[0] = max(m[0] - 1, 0)
                marker += data[i]
                i += 1
            for m in multips: m[0] = max(m[0] - 1, 0)
            multips.append(list(map(int, marker.split('x'))))
        else:
            clear_multips = [x.copy() for x in multips].copy()
            temp_ans = 1
            for m in multips:
                if m[0]:
                    temp_ans *= m[1]
                else:
                    clear_multips.remove(m)
            multips = clear_multips
            ans += temp_ans
            for m in multips: m[0] = max(m[0] - 1, 0)
        i += 1
        
    return ans


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
