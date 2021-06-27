def occupied_count(f, i, j, state):
    ans = 0
    if f[i-1][j-1] == state: ans += 1
    if f[i-1][j] == state: ans += 1
    if f[i-1][j+1] == state: ans += 1
    if f[i][j-1] == state: ans += 1
    if f[i][j+1] == state: ans += 1
    if f[i+1][j-1] == state: ans += 1
    if f[i+1][j] == state: ans += 1
    if f[i+1][j+1] == state: ans += 1
    return ans


def ch1(f):
    temp = [list(x) for x in f.copy()]
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == 'L':
                if occupied_count(f, i, j, '#') == 0:
                    temp[i][j] = '#'
            elif f[i][j] == '#':
                if occupied_count(f, i, j, '#') >= 4:
                    temp[i][j] = 'L'
    if temp != f: return ch1(temp)
    else: return sum([''.join(x).count('#') for x in f])
    

file = ['.' + x + '.' for x in open('c:/Code/Advent of Code/2020/inputs/input-11.txt').read().split('\n')]
file = [list(x) for x in ['.' * (len(file[0]))] + file + ['.' * (len(file[0]))]]

print(ch1(file))
