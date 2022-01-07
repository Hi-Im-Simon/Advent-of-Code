tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-18.txt').readlines()]


def prep_input(f):
    return [eval(line) for line in f]


def explode(nums, depth=0):
    if type(nums[0]) is int and type(nums[1]) is int:
        if depth >= 4:
            return None, nums[0], nums[1]
    for i, el in enumerate(nums):
        if type(el) is list:
            output, left, right = explode(el, depth+1)
            if output:
                nums[i] = output
            else:
                del nums[i]
    if len(nums) > 1:
        if type(nums[0])
    return nums, left, right


def part1(f): 
    nums = prep_input(f)
    print(nums)
    
    nums, _, _ = explode(nums)
    
    return nums


def part2(f): return None


print(f"part 1:\n{ part1(tf) }")
print(f"part 2:\n{ part2(f) }")
