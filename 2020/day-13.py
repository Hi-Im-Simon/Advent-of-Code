file = open('2020/inputs/input-13.txt')
f = [x.strip() for x in file.readlines()]
f = [int(f[0]), f[1].split(',')]


def find_earliest_bus(file):
    ansTime = -float('inf')
    for bus in file[1]:
        if bus != 'x':
            busTime = (file[0] % int(bus)) - int(bus)
            if busTime > ansTime:
                ansTime = busTime
                ansBus = int(bus)
    return ansBus * (-ansTime)


def find_earliest_timestamp(file):
    modulos = {}
    for i in range(len(file)):
        if file[i] != 'x':
            modulos[int(file[i])] = -i % int(file[i])
    iterator = 0
    increment = 1
    for bus in modulos.keys():
        while iterator % bus != modulos[bus]:
            iterator += increment
        increment *= bus
    return iterator


print(find_earliest_bus(f))
print(find_earliest_timestamp(f[1]))

file.close()
