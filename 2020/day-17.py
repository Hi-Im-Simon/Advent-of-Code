file = open('2020/inputs/input-17.txt')
f = [[x.strip() for x in file.readlines()]]


def expandCube(file):
    for layer in range(len(file)):
        for row in range(len(file[layer])):
            file[layer][row] = '.' + file[layer][row] + '.'
        file[layer].append('.' * len(file[layer][row]))
        file[layer].insert(0, '.' * len(file[layer][row]))
    file.append(['.' * len(file[0][0])] * len(file[0]))
    file.insert(0, ['.' * len(file[0][0])] * len(file[0]))
    return file


def simulate(file, n):
    file = expandCube(file)
    for _ in range(n):
        file = expandCube(file)
        file2 = [[y for y in x.copy()] for x in file.copy()]
        for lay in range(1, len(file) - 1):
            for row in range(1, len(file[lay]) - 1):
                for col in range(1, len(file[lay][row]) - 1):
                    count = 0
                    for lay2 in range(lay - 1, lay + 2):
                        for row2 in range(row - 1, row + 2):
                            for col2 in range(col - 1, col + 2):
                                if file[lay2][row2][col2] == '#':
                                    count += 1
                    if file[lay][row][col] == '#' and count not in [3, 4]:
                        file2[lay][row] = file2[lay][row][:col] + '.' + file2[lay][row][col + 1:]
                    elif file[lay][row][col] == '.' and count == 3:
                        file2[lay][row] = file2[lay][row][:col] + '#' + file2[lay][row][col + 1:]
        file = [[y for y in x.copy()] for x in file2.copy()]
    ans = 0
    for lay in range(len(file)):
        for row in range(len(file[lay])):
            for col in range(len(file[lay][row])):
                if file[lay][row][col] == '#':
                    ans += 1
    return ans


print(simulate(f, 6))

file.close()
