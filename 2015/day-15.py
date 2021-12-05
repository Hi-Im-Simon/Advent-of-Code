tf = [x.strip().split() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip().split() for x in open('2015/inputs/input-15.txt').readlines()]


def prep_input(f):
    ingr = {}
    for line in f:
        head = line[0][:-1]
        ingr[head] = {}
        for i in range(1, len(line), 2):
            ingr[head][line[i]] = int(line[i+1].strip(','))
    return ingr


def best_recipy(f):
    for i in range(101):
        pass


print(prep_input(tf))
#print('part 1:\n' + str(ans1))
#print('part 2:\n' + str(ans2))
