tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-16.txt').readlines()    # your input data


class Valve:
    def __init__(self, flow, valves):
        self.flow = flow
        self.valves = valves
        

def prep_input(f):  # edit to adjust how the program reads your files
    data = dict()
    for line in f:
        line = line.rstrip().split()
        data[line[1]] = Valve(int(line[4].split('=')[1].strip(';')), [x.strip(',') for x in line[9:]])
    return data


def part1(f):
    data = prep_input(f)
    
    def rec(cur, m, e, timer=1, flown=0, opened=set(), my_cur=None, my_flown=None, my_opened=None):
        global CUR_MAX
        if timer == m:
            my_cur = cur
            my_flown = flown
            my_opened = opened
        elif timer == e:
            if flown > CUR_MAX:
                global best_cur, best_flown, best_opened
                CUR_MAX = flown
                best_cur = my_cur
                best_flown = my_flown
                best_opened = my_opened
            return
        
        # calculate current minute's flow
        flown += sum([data[x].flow for x in opened])
        
        if cur not in opened and data[cur].flow > 0:
            opened_copy = opened.copy()
            opened_copy.add(cur)
            rec(cur, m, e, timer + 1, flown, opened_copy, my_cur, my_flown, my_opened)
        else:
            for v in data[cur].valves:
                rec(v, m, e, timer + 1, flown, opened, my_cur, my_flown, my_opened)
    
    for i in range(0, MAX_TIME, sample_out):
        print(min(sample_out + i, MAX_TIME), min(sample_size + i, MAX_TIME))
        if sample_out + i >= MAX_TIME:
            break
        rec(best_cur, sample_out + i, sample_size + i, i, best_flown, best_opened)
        # print(i)
        # print(best_cur)
        # print(best_flown)
        # print(best_opened)
        # print('-----')
    return best_flown

def part2(f):
    data = prep_input(f)
    
    def rec(curP, curE, m, e, timer=1, flown=0, opened=set(), my_curP=None, my_curE=None, my_flown=None, my_opened=None):
        global CUR_MAX
        if timer == m:
            my_curP = curP
            my_curE = curE
            my_flown = flown
            my_opened = opened
        elif timer == e:
            if flown > CUR_MAX:
                global best_curP, best_curE, best_flown, best_opened
                CUR_MAX = flown
                best_curP = curP
                best_curE = curE
                best_flown = my_flown
                best_opened = my_opened
            return
        
        # calculate current minute's flow
        flown += sum([data[x].flow for x in opened])
                
        if curP not in opened and data[curP].flow > 0:
            opened_copy = opened.copy()
            if curE not in opened and data[curE].flow > 0:
                # they can both open
                if curP != curE:
                    opened_copy.add(curP)
                    opened_copy.add(curE)
                    rec(curP, curE, m, e, timer + 1, flown, opened_copy, my_curP, my_curE, my_flown, my_opened)
                    return
                    
            opened_copy.add(curP)
            for vE in data[curE].valves:
                if curP != vE:
                    rec(curP, vE, m, e, timer + 1, flown, opened_copy, my_curP, my_curE, my_flown, my_opened)
        elif curE not in opened and data[curE].flow > 0:
            opened_copy = opened.copy()
            opened_copy.add(curE)
            for vP in data[curP].valves:
                if vP != curE:
                    rec(vP, curE, m, e, timer + 1, flown, opened_copy, my_curP, my_curE, my_flown, my_opened)
        else:
            for vP in data[curP].valves:
                for vE in data[curE].valves:
                    if vP != vE:
                        rec(vP, vE, m, e, timer + 1, flown, opened, my_curP, my_curE, my_flown, my_opened)
                        
    for i in range(5, MAX_TIME, sample_out):
        rec(best_curP, bestE_curE, min(sample_out + i, MAX_TIME), min(sample_size + i, MAX_TIME), i, best_flown, best_opened)
        print(i)
        print(best_curP, best_curE)
        print(best_flown)
        print(best_opened)
        print('-----')
    return best_flown


sample_size, sample_out = 10, 2
MAX_TIME = 30

CUR_MAX = 0
best_cur, best_flown, best_opened = 'AA', 0, set()
print(f"part 1:\n{ part1(f) }")
CUR_MAX = 0
best_curP, bestE_curE, best_flown, best_opened = 'AA', 'AA', 0, set()
# print(f"part 2:\n{ part2(tf) }")
