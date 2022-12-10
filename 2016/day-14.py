import hashlib
tf = open('2016/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2016/inputs/input-14.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.rstrip() for x in f][0]
    return data


def string_to_md5(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


def vals_to_md5(string, num, repeat=1):
    global HASHES
    if len(HASHES) > num:
        return HASHES[num]
    m = string + str(num)
    for _ in range(repeat):
        m = string_to_md5(m)
    HASHES.append(m)
    return m


def parts1_2(f, repeat=1):
    data = prep_input(f)
    indices = set()
    
    i = 0
    while len(indices) < 64:
        md5 = vals_to_md5(data, i, repeat)

        for j in range(1, len(md5)-1):
            if md5[j-1] == md5[j] == md5[j+1]:
                for k in range(1, 1001):
                    md52 = vals_to_md5(data, i + k, repeat)
                    if md5[j]*5 in md52:
                        indices.add(i)
                break
                    
        i += 1
    return sorted(indices)[-1]


HASHES = []
print(f"part 1:\n{ parts1_2(f) }")
HASHES = []
print(f"part 2:\n{ parts1_2(f, 2017) }")   # this will take a while

