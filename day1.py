file = open('c:/Code/Advent of Code/2020/inputs/input1.txt').readlines()
file = [int(i[:-1]) for i in file]


def ch1(f):
    n = len(f)
    for i in range(n-1):
        for j in range(i+1, n):
            n1, n2 = f[i], f[j]
            if n1 + n2 == 2020:
                return n1 * n2


def ch2(f):
    n = len(f)
    for i in range(n-2):
        for j in range(1, n-1):
            n1, n2, n3 = f[i], f[j], 2020 - f[i] - f[j]
            if n3 in f:
                return n1 * n2 * n3


print(ch1(file))
print(ch2(file))
