file = open('2020/inputs/input-12.txt')
f = [x.strip() for x in file.readlines()]


def sail(file, x = 0, y = 0, degr = 90):
    for instr in file:
        instr, val = instr[0], int(instr[1:])
        if instr == 'N':
            y -= val
        elif instr == 'S':
            y += val
        elif instr == 'E':
            x += val
        elif instr == 'W':
            x -= val
        elif instr == 'L':
            degr -= val
            while not 0 <= degr < 360:
                degr += 360
        elif instr == 'R':
            degr += val
            while not 0 <= degr < 360:
                degr -= 360
        elif instr == 'F':
            if degr == 0:
                y -= val
            elif degr == 180:
                y += val
            elif degr == 90:
                x += val
            elif degr == 270:
                x -= val
    return abs(x) + abs(y)


def sail_relative(file, xw = 0, yw = 0, x = 0, y = 0):
    for instr in file:
        instr, val = instr[0], int(instr[1:])
        if instr == 'N':
            yw += val
        elif instr == 'S':
            yw -= val
        elif instr == 'E':
            xw += val
        elif instr == 'W':
            xw -= val
        elif instr == 'L':
            while val > 0:
                val -= 90
                xw, yw = -yw, xw
        elif instr == 'R':
            while val > 0:
                val -= 90
                xw, yw = yw, -xw
        elif instr == 'F':
            xm, ym = val * xw, val * yw
            x += xm
            y += ym
    return abs(x) + abs(y)


print(sail(f))
print(sail_relative(f, 10, 1))

file.close()
