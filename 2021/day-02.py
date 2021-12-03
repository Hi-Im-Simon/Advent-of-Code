tf = [x.strip().split() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip().split() for x in open('2021/inputs/input-02.txt').readlines()]


def get_positions(f):
    horiz, depth = 0, 0
    for line in f:
        if line[0] == 'forward':
            horiz += int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        elif line[0] == 'up':
            depth -= int(line[1])    
    return horiz, depth, horiz * depth


def get_positions_and_aim(f):
    horiz, depth, aim = 0, 0, 0
    for line in f:
        if line[0] == 'forward':
            horiz += int(line[1])
            depth += aim * int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
    return horiz, depth, aim, horiz * depth


print('part 1:\n' + str(get_positions(f)[2]))
print('part 2:\n' + str(get_positions_and_aim(f)[3]))
