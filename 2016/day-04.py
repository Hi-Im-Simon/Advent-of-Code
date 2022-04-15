# tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-04.txt').readlines()    # your input data


ALPH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    data = [[x[:-11], int(x[-10:-7]), x[-6:-1]] for x in data]
    return data


def is_valid(name, check):
    real = True
    lets = {let: 0 for let in ALPH}
    for let in name:
        if let != '-':
            lets[let] += 1
    for i in range(len(check)-1):
        if lets[check[i]] < lets[check[i+1]] or (lets[check[i]] == lets[check[i+1]] and check[i] > check[i+1]):
            real = False
            break
    else:
        for let in ALPH:
            if let not in check:
                if lets[let] > lets[check[-1]]:
                    real = False
                    break
    return real


def part1(f):
    data = prep_input(f)
    ans = 0
    for line in data:
        name, id, check = line
        if is_valid(name, check):
            ans += id
    return ans


def part2(f):
    data = prep_input(f)
    for line in data:
        name, id, check = line
        if is_valid(name, check):
            decrypted_name = ''
            for let in name:
                if let != '-':
                    decrypted_name += ALPH[(ALPH.index(let) + id) % len(ALPH)]
            if decrypted_name == 'northpoleobjectstorage':
                return id


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
