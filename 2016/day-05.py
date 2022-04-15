import hashlib

# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-05.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    return f[0]


def part1(f):
    data = prep_input(f)
    password = ''
    i = 0
    while len(password) < 8:
        string = data + str(i)
        hash = hashlib.md5(string.encode()).hexdigest()
        if hash[:5] == '00000':
            password += hash[5]
        i += 1
    return password


def part2(f):
    data = prep_input(f)
    password = [''] * 8
    filled = 0
    i = 0
    while filled < 8:
        string = data + str(i)
        hash = hashlib.md5(string.encode()).hexdigest()
        if hash[:5] == '00000':
            if hash[5].isdigit() and int(hash[5]) < 8 and password[int(hash[5])] == '':
                password[int(hash[5])] = hash[6]
                filled += 1
        i += 1
    return ''.join(password)


print(f"part 1:\n{ part1(f) }") # takes a few seconds
print(f"part 2:\n{ part2(f) }") # takes even longer
