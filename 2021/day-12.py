# tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-12.txt').readlines()]


def prep_input(f):
    caves = {}
    for line in f:
        x1, x2 = line.split('-')
        if x1 in caves:
            caves[x1].append(x2)
        else:
            caves[x1] = [x2]
        if x2 in caves:
            caves[x2].append(x1)
        else:
            caves[x2] = [x1]
    return caves


def part1(cave, visited):
    for c in caves[cave]:
        if c == 'end':
            global ans1
            ans1 += 1
        elif c.upper() == c:
            part1(c, visited)
        elif not visited[c]:
            vis = visited.copy()
            vis[c] = True
            part1(c, vis)
    return ans1


def part2(cave, visited, event=False):
    for c in caves[cave]:
        if c == 'end':
            global ans2
            ans2 += 1
        elif c.upper() == c:
            part2(c, visited, event)
        elif not visited[c]:
            vis = visited.copy()
            vis[c] = True
            part2(c, vis, event)
        elif not event and c != 'start':
            part2(c, visited, event=True)
    return ans2


caves = prep_input(f)
ans1, ans2 = 0, 0
print(f"part 1:\n{ part1('start', visited={x: False if x != 'start' else True for x in caves }) }")
print(f"part 2:\n{ part2('start', visited={x: False if x != 'start' else True for x in caves }) }")
