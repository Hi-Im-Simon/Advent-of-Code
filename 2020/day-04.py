file = open('2020/inputs/input-04.txt')
f = [x.strip().split() for x in file.readlines()]
i = 1
while len(f) > i:
    if f[i] == []:
        i += 1
    else:
        f[i - 1] = f[i - 1] + f[i]
        del f[i]


def count_valid(file):
    ans = 0
    for per in file:
        count = 0
        for field in per:
            field = field.split(':')[0]
            if field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
                count += 1
        if count == 7:
            ans += 1
    return ans


def count_valid_strict(file):
    ans = 0
    for per in file:
        count = 0
        for field in per:
            field, data = field.split(':')
            if field == 'byr':
                data = int(data)
                if 1920 <= data <= 2002:
                    count += 1
            elif field == 'iyr':
                data = int(data)
                if 2010 <= data <= 2020:
                    count += 1
            elif field == 'eyr':
                data = int(data)
                if 2020 <= data <= 2030:
                    count += 1
            elif field == 'hgt':
                if len(data) > 3:
                    unit = data[-2:]
                    data = int(data[:-2])
                    if unit == 'cm' and 150 <= data <= 193 or unit == 'in' and 59 <= data <= 76:
                        count += 1
            elif field == 'hcl':
                if data[0] == '#':
                    for char in data[1:]:
                        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                            break
                    else:
                        count += 1
            elif field == 'ecl':
                if data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    count += 1
            elif field == 'pid':
                if len(data) == 9:
                    count += 1
        if count == 7:
            ans += 1
    return ans


print(count_valid(f))
print(count_valid_strict(f))

file.close()
