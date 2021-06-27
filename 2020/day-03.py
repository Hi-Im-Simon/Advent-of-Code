file = open('c:/Code/Advent of Code/2020/inputs/input-03.txt').readlines()
file = [x.strip() for x in file]
file = [x * int(7 * (len(file) / len(x)) + 1) for x in file]


def ch1(f, r, d):
    x, y = 0, 0
    ans = 0
    for _ in range(1, int(len(f)/d)):
        x += r
        y += d
        if f[y][x] == '#':
            ans += 1
    return ans


def ch2(f):
    return ch1(f, 1, 1) * ch1(f, 3, 1) * ch1(f, 5, 1) * ch1(f, 7, 1) * ch1(f, 1, 2)


print(ch1(file, 3, 1))
print(ch2(file))
