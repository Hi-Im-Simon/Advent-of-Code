f = [x.strip().split() for x in open('2015/inputs/input-16.txt').readlines()]


def prep_input(f):
    aunts = []
    for line in f:
        aunt = {'children': 'x',
                'cats': 'x',
                'samoyeds': 'x',
                'pomeranians': 'x',
                'akitas': 'x',
                'vizslas': 'x',
                'goldfish': 'x',
                'trees': 'x',
                'cars': 'x',
                'perfumes': 'x'
                }
        for i in range(2, len(line), 2):
            aunt[line[i].strip(':')] = int(line[i+1].strip(','))
        aunts.append(aunt)
    return aunts


def find_aunt(f):
    aunts = prep_input(f)
    for i, aunt in enumerate(aunts):
        if aunt['children'] in [3, 'x'] and aunt['cats'] in [7, 'x'] and aunt['samoyeds'] in [2, 'x'] and aunt['pomeranians'] in [3, 'x'] and aunt['akitas'] in [0, 'x'] and aunt['vizslas'] in [0, 'x'] and aunt['goldfish'] in [5, 'x'] and aunt['trees'] in [3, 'x'] and aunt['cars'] in [2, 'x'] and aunt['perfumes'] in [1, 'x']:
            return i + 1
        
def find_aunt_ranges(f):
    aunts = prep_input(f)
    for i, aunt in enumerate(aunts):
        if aunt['children'] in [3, 'x'] and (aunt['cats'] == 'x' or aunt['cats'] > 7) and aunt['samoyeds'] in [2, 'x'] and (aunt['pomeranians'] == 'x' or aunt['pomeranians'] < 3) and aunt['akitas'] in [0, 'x'] and aunt['vizslas'] in [0, 'x'] and (aunt['goldfish'] == 'x' or aunt['goldfish'] < 5) and (aunt['trees'] == 'x' or aunt['trees'] > 3) and aunt['cars'] in [2, 'x'] and aunt['perfumes'] in [1, 'x']:
            return i + 1
    
    
print('part 1:\n' + str(find_aunt(f)))
print('part 2:\n' + str(find_aunt_ranges(f)))
