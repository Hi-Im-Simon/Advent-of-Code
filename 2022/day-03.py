tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-03.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    return data


def out_from_ord(ord):
    if ord > 90: return ord - 96
    else: return ord - 38


def part1(f):
    data = prep_input(f)
    ans = 0
    for d in data:
        r1, r2 = d[:len(d) // 2], d[len(d) // 2:]
        common = ord(''.join(set(r1).intersection(r2)))
        ans += out_from_ord(common)

    
    return ans


def part2(f):
    data = prep_input(f)
    ans = 0
    for d in range(0, len(data), 3):
        common = ord(''.join(set(data[d]).intersection(data[d+1]).intersection(data[d+2])))
        ans += out_from_ord(common)
    
    
    return ans


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
