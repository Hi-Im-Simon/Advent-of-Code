file = open('2020/inputs/input-08.txt')
f = [[x.strip().split(' ')[0], int(x.strip().split(' ')[1])] for x in file.readlines()]


def game_debugger(file):
    pastInstr = []
    i, acc = 0, 0
    while i not in pastInstr:
        pastInstr.append(i)
        instr, val = file[i]
        if instr == 'acc':
            acc += val
            i += 1
        elif instr == 'jmp':
            i += val
        else:
            i += 1
    return acc


def game_deep_debugger(file):
    for j in range(len(file)):
        if file[j][0] == 'nop':
            file[j][0] = 'jmp'
        elif file[j][0] == 'jmp':
            file[j][0] = 'nop'
        else:
            continue
        pastInstr = []
        i, acc = 0, 0
        while i not in pastInstr:
            if i == len(file):
                return acc
            elif i > len(file):
                continue
            else:
                pastInstr.append(i)
                instr, val = file[i]            
                if instr == 'acc':
                    acc += val
                    i += 1
                elif instr == 'jmp':
                    i += val
                else:
                    i += 1
        if file[j][0] == 'nop':
            file[j][0] = 'jmp'
        elif file[j][0] == 'jmp':
            file[j][0] = 'nop'


print(game_debugger(f))
print(game_deep_debugger(f))

file.close()
