file = open('2020/inputs/input-15.txt')
f = [int(x) for x in file.read().split(',')]


def game(file, stop):
    nums = {}
    for i in range(len(file[:-1])):
        nums[file[i]] = i + 1

    last = file[-1]
    for i in range(len(file), stop):
        if last not in nums:
            nums[last] = i
            last = 0
        else:
            cur = i - nums[last]
            nums[last] = i
            last = cur
    return last


print(game(f, 2020))
print(game(f, 30000000))

file.close()
