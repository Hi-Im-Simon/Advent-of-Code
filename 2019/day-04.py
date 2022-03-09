f = open('2019/inputs/input-04.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [tuple(x.strip().split('-')) for x in f][0]
    return data


def part1(f):
    ans = 0
    data = prep_input(f)
    for i0 in range(int(data[0][0]), int(data[1][0])+1):
        for i1 in range(i0, 10):
            for i2 in range(i1, 10):
                for i3 in range(i2, 10):
                    for i4 in range(i3, 10):
                        for i5 in range(i4, 10):
                            if (i0 == i1 or i1 == i2 or i2 == i3 or i3 == i4 or i4 == i5):
                                num = int(''.join([str(x) for x in [i0, i1, i2, i3, i4, i5]]))
                                if int(data[0]) <= num <= int(data[1]):
                                    ans += 1
    return ans


def part2(f):
    ans = 0
    data = prep_input(f)
    for i0 in range(int(data[0][0]), int(data[1][0])+1):
        for i1 in range(i0, 10):
            for i2 in range(i1, 10):
                for i3 in range(i2, 10):
                    for i4 in range(i3, 10):
                        for i5 in range(i4, 10):
                            if (i0 == i1 != i2 or i0 != i1 == i2 != i3 or i1 != i2 == i3 != i4 or i2 != i3 == i4 != i5 or i3 != i4 == i5):
                                num = int(
                                    ''.join([str(x) for x in [i0, i1, i2, i3, i4, i5]]))
                                if int(data[0]) <= num <= int(data[1]):
                                    ans += 1
    
    
    return ans


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
