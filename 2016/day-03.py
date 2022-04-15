tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-03.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    return data


def part1(f):
    data = prep_input(f)
    
    
    return data


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
