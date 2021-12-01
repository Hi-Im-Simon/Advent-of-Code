tf = open('2015/inputs/input-00.txt').read()
f = open('2015/inputs/input-03.txt').read()

locs1 = [[0, 0]]
loc1 = locs1[-1].copy()

locs2 = [[0, 0]]
loc2s = locs2[-1].copy()
loc2r = locs2[-1].copy()

for i, c in enumerate(f):
    if c == '^':
        loc1[1] += 1
        if i % 2 == 0:
            loc2s[1] += 1
        else:
            loc2r[1] += 1
    elif c == 'v':
        loc1[1] -= 1
        if i % 2 == 0:
            loc2s[1] -= 1
        else:
            loc2r[1] -= 1
    elif c == '>':
        loc1[0] += 1
        if i % 2 == 0:
            loc2s[0] += 1
        else:
            loc2r[0] += 1
    elif c == '<':
        loc1[0] -= 1
        if i % 2 == 0:
            loc2s[0] -= 1
        else:
            loc2r[0] -= 1
        
    if loc1 not in locs1:
        locs1.append(loc1.copy())
    if loc2s not in locs2:
        locs2.append(loc2s.copy())
    if loc2r not in locs2:
        locs2.append(loc2r.copy())

print('part 1:\n' + str(len(locs1)))
print('part 2:\n' + str(len(locs2)))
