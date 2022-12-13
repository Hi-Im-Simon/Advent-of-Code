import ast

tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-13.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [ast.literal_eval(x.rstrip()) for x in f if x.rstrip() != '']
    return data


def compare(left, right):
    for i in range(min(len(left), len(right))):
        if type(left[i]) is int and type(right[i]) is int:
            if left[i] < right[i]: 
                return 1
            elif left[i] > right[i]: 
                return 0
        elif type(left[i]) is list and type(right[i]) is list:
            out = compare(left[i], right[i])
            if out >= 0:
                return out
        else:
            out = compare(
                [left[i]] if (type(left[i]) == int) else left[i],
                [right[i]] if (type(right[i]) == int) else right[i]
            )
            if out >= 0:
                return out
    # if it doesn't get stopped during the loop, return value depending on length
    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return 0
    else:
        return -1


def part1(f):
    data = prep_input(f)
    ans = 0
    for i in range(0, len(data), 2):
        ans += int(((i + 2) / 2) if compare(data[i], data[i+1]) else 0)
    return ans


def part2(f):
    data = prep_input(f)
    divider_packets = [[[2]], [[6]]]
    ordered = [*divider_packets]
    for i in range(len(data)):
        for j in range(len(ordered)):
            if compare(data[i], ordered[j]):
                ordered = ordered[:j] + [data[i]] + ordered[j:]
                break
        else:
            ordered.append(data[i])
    return (ordered.index(divider_packets[0]) + 1) * (ordered.index(divider_packets[1]) + 1)


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
