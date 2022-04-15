tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-03.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [list(map(int, x.split())) for x in f]
    return data


def count(data):
    data = [sorted(x) for x in data]
    ans = 0
    for line in data:
        if line[2] < sum(line[:2]):
            ans += 1
    return ans


def part1(f):
    return count(prep_input(f))


def part2(f):
    data = prep_input(f)
    for i in range(0, len(data), 3):
        data[i+1][0], data[i][1] = data[i][1], data[i+1][0]
        data[i+2][0], data[i][2] = data[i][2], data[i+2][0]
        data[i+2][1], data[i+1][2] = data[i+1][2], data[i+2][1]
    return count(data)


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
