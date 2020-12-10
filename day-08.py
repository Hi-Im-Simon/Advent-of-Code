
def ch1(i, activ, ans):
    instr = f[i]
    if activ[i] == 0:
        activ[i] = 1
        if instr[0] == 'nop': 
            return ch1(i+1, activ, ans)
        elif instr[0] == 'jmp':
            return ch1(i+instr[1], activ, ans)
        else:
            ans += instr[1]
            return ch1(i+1, activ, ans)
    else: return ans


def ch2_check(i, activ, ans, f):
    if i >= len(f): return ans
    instr = f[i]
    if activ[i] == 1: return False    
    else:
        activ[i] = 1
        if instr[0] == 'nop':
            return ch2_check(i+1, activ, ans, f)
        elif instr[0] == 'jmp':
            return ch2_check(i+instr[1], activ, ans, f)
        else:
            ans += instr[1]
            return ch2_check(i+1, activ, ans, f)


def ch2():
    ans = False
    for i in range(len(f)):
        if f[i][0] == 'nop':
            f_c = f.copy()
            f_c = f[:i] + [['jmp', f[i][1]]] + f[i+1:]
            ans = ch2_check(0, [0 for _ in range(len(f))], 0, f_c)
        elif f[i][0] == 'jmp':
            f_c = f.copy()
            f_c = f[:i] + [['nop', f[i][1]]] + f[i+1:]
            ans = ch2_check(0, [0 for _ in range(len(f))], 0, f_c)
        if ans != False:
            return ans

f = open('c:/Code/Advent of Code/2020/inputs/input8.txt').read().split('\n')
f = [[l.split()[0], int(l.split()[1])] for l in f]

print(ch1(0, [0 for _ in range(len(f))], 0))
print(ch2())