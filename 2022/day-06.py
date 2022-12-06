tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-06.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = f[0].strip()
    return data


def part1_2(f, dists):
    data = prep_input(f)
    for i in range(3, len(data)):
        if len(set(data[i-dists+1:i+1])) == dists:
            return i + 1


print(f"part 1:\n{ part1_2(f, 4) }")
print(f"part 2:\n{ part1_2(f, 14) }")
