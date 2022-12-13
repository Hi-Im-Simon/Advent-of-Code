import sys
sys.setrecursionlimit(10000)

tf = open('2022/inputs/input-00.txt').readlines()
f = open('2022/inputs/input-12.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = []
    S, E = None, None
    for i in range(len(f)):
        l = f[i].rstrip()
        line = [100]
        if 'S' in l:
            S = (l.index('S') + 1, i + 1)
        if 'E' in l:
            E = (l.index('E') + 1, i + 1)
        for x in l:
            if x not in ['S', 'E']:
                line.append(ord(x) - 97)
            else:
                if x == 'S':
                    line.append(0)
                else:
                    line.append(25)
        data.append(line + [100])
    return [[100 for _ in range(len(data[0]))]] + data + [[100 for _ in range(len(data[0]))]], S, E


def part1():
    return dists[S]


def part2():
    return min([dists[x] for x in dists if data[x[1]][x[0]] == 0])


data, S, E = prep_input(f)
dists = dict({ E: 0 })


def rev_bfs(cur=E):
    neighs = [(cur[0] - 1, cur[1]), (cur[0] + 1, cur[1]),
              (cur[0], cur[1] - 1), (cur[0], cur[1] + 1)]
    todo = []
    for neigh in neighs:
        if 100 > data[neigh[1]][neigh[0]] + 1 >= data[cur[1]][cur[0]]:
            if neigh not in dists or dists[neigh] > dists[cur] + 1:
                dists[neigh] = dists[cur] + 1
                todo.append(neigh)
    for neigh in todo:
        rev_bfs(neigh)
rev_bfs()


print(f"part 1:\n{ part1() }")
print(f"part 2:\n{ part2() }")
