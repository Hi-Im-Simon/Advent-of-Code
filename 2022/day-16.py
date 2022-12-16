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
    times = dict({ i: 0 for i in range(40) })
    valves = prep_input(f)
    ans = [0]
    
    def rec(time, cur='AA', flown=0, opened=set()):
        if flown < times[time + 1]:
            return
        elif flown > times[time]:
            times[time] = flown
        opened = opened.copy()
        if not time:
            if flown > ans[0]:
                ans[0] = flown
        else:
            flown += sum([valves[v].flow for v in opened])
            for v in valves[cur].valves:
                rec(time - 1, v, flown, opened)
            if valves[cur].flow and not (cur in opened):
                opened.add(cur)
                rec(time - 1, cur, flown, opened)
    
    rec(30)
    return ans[0]


def part2(f):
    times = dict({ i: 0 for i in range(40) })
    valves = prep_input(f)    
    relevant_valves_count = sum([1 if valves[v].flow else 0 for v in valves])
    ans = [0]
    
    def rec(time, curP='AA', curE='AA', flown=0, opened=set()):
        if flown < times[time + 1]:
            return
        elif flown > times[time]:
            times[time] = flown
            
        if not time:
            if flown > ans[0]:
                ans[0] = flown
        elif len(opened) >= relevant_valves_count:
            flown += (sum([valves[v].flow for v in opened]) * time)
            if flown > ans[0]:
                ans[0] = flown
        else:
            flown += sum([valves[v].flow for v in opened])
            
            vPs = valves[curP].valves.copy()
            if valves[curP].flow and not (curP in opened):
                vPs.append(curP)
            vEs = valves[curE].valves.copy()
            if valves[curE].flow and not (curE in opened):
                vEs.append(curE)
                
            for vP in vPs:
                for vE in vEs:
                    new_opened = opened.copy()
                    if vP == curP:
                        new_opened.add(curP)
                    if vE == curE:
                        new_opened.add(curE)
                    rec(time - 1, vP, vE, flown, new_opened)
    
    rec(26)
    return ans[0]


# print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
