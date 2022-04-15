from functools import reduce
from itertools import combinations
from operator import mul

# tf = open('2015/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2015/inputs/input-24.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [int(x.strip()) for x in f]
    return data


def part1_and_2(f, num_groups):
    data = prep_input(f)
    group_size = sum(data) // num_groups
    for i in range(len(data)):
        qes = [reduce(mul, c) for c in combinations(data, i)
               if sum(c) == group_size]
        if qes:
            return min(qes)


print(f"part 1:\n{ part1_and_2(f, 3) }")
print(f"part 2:\n{ part1_and_2(f, 4) }")
