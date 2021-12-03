tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-03.txt').readlines()]


def get_common_bits(f):
    common = [0 for _ in range(len(f[0]))] 
    for i in range(len(f[0])):
        for line in f:
            if line[i] == '1':
                common[i] += 1
    return common
    
    
def get_gamma_epsilon(f):
    common = get_common_bits(f)
    gamma = ''
    for bit in common:
        if bit > len(f) // 2:
            gamma += '1'
        else:
            gamma += '0'
    epsilon = gamma.replace('0', '2').replace('1', '0').replace('2', '1')
    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    return gamma, epsilon, gamma * epsilon


def get_oxygen(f):
    nums = f.copy()
    for i in range(len(nums[0])):
        common = ''.join(['1' if x >= len(nums) / 2 else '0' for x in get_common_bits(nums)])
        for num in nums.copy():
            if int(common[i]) != int(num[i]):
                nums.remove(num)
                if len(nums) <= 1:
                    return nums


def get_co2(f):
    nums = f.copy()
    for i in range(len(nums[0])):
        common = ''.join(['0' if x >= len(nums) / 2 else '1' for x in get_common_bits(nums)])
        for num in nums.copy():
            if int(common[i]) != int(num[i]):
                nums.remove(num)
                if len(nums) <= 1:
                    return nums
    

print('part 1:\n' + str(get_gamma_epsilon(f)[2]))
print('part 2:\n' + str(int(get_oxygen(f)[0], 2) * int(get_co2(f)[0], 2)))
