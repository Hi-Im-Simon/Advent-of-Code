tf = [x.strip().split() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip().split() for x in open('2015/inputs/input-09.txt').readlines()]


def make_dicts(f):
    locs = {}
    for line in f:
        if line[0] not in locs:
            locs[line[0]] = {}
        if line[2] not in locs:
            locs[line[2]] = {}
        locs[line[0]][line[2]] = int(line[4])
        locs[line[2]][line[0]] = int(line[4])
    return locs


def route(r, locs, dist, path='short'):
    if len(r) == len(locs):
        return dist
    else:
        if path == 'long':
            m = 0
        else:
            m = float('inf')
        for city in locs[r[-1]]:
            if city not in r:
                if path == 'long':
                    m = max(route(r + [city], locs, dist + locs[r[-1]][city], 'long'), m)
                else:
                    m = min(route(r + [city], locs, dist + locs[r[-1]][city]), m)
    return m


def shortest_longest_route(f, path='short'):
    locs = make_dicts(f)
    route_lens = []
    for city in locs.keys():
        route_lens.append(route([city], locs, 0, path))
    if path == 'long':
        return max(route_lens)
    else:
        return min(route_lens)


print('part 1:\n' + str(shortest_longest_route(f, 'short')))
print('part 2:\n' + str(shortest_longest_route(f, 'long')))
