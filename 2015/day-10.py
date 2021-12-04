tf = [x.strip() + 'x' for x in open('2015/inputs/input-00.txt').readlines()][0]
f = [x.strip() + 'x' for x in open('2015/inputs/input-10.txt').readlines()][0]


def look_and_say(f, length):
    for _ in range(length):
        new_num = ''
        num_c = 1
        for i in range(1, len(f)):
            if f[i] == f[i-1]:
                num_c += 1
            else:
                new_num += str(num_c) + f[i-1]
                num_c = 1
        f = new_num + 'x'
    return new_num


print('part 1:\n' + str(len(look_and_say(f, 40))))
print('part 2:\n' + str(len(look_and_say(f, 50))))
