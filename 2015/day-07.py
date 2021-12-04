tf = [x.strip().split() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip().split() for x in open('2015/inputs/input-07.txt').readlines()]


def operation_neg(val, bit):
    val = bin(val)[2:]
    val = '0' * (bit - len(val)) + val
    return int(val.replace('0', '2').replace('1', '0').replace('2', '1'), 2)


def make_operations(f, vals={}):
    f = f.copy()
    while f:
        for line in f.copy():
            if line[1] == '->' and (line[0] in vals or line[0].isdigit()):
                vals[line[2]] = int(line[0]) if line[0].isdigit() else vals[line[0]]
            elif line[1] == 'AND' and (line[0] in vals or line[0].isdigit()) and (line[2] in vals or line[2].isdigit()):
                vals[line[4]] = [int(line[0]) if line[0].isdigit() else vals[line[0]]][0] & [int(line[2]) if line[2].isdigit() else vals[line[2]]][0]
            elif line[1] == 'OR' and (line[0] in vals or line[0].isdigit()) and (line[2] in vals or line[2].isdigit()):
                vals[line[4]] = [int(line[0]) if line[0].isdigit() else vals[line[0]]][0] | [int(line[2]) if line[2].isdigit() else vals[line[2]]][0]
            elif line[1] == 'LSHIFT' and (line[0] in vals or line[0].isdigit()) and (line[2] in vals or line[2].isdigit()):
                vals[line[4]] = [int(line[0]) if line[0].isdigit() else vals[line[0]]][0] << [int(line[2]) if line[2].isdigit() else vals[line[2]]][0]
            elif line[1] == 'RSHIFT' and (line[0] in vals or line[0].isdigit()) and (line[2] in vals or line[2].isdigit()):
                vals[line[4]] = [int(line[0]) if line[0].isdigit() else vals[line[0]]][0] >> [int(line[2]) if line[2].isdigit() else vals[line[2]]][0]
            elif line[0] == 'NOT' and (line[1] in vals or line[1].isdigit()):
                vals[line[3]] = operation_neg(vals[line[1]], 16)
            else:
                continue
            f.remove(line)
    return vals


def make_operations_set_b(f, b):
    f = f.copy()
    for line in f:
        if line[1] == '->' and line[2] == 'b':
            f.remove(line)
    vals = make_operations(f, vals={'b': b})
    return vals

            
a = make_operations(f)['a']
print('part 1:\n' + str(a))
print('part 2:\n' + str(make_operations_set_b(f, a)['a']))
