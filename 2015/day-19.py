import sys
sys.setrecursionlimit(999999999)

tf = [x.strip() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2015/inputs/input-19.txt').readlines()]


def prep_input(f):
    reps = {}
    for line in f[:-2]:
        x1, x2 = line.split(' => ')
        i = 0
        x2_list = []
        while i < len(x2)-1:
            if x2[i+1].islower():
                x2_list.append(x2[i:i+2])
                i += 2
            else:
                x2_list.append(x2[i])
                i += 1
        if len(x2) > i:
            x2_list.append(x2[-1])
        x2 = x2_list
        if x1 in reps:
            reps[x1].append(x2)
        else:
            reps[x1] = [x2]
    molec = f[-1]
    molec_list = []
    i = 0
    while i < len(molec)-1:
        if molec[i+1].islower():
            molec_list.append(molec[i:i+2])
            i += 2
        else:
            molec_list.append(molec[i])
            i += 1
    if len(molec) > i:
        molec_list.append(molec[-1])
    return reps, molec_list


def part1(f):
    reps, molec = prep_input(f)
    molecs = set()
    for i in range(len(molec)):
        if molec[i] in reps:
            for m in reps[molec[i]]:
                molecs.add(''.join(molec[:i] + m + molec[i+1:]))
    return len(molecs)


def rec(reps, molec, go_to_len, cur, steps=0):
    minn = float('inf')
    if len(cur) == go_to_len:
        if cur == molec:
            return steps
    else:
        for to_replace_i in range(len(cur)):
            if cur[to_replace_i] in reps:
                for rep in reps[cur[to_replace_i]]:
                    minn = min(rec(reps, molec, go_to_len, cur[:to_replace_i] + rep + cur[to_replace_i+1:], steps+1), minn)
    return minn


def prep_molec(reps, molec):
    found = True
    steps = 0
    while found:
        found = False
        i = 0
        while i < len(molec):
            m = 0
            for rep in reps:
                if not found:
                    for j in range(2, len(molec)-i+1):
                        
                        if molec[i:i+j] in reps[rep]:
                            found = True
                            m = rep
                            # print(i, len(molec), molec[i:i+j], rep, reps[rep])
                            break
            
            if m:
                for _ in range(i+1, i+j):
                    del molec[i+1]
                molec[i] = m
            else:
                i += 1
                continue
            steps += 1
            # print(''.join(molec))
    return molec, steps


def get_next_brac(molec):
    cur_molec = []
    bracs = 0
    for i in range(len(molec)):
        if molec[i] == 'Rn':  # '('
            if bracs > 0 or len(cur_molec) == 0:
                bracs += 1
                cur_molec.append(molec[i])
            else:
                break
        elif molec[i] == 'Ar':
            bracs -= 1
            cur_molec.append(molec[i])
            if bracs == 0:
                return cur_molec, i+1
        else:
            cur_molec.append(molec[i])
    return cur_molec, i


def part2(f):
    reps, molec = prep_input(f)
    new_molec = []
    while True:
        cur_molec, i = get_next_brac(molec)
        print(cur_molec)
        molec = molec.copy()[i:]
        m, steps = prep_molec(reps, cur_molec)
        new_molec.append(m)
        if len(molec) == 1:
            new_molec.append([molec[0]])
            break
    
    return
    while len(new_molec) > 1:
        new_molec[0] = prep_molec(reps, new_molec[0] + new_molec[1])[0]
        del new_molec[1]
        print(new_molec)
    print(prep_molec(reps, new_molec[0]))
    # print(prep_molec(reps, molec))
    # return print(''.join(molec))
    # molec, steps = prep_molec(reps, molec)
    # print(steps)
    # go_to_len = len(molec)
    # return rec(reps, molec, go_to_len, ['e']) + steps


print('part 1:\n' + str(part1(f)))
print('part 2:\n' + str(part2(f)))
