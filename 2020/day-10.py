file = open('2020/inputs/input-10.txt')
f = [int(x.strip()) for x in file.readlines()]


def differences(file):
    file = [0] + sorted(file.copy()) + [max(file) + 3]
    c1, c2, c3 = 0, 0, 0
    for i in range(1, len(file)):
        if file[i] - file[i - 1] == 1:
            c1 += 1
        elif file[i] - file[i - 1] == 2:
            c2 += 1
        else:
            c3 += 1
    return c1 * c3


def count_arrangements_rec(file):
    tab = [1, 1]
    if file[2] - file[0] <= 3:
        tab.append(2)
    else:
        tab.append(0)

    for i in range(3, max(file)):
        if i in file:
            tab.append(tab[i - 1] + tab[i - 2] + tab[i - 3])
        else:
            tab.append(0)

    return max(tab)


def count_arrangements(file):
    file = [0] + sorted(file.copy()) + [max(file) + 3]
    return count_arrangements_rec(file)


print(differences(f))
print(count_arrangements(f))

file.close()
