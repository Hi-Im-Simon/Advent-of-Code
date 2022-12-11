import numpy as np
import math
tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-11.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip().split() for x in f] + [[]] # + to append the last monkey to the list
    monkeys = []
    
    for line in data:
        if line == []:
            monkeys.append(monkey)
        elif line[0] == 'Monkey':
            monkey = Monkey()
        elif line[0] == 'Starting':
            monkey.items = [int(x.strip(',')) for x in line[2:]]
        elif line[0] == 'Operation:':
            monkey._operator = line[4]
            monkey._value = (int(line[5]) if line[5] != 'old' else line[5])
        elif line[0] == 'Test:':
            monkey.div = int(line[3])
        elif line[1] == 'true:':
            monkey.throw[1] = int(line[5])
        elif line[1] == 'false:':
            monkey.throw[0] = int(line[5])
    return monkeys


class Monkey:
    def __init__(self):
        self.items = None
        self._operator = None
        self._value = None
        self.div = None
        self.throw = [None, None]
        self.inspections = 0
        
    def calc(self, div_func):
        if self._value == 'old':
            val = self.items[0]
        else:
            val = self._value
            
        if self._operator == '+':
            self.items[0] += val
        else:
            # self.items[0] = np.multiply(self.items[0], val)
            self.items[0] *= val
        self.items[0] = div_func(self.items[0])
        self.inspections += 1
        return self.throw[not (self.items[0] % self.div)]
    
    
def _solve(monkeys, repeats, func):
    for _ in range(repeats):
        for monkey in monkeys:
            for _ in monkey.items:
                new_monkey = monkey.calc(func)
                monkeys[new_monkey].items.append(monkey.items[0])
                monkey.items = monkey.items[1:]

    inspections = sorted([monkey.inspections for monkey in monkeys])
    return inspections[-1] * inspections[-2]
    

def part1(f):
    monkeys = prep_input(f)
    return _solve(monkeys, 20, lambda x: x // 3)
    


def part2(f):
    monkeys = prep_input(f)
    common_div = max(math.lcm(*[monkey.div for monkey in monkeys]), 1)
    return _solve(monkeys, 10000, lambda x: x % common_div)


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
