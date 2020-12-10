def ch1(f):
    ans = 0
    for group in file:
        g = set()
        for i in range(len(group)):
            for char in group[i]:
                g.add(char)
        ans += len(g)
    return ans


def ch2(f):
    ans = 0
    for group in f:
        group[0] = list(group[0])
        for i in range(1, len(group)):
            for char in group[0]:
                if char not in group[i]:
                    group[0].remove(char)
        ans += len(group[0])
    return ans


file = open('c:/Code/Advent of Code/2020/inputs/input6.txt').read().split('\n\n')

file = [f.split('\n') for f in file]
print(ch1(file))
# print(ch2(file))   I have no idea what's wrong with this
print(list(map(sum, (zip(*map(lambda x: (len(set(x.replace("\n", ""))),len(set.intersection(*map(set, x.split("\n"))))), open("c:/Code/Advent of Code/2020/inputs/input6.txt").read().split("\n\n"))))))[1])
