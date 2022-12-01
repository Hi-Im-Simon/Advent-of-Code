tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-01.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [int(x.strip()) if x.strip() != '' else x.strip() for x in f]
    elfs = [0]
    i = 0
    for d in data:
        if d == '':
            i += 1
            elfs.append(0)
        else:
            elfs[i] += d
    return elfs


def part1(f):
    elfs = prep_input(f)
    return max(elfs)


def part2(f):
    elfs = prep_input(f)
    return sum(sorted(elfs)[-3:])


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
