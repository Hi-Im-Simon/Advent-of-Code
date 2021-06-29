file = open('2020/inputs/input-03.txt')
f = [x.strip() * int((len(x) * 10)) for x in file.readlines()]


def count_encounters(file, xi, yi):
    ans = 0
    x = 0
    for y in range(0, len(file), yi):
        if file[y][x] == '#':
            ans += 1
        x += xi
    return ans


def experiment_result(file):
    return count_encounters(f, 1, 1) * count_encounters(f, 3, 1) * count_encounters(f, 5, 1) * count_encounters(f, 7, 1) * count_encounters(f, 1, 2)


print(count_encounters(f, 3, 1))
print(experiment_result(f))

file.close()
