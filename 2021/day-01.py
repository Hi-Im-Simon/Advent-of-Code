tf = [int(l.strip()) for l in open('2021/inputs/input-00.txt').readlines()]
f = [int(l.strip()) for l in open('2021/inputs/input-01.txt').readlines()]


def count_increases(f):
    ans = 0
    for i in range(1, len(f)):
        if f[i] > f[i-1]:
            ans += 1
    return ans

def count_sum_increases(f):
    anss = []
    ans = 0
    for i in range(2, len(f)):
        anss.append(sum([f[i-2], f[i-1], f[i]]))
    for i in range(1, len(anss)):
        if anss[i] > anss[i-1]:
            ans += 1
    return ans
    
print('part 1:\n' + str(count_increases(f)))
print('part 2:\n' + str(count_sum_increases(f)))
