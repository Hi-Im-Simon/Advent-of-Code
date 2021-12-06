# tf = [int(x) for x in open('2021/inputs/input-00.txt').read().split(',')]
f = [int(x) for x in open('2021/inputs/input-06.txt').read().split(',')]


def part1_and_2(fish, t):
    f_time = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for f in fish:
        f_time[f] += 1
    for _ in range(t):
        f_time[8], f_time[7], f_time[6], f_time[5], f_time[4], f_time[3], f_time[2], f_time[1], f_time[0] = f_time[0], f_time[8], f_time[7] + f_time[0], f_time[6], f_time[5], f_time[4], f_time[3], f_time[2], f_time[1]    
    return sum(list(f_time.values()))


print('part 1:\n' + str(part1_and_2(f, 80)))
print('part 2:\n' + str(part1_and_2(f, 256)))
