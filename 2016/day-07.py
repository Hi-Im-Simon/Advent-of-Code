tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-07.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    for i, line in enumerate(data):
        seqs, hypernets = [], []
        line += '['
        seq = ''
        for let in line:
            if let == '[' and len(seq) > 0:
                seqs.append(seq)
                seq = ''
            elif let == ']':
                hypernets.append(seq)
                seq = ''
            else:
                seq += let
        data[i] = [seqs, hypernets]
    return data


def is_abba(string, flag=4):
    return len(string) == flag and string[:len(string) // 2] == string[len(string) // 2 + flag % 2:][::-1] and string[0] != string[1]


def part1(f):
    data = prep_input(f)
    ans = 0
    for line in data:
        TLS = True
        for el in line[1]:
            for i in range(len(el) - 3):
                if is_abba(el[i:i+4]):
                    TLS = False
                    break
        if TLS:
            TLS = False
            for el in line[0]:
                for i in range(len(el) - 3):
                    if is_abba(el[i:i+4]):
                        TLS = True
            if TLS: 
                ans += 1
    return ans


def part2(f):
    data = prep_input(f)
    ans = 0
    for line in data:
        SSL = False
        for el in line[0]:
            for i in range(len(el) - 2):
                if is_abba(el[i:i+3], 3):
                    for el2 in line[1]:
                        for j in range(len(el2) - 2):
                            if el[i:i+3] == el2[j+1] + el2[j] + el2[j+1] and el2[j] == el2[j+2]:
                                SSL = True
                                break
        if SSL:
            ans += 1
    return ans


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
