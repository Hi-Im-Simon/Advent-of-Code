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


def part1(f):
    data = prep_input(f)
    triplets = dict()
    ans = 0
    indices = set()
    
    i = 0
    while True:
        md5 = string_to_md5(data + str(i))
        
        for j in range(2, len(md5)-2):
            if (md5[j-2] == md5[j-1] == md5[j] == md5[j+1] == md5[j+2]):
                for k in triplets[md5[j]]:
                    if i - k < 1000:
                        print(i, k)
                        ans += 1
                        indices.add(k)
                        break
                # break
        if ans >= 64:
            return max(indices), sorted(indices)
        # if i == 22728: 
        #     print(md5)
        #     return
        
        for j in range(1, len(md5)-1):
            if md5[j-1] == md5[j] == md5[j+1]:
                if md5[j] in triplets.keys():
                    triplets[md5[j]].append(i)
                else:
                    triplets[md5[j]] = [i]
                break   # because we only consider the first triplet
        i += 1


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(tf) }")
print(f"part 2:\n{ part2(f) }")
