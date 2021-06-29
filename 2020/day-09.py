file = open('2020/inputs/input-09.txt')
f = [int(x.strip()) for x in file.readlines()]


def find_weakness(file, preamble):
    for i in range(preamble, len(file)):
        found = False
        for a in range(i - preamble, i - 1):
            if found:
                break
            for b in range(a + 1, i):
                if file[a] + file[b] == file[i]:
                    found = True
                    break
        if not found:
            return file[i]


def find_weakness_set(file, preamble):
    weakness = find_weakness(file, preamble)
    i = 0
    nums = []
    while True:
        summ = sum(nums)
        if summ == weakness:
            return min(nums) + max(nums)
        elif summ < weakness:
            nums.append(file[i])
            i += 1
        elif summ > weakness:
            nums = nums[1:]


PREAMBLE = 25
print(find_weakness(f, PREAMBLE))
print(find_weakness_set(f, PREAMBLE))

file.close()
