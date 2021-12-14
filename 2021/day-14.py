tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-14.txt').readlines()]


def prep_input(f):
    pair = {}
    switch = 0
    for line in f:
        if line == '':
            switch = 1
        elif switch:
            line = line.split(' -> ')
            pair[line[0]] = line[1]
        else:
            polymer = line
    return polymer, pair


def part1_and_2(f, t=1): 
    polymer, pair = prep_input(f)
    pair_count = {x: 0 for x in pair}
    letter_count = {x: polymer.count(x) for x in pair.values()}
    for i in range(len(polymer)-1):
        pair_count[polymer[i:i+2]] += 1
        
    for _ in range(t):
        new_pair_count = pair_count.copy()
        for ac in pair_count:
            count = pair_count[ac]
            if count > 0:
                a, b, c = ac[0], pair[ac], ac[1]
                new_pair_count[a+b] += count
                new_pair_count[b+c] += count
                new_pair_count[ac] -= count
                letter_count[b] += count
        pair_count = new_pair_count
        
    vals = letter_count.values()
    return max(vals) - min(vals)


print(f"part 1:\n{ part1_and_2(f, 10) }")
print(f"part 2:\n{ part1_and_2(f, 40) }")
