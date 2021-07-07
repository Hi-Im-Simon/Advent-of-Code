file = open('2020/inputs/input-14.txt')
f = [x.strip().split(' = ') for x in file.readlines()]


def decode(file):
    memory = []
    for line in file:
        if line[0] == 'mask':
            mask = line[1][::-1]
        else:
            mem = int(line[0][4:-1])
            val = str(bin(int(line[1])))[2:][::-1]
            memory += [0] * (mem - len(memory))
            result = ''
            for i in range(len(mask)):
                if i < len(val):
                    if mask[i] == 'X':
                        result += val[i]
                    else:
                        result += mask[i]
                else:
                    if mask[i] == '1':
                        result += '1'
                    else:
                        result += '0'
            memory[mem - 1] = result[::-1]
    return sum([int(str(x), 2) for x in memory])

""" INEFFICIENT METHODE
def build_nums(num, val):
    if num.count('X') > 0:
        i = 0
        while num[i] != 'X':
            i += 1
        build_nums(num[:i] + '0' + num[i + 1:], val)
        build_nums(num[:i] + '1' + num[i + 1:], val)
    else:
        global memory
        memory += [0] * (int(num, 2) - len(memory))
        memory[int(num, 2) - 1] = val


memory = []
def decode_v2(file):
    global memory
    for line in file:
        if line[0] == 'mask':
            mask = line[1][::-1]
        else:
            mem = int(line[0][4:-1])
            val = str(bin(mem))[2:][::-1]
            vall = int(line[1])
            result = ''
            for i in range(len(mask)):
                if i < len(val):
                    if val[i] == '1' and mask[i] != 'X':
                        result += '1'
                    else:
                        result += mask[i]
                else:
                    result += mask[i]
            build_nums(result[::-1], vall)
    return sum(memory)
"""

def decode_v2(file):
    memory = {}
    memory2 = set()
    for line in file:
        if line[0] == 'mask':
            mask = line[1][::-1]
        else:
            mem = int(line[0][4:-1])
            val = str(bin(mem))[2:][::-1]
            vall = int(line[1])
            result = ''
            for i in range(len(mask)):
                if i < len(val):
                    if val[i] == '1' and mask[i] != 'X':
                        result += '1'
                    else:
                        result += mask[i]
                else:
                    result += mask[i]
            result = result[::-1].lstrip('0')

            tab = [int(result.replace('X', '0'), 2)]
            leng = len(result)
            for i in range(len(result)):
                if result[i] == 'X':
                    for n in range(len(tab)):
                        tab.append(tab[n] + 2 ** (leng - i - 1))
            for n in tab:
                memory[n] = vall
                memory2.add(n)
    ans = 0
    for i in memory2:
        ans += memory[i]
    return ans


print(decode(f))
print(decode_v2(f))

file.close()
