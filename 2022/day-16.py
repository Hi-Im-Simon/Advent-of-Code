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
    
    def rec(cur, timer=1, flown=0, opened=set()):
        # calculate current minute's flow
        flown += sum([data[x].flow for x in opened])
        
        # if current flow is highest, save it
        global answers
        answers[timer] = max(answers[timer], flown)
        
        # if current flow is lower than the highest 2 steps ago, abort
        if answers[timer - 2] > flown or timer == MAX_TIME:
            return
        
        if cur not in opened and data[cur].flow > 0:
            opened_copy = opened.copy()
            opened_copy.add(cur)
            rec(cur, timer + 1, flown, opened_copy)
        else:
            for v in data[cur].valves:
                rec(v, timer + 1, flown, opened)
    
    rec('AA')
    return answers[MAX_TIME]


def part2(f):
    data = prep_input(f)
    
    def rec(curP, curE, timer=5, flown=0, opened=set(), pathP=['AA'], pathE=['AA']):
            # calculate current minute's flow
            flown += sum([data[x].flow for x in opened])
            
            # if current flow is highest, save it
            global answers
            answers[timer] = max(answers[timer], flown)
            
            # if current flow is lower than the highest 2 steps ago, abort
            if answers[timer - 2] > flown:
                return
            
            if timer == MAX_TIME:
                print(pathP)
                return
                    
            if curP not in opened and data[curP].flow > 0:
                opened_copy = opened.copy()
                if curE not in opened and data[curE].flow > 0:
                    # they can both open
                    if curP != curE:
                        opened_copy.add(curP)
                        opened_copy.add(curE)
                        rec(curP, curE, timer + 1, flown, opened_copy, pathP + [curP], pathE + [curE])
                        return
                        
                opened_copy.add(curP)
                for vE in data[curE].valves:
                    if curP != vE:
                        rec(curP, vE, timer + 1, flown, opened_copy, pathP + [curP], pathE + [vE])
            elif curE not in opened and data[curE].flow > 0:
                opened_copy = opened.copy()
                opened_copy.add(curE)
                for vP in data[curP].valves:
                    if vP != curE:
                        rec(vP, curE, timer + 1, flown, opened_copy, pathP + [vP], pathE + [curE])
            else:
                for vP in data[curP].valves:
                    for vE in data[curE].valves:
                        if vP != vE:
                            rec(vP, vE, timer + 1, flown, opened, pathP + [vP], pathE + [vE])
    global MAX_TIME
    rec('AA', 'AA')
    return answers[MAX_TIME]


MAX_TIME = 15
answers = [0] * (MAX_TIME + 1)
# print(f"part 1:\n{ part1(f) }")
answers = [0] * (MAX_TIME + 1)
print(f"part 2:\n{ part2(tf) }")
