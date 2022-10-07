# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-12.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip().split() for x in f]
    return data


def is_number(x):
    if x.isdigit() or x[0] == '-' and x[1:].isdigit():
        return True
    return False


def solve(f, vars):
    data = prep_input(f)
    i = 0
    
    while i < len(data):
        line = data[i]
        if line[0] == 'cpy':
            if is_number(line[1]):
                vars[line[2]] = int(line[1])
            else:
                vars[line[2]] = vars[line[1]]
        elif line[0] == 'inc':
            vars[line[1]] += 1
        elif line[0] == 'dec':
            vars[line[1]] -= 1
        elif line[0] == 'jnz':
            if is_number(line[1]) and int(line[1]) != 0 or line[1] in vars and vars[line[1]] != 0:
                if is_number(line[2]):
                    i += int(line[2])
                else:
                    i += vars[line[2]]
                continue
        i += 1
    return vars['a']


print(f"part 1:\n{ solve(f, { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }) }")
print(f"part 2:\n{ solve(f, { 'a': 0, 'b': 0, 'c': 1, 'd': 0 }) }")
