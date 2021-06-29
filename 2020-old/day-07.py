def find_bag(b):
    a = 0
    for i in range(len(bags_in_bag[b])):
        if 'shiny gold bags' == bags_in_bag[b][i]:
            return 1
        else:
            if ' other bags' != bags_in_bag[b][i]:
                a += find_bag(bag.index(bags_in_bag[b][i]))
    if a > 0: return 1
    else: return 0


def find_id(b):
    return bag.index(b)


def ch1():
    ans = 0
    for i in range(len(bag)):
        if 'shiny gold bags' in bags_in_bag[i]: # if bag[i] IS or one of bags in bags_in_bag[i] IS then go to next one
            ans += 1
        else:
            ans += find_bag(i)
    return ans


def ch2(b, amount):
    ans = 0
    b_id = find_id(b)
    if ' other bags' not in bags_in_bag[b_id]:
        for i in range(len(bags_in_bag[b_id])):
            ans += ch2(bags_in_bag[b_id][i], am_of_bags_in_bags[b_id][i])
        return (ans + 1) * amount
    else:
        return amount


file = open('c:/Code/Advent of Code/2020/inputs/input-07.txt').read().split('\n')
file = [[f.split(' contain ')[0]] + [f.split(' contain ')[1][:-1].split(', ')] for f in file]
bag, bags_in_bag, am_of_bags_in_bags = [file[i][0] for i in range(len(file))], [[file[i][1][j][2:] if file[i][1][j][-1] == 's' else file[i][1][j][2:]+'s' for j in range(len(file[i][1]))] for i in range(len(file))], [[int(file[i][1][j][0]) if file[i][1][j][0] != 'n' else 0 for j in range(len(file[i][1]))] for i in range(len(file))]

# print(ch1()) # it takes a few seconds
print(ch2('shiny gold bags', 1) - 1)
#[print(bags_in_bag[i], am_of_bags_in_bags[i]) for i in range(len(bag))]