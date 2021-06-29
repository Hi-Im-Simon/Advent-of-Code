file = open('2020/inputs/input-01.txt')
f = [int(x[:-1]) for x in file.readlines()]


def find_sum_2(file, s):
    for i in range(len(file) - 1):
        for j in range(i + 1, len(file)):
            if file[i] + file[j] == s:
                return file[i] * file[j]


def find_sum_3(file, s):
    for i in range(len(file) - 2):
        for j in range(i + 1, len(file) - 1):
            for k in range(j + 1, len(file)):
                if file[i] + file[j] + file[k] == s:
                    return file[i] * file[j] * file[k]


print(find_sum_2(f, 2020))
print(find_sum_3(f, 2020))

file.close()
