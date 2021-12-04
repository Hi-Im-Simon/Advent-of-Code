from itertools import permutations

tf = [x.strip().strip('.').split() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip().strip('.').split() for x in open('2015/inputs/input-13.txt').readlines()]


def prep_input(f):
    guests = {}
    for line in f:
        if line[0] not in guests:
            guests[line[0]] = {}
        guests[line[0]][line[10]] = int(line[3]) if line[2] == 'gain' else -int(line[3])
    return guests


def get_happiness(guests, order):
    happiness = 0
    for i in range(len(order)-1):
        happiness += guests[order[i]][order[i+1]] + guests[order[i+1]][order[i]]
    return happiness
            

def optimal_happiness(f, incl=None):
    guests = prep_input(f)
    if incl:
        guests[incl] = {}
        for person in guests:
            if person != incl:
                guests[incl][person] = 0
                guests[person][incl] = 0
            
    orders = list(permutations(list(guests)))
    return max([get_happiness(guests, list(x) + [x[0]]) for x in orders])


# def optimal_happiness_with_you(f):
    
    

print('part 1:\n' + str(optimal_happiness(f)))
print('part 2:\n' + str(optimal_happiness(f, 'you')))
