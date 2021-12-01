tf = [line.strip() for line in open('2015/inputs/input-00.txt').readlines()]
f = [line.strip() for line in open('2015/inputs/input-05.txt').readlines()]

vowels = 'aeiou'
no_no_strs = ['ab', 'cd', 'pq', 'xy']


def find_nice1(f):
    nice = 0
    for line in f:
        vowel_c = 0
        for v in vowels:
            vowel_c += line.count(v)
        if vowel_c < 3:
            continue
        
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                f = True
                break
        else:
            continue
        
        f = False
        for s in no_no_strs:
            if s in line:
                f = True
                break
        if f:
            continue
        nice += 1
    return nice

def find_nice2(f):
    nice = 0
    for line in f:
        for i in range(len(line)-1):
            pair = line[i:i+2]
            if pair in line[i+2:]:
                break
        else:
            continue
    
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                break
        else:
            continue
        nice += 1
    return nice


print('part 1:\n' + str(find_nice1(f)))
print('part 2:\n' + str(find_nice2(f)))
