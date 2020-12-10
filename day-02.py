file = open('c:/Code/Advent of Code/2020/inputs/input-02.txt').readlines()
file = [[x for x in file[i].split()] for i in range(len(file))]
for i in range(len(file)):
    file[i] = [int(x) for x in file[i][0].split('-')] + [file[i][1][0]] + [file[i][2]]


def ch1(f):
    ans = 0
    for i in range(len(f)):
        if f[i][0] <= f[i][3].count(f[i][2]) <= f[i][1]:
            ans += 1
    return ans


def ch2(f):
    ans = 0
    for i in range(len(f)):
        if (f[i][3][f[i][0]-1] == f[i][2]) != (f[i][3][f[i][1]-1] == f[i][2]):
            ans += 1
    return ans


print(ch1(file))
print(ch2(file))
