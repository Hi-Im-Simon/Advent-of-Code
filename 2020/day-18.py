file = open('2020/inputs/input-18.txt')
f = [x.strip() for x in file.readlines()]


def skipBrackets(eq, x):
    pars, i = eq[x].count('('), x
    while pars != 0:
        i += 1
        pars += eq[i].count('(')
        pars -= eq[i].count(')')
    l = [eq[x][1:]] + eq[x + 1:i] + [eq[i][:-1]]
    del eq[x + 1:i + 1]
    eq[x] = str(calc(l))
    return eq
    

def calc(eq):
    ans = 0
    while len(eq) > 1:
        if '(' in eq[0]:
            eq = skipBrackets(eq, 0)
        elif '(' in eq[2]:
            eq = skipBrackets(eq, 2)
        else:
            if eq[1] == '+':
                eq = [str(int(eq[0]) + int(eq[2]))] + eq[3:]
            elif eq[1] == '*':
                eq = [str(int(eq[0]) * int(eq[2]))] + eq[3:]
    return int(eq[0])


def math(file):
    ans = 0
    for eq in file:
        ans += calc(eq.split())
    return ans


def toRevMath(file):
    ans = 0
    for eq in file:
        eq = eq.split()
        for i in range(1, len(eq) - 1):
            if eq[i] == '+':
                j = i
                if ')' in eq[i - 1]:
                    pars = eq[i - 1].count(')')
                    i -= 1
                    while pars > 0:
                        i -= 1
                        pars -= eq[i].count('(')
                        pars += eq[i].count(')')
                    eq[i] = '(' + eq[i]
                else:
                    eq[i - 1] = '(' + eq[i - 1]
                if '(' in eq[j + 1]:
                    pars = eq[j + 1].count('(')
                    j += 1
                    while pars > 0:
                        j += 1
                        pars += eq[j].count('(')
                        pars -= eq[j].count(')')
                    eq[j] = eq[j] + ')'
                else:
                    eq[j + 1] = eq[j + 1] + ')'
        ans += calc(eq)
    return ans


print(math(f))
print(toRevMath(f))

file.close()
