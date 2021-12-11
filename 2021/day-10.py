# tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-10.txt').readlines()]


def prep_input(f):
    for i, line in enumerate(f):
        f[i] = list(line)
        for j, el in enumerate(line):
            match el:
                case '<': f[i][j] = -4
                case '{': f[i][j] = -3
                case '[': f[i][j] = -2
                case '(': f[i][j] = -1
                case ')': f[i][j] = 1
                case ']': f[i][j] = 2
                case '}': f[i][j] = 3
                case '>': f[i][j] = 4
    return f


def part1(f):
    nav_sys = prep_input(f)
    ans = 0
    for line in nav_sys:
        mem = []
        for char in line:
            if char < 0:
                mem.append(char)
            else:
                if mem[-1] == -char:
                    mem.pop()
                else:
                    ans += illegal_table[char]
                    break
    return ans


def part2(f):
    nav_sys = prep_input(f)
    new_nav_sys = []
    for line in nav_sys:
        mem = []
        for char in line:
            if char < 0:
                mem.append(char)
            else:
                if mem[-1] == -char:
                    mem.pop()
                else:
                    break
        else:
            new_nav_sys.append(line)
    
    scores = []
    for line in new_nav_sys:
        mem = []
        for char in line:
            if char < 0:
                mem.append(char)
            else:
                mem.pop()
        mem = mem[::-1]
        score = 0
        for el in mem:
            score = score * 5 - el
        scores.append(score)
    return sorted(scores)[len(scores) // 2]


illegal_table = {
    1: 3,
    2: 57,
    3: 1197,
    4: 25137
}

print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
