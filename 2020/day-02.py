file = open('2020/inputs/input-02.txt')
f = [x.strip().split() for x in file.readlines()]

def count_valid_passwords_a(file):
    ans = 0
    for line in f:
        start, end = [int(x) for x in line[0].split('-')]
        if start <= line[2].count(line[1][0]) <= end:
            ans += 1
    return ans


def count_valid_passwords_b(file):
    ans = 0
    for line in f:
        a, b = [int(x) - 1 for x in line[0].split('-')]
        letter = line[1][0]
        code = line[2]
        count = 0
        if len(code) > b:
            if code[a] == letter:
                count += 1
            if code[b] == letter:
                count += 1
            if count == 1:
                ans += 1
    return ans


print(count_valid_passwords_a(f))
print(count_valid_passwords_b(f))

file.close()
