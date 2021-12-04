tf = [x.strip() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2015/inputs/input-08.txt').readlines()]


def count_char(f):
    string_c = 0
    memory_c = 0
    for line in f:
        string_c += len(line)
        memory_c += (len(eval(line)))
    return string_c, memory_c, string_c - memory_c


def count_encoded_char(f):
    encoded_c = 0
    string_c =  count_char(f)[0]
    for line in f:
        encoded_c += 2 + len(line) + line.count('"') + line.count('\\')
    return encoded_c, string_c, encoded_c - string_c


print('part 1:\n' + str(count_char(f)[2]))
print('part 2:\n' + str(count_encoded_char(f)[2]))
