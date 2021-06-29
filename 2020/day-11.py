file = open('2020/inputs/input-11.txt')
f = [list(x.strip()) for x in file.readlines()]


def play_rounds(file, rounds=int(1e200)):
    leng = len(file) + 2
    file = [['.'] * (len(file[0]) + 2)] + [['.'] + x + ['.'] for x in file] + [['.'] * (len(file[0]) + 2)]
    newFile = [x.copy() for x in file]
    for _ in range(1, rounds):
        for y in range(1, leng - 1):
            for x in range(1, len(file[0]) - 1):
                count = [file[y - 1][x - 1], file[y - 1][x], file[y - 1][x + 1], file[y][x - 1], file[y][x + 1], file[y + 1][x - 1], file[y + 1][x], file[y + 1][x + 1]].count('#')
                if file[y][x] == 'L' and count == 0:
                    newFile[y][x] = '#'
                elif file[y][x] == '#' and count >= 4:
                    newFile[y][x] = 'L'
        if file == newFile:
            return sum([x.count('#') for x in file])
        file = [x.copy() for x in newFile]


def play_rounds_strict(file, rounds=int(1e200)):
    leng = len(file)
    newFile = [x.copy() for x in file]
    for _ in range(1, rounds):
        for y in range(leng):
            for x in range(len(file[0])):
                count = 0
                y1 = y
                while y1 > 0:
                    y1 -= 1
                    if file[y1][x] == 'L':
                        break
                    if file[y1][x] == '#':
                        count += 1
                        break
                x1, y1 = x, y
                while y1 > 0 and x1 < len(file[0]) - 1:
                    x1 += 1
                    y1 -= 1
                    if file[y1][x1] == 'L':
                        break
                    if file[y1][x1] == '#':
                        count += 1
                        break
                x1 = x
                while x1 < len(file[0]) - 1:
                    x1 += 1
                    if file[y][x1] == 'L':
                        break
                    if file[y][x1] == '#':
                        count += 1
                        break
                x1, y1 = x, y
                while y1 < leng - 1 and x1 < len(file[0]) - 1:
                    x1 += 1
                    y1 += 1
                    if file[y1][x1] == 'L':
                        break
                    if file[y1][x1] == '#':
                        count += 1
                        break
                y1 = y
                while y1 < leng - 1:
                    y1 += 1
                    if file[y1][x] == 'L':
                        break
                    if file[y1][x] == '#':
                        count += 1
                        break
                x1, y1 = x, y
                while y1 < leng - 1 and x1 > 0:
                    x1 -= 1
                    y1 += 1
                    if file[y1][x1] == 'L':
                        break
                    if file[y1][x1] == '#':
                        count += 1
                        break
                x1 = x
                while x1 > 0:
                    x1 -= 1
                    if file[y][x1] == 'L':
                        break
                    if file[y][x1] == '#':
                        count += 1
                        break
                x1, y1 = x, y
                while y1 > 0 and x1 > 0:
                    x1 -= 1
                    y1 -= 1
                    if file[y1][x1] == 'L':
                        break
                    if file[y1][x1] == '#':
                        count += 1
                        break

                if file[y][x] == 'L' and count == 0:
                    newFile[y][x] = '#'
                elif file[y][x] == '#' and count >= 5:
                    newFile[y][x] = 'L'
        if file == newFile:
            return sum([x.count('#') for x in file])
        file = [x.copy() for x in newFile]


print(play_rounds(f))
print(play_rounds_strict(f))

file.close()
