tf = open('2015/inputs/input-00.txt').read()
f = [[int(x) for x in line.strip().split('x')] for line in open('2015/inputs/input-02.txt').readlines()]

paper = 0
ribbon = 0

for g in f:
    sides = [g[0]*g[1], g[1]*g[2], g[2]*g[0]]
    paper += 2 * sum(sides) + min(sides)
    
    qub = g[0] * g[1] * g[2]
    g.remove(max(g))
    ribbon += 2 * sum(g) + qub
    
print('part 1:\n' + str(paper))
print('part 2:\n' + str(ribbon))
