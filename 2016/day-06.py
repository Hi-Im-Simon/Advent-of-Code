# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-06.txt').readlines()    # your input data


ALPH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    return data


def part1_and_2(f, part_nr):
    data = prep_input(f)
    counts = [{let: 0 for let in ALPH} for _ in range(len(data[0]))]
    for line in data:
        for i, let in enumerate(line):
            counts[i][let] += 1
    message = ''
    for i in range(len(data[0])):
        for let in counts[i].copy():
            if counts[i][let] == 0:
                del counts[i][let]
        if part_nr == 1: message += max(counts[i], key=counts[i].get)
        elif part_nr == 2: message += min(counts[i], key=counts[i].get)
    return message


print(f"part 1:\n{ part1_and_2(f, 1) }")
print(f"part 2:\n{ part1_and_2(f, 2) }")
