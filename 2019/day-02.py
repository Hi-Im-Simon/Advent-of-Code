file = open('2019/inputs/input-02.txt')
f = [int(x) for x in file.read().split(',')]


def run(file, n1=12, n2=2, i=0):
    file = file.copy()
    file[1] = n1
    file[2] = n2
    while file[i] != 99:
        if file[i] == 1:
            file[file[i + 3]] = file[file[i + 1]] + file[file[i + 2]]
        elif file[i] == 2:
            file[file[i + 3]] = file[file[i + 1]] * file[file[i + 2]]
        i += 4
    return file[0]


def findPair(file):
    for x in range(0, 100):
        for y in range(0, 100):
            if run(file.copy(), x, y) == 19690720:
                return 100 * x + y
            


print(run(f))
print(findPair(f))

file.close()
