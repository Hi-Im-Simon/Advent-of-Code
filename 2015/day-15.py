# tf = [x.strip().split() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip().split() for x in open('2015/inputs/input-15.txt').readlines()]


def prep_input(f):
    ingr = {}
    for line in f:
        head = line[0][:-1]
        ingr[head] = {}
        for i in range(1, len(line), 2):
            ingr[head][line[i]] = int(line[i+1].strip(','))
    return ingr


def best_recipy(f, spoons, wanted_call):
    ingr = prep_input(f)
    ans = 0
    for i0 in range(spoons+1):
        for i1 in range(spoons-i0+1):
            for i2 in range(spoons-i0-i1+1):
                i3 = spoons - i0 - i1 - i2
                iss = [i0, i1, i2, i3]
                vals = [0, 0, 0, 0]  
                call = 0   
                for i, ing in enumerate(ingr):
                    for j, prop in enumerate(ingr[ing]):
                        if prop != 'calories':
                            vals[j] += ingr[ing][prop] * iss[i]
                        elif wanted_call > 0:
                            call += ingr[ing][prop] * iss[i]
                possible_ans = max(vals[0], 0) * max(vals[1], 0) * max(vals[2], 0) * max(vals[3], 0)
                if possible_ans > ans and call == wanted_call:
                    ans = possible_ans
    return ans
    
    
print('part 1:\n' + str(best_recipy(f, 100, 0)))
print('part 2:\n' + str(best_recipy(f, 100, 500)))
