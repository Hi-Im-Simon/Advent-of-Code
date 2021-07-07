file = open('2020/inputs/input-07.txt')
f = [x.strip()[:-1].split(' bags contain ') for x in file.readlines()]
bags = {}

for line in f:
    line[1] = line[1].split(', ')
    if line[1][0] != 'no other bags':
        for i in range(len(line[1])):
            line[1][i] = (int(line[1][i][0]), line[1][i][1:].strip().replace(' bags', '').replace(' bag', ''))
            bags[line[0]] = line[1]
    else:
        bags[line[0]] = [(0, 'none')]


def is_bag1_in_bag2(bag1, bag2):
    ans = 0
    for b in bags[bag2]:
        if b[0] == 0:
            return False
        if b[1] == bag1:
            return True
        if is_bag1_in_bag2(bag1, b[1]):
            return True


def how_many_bags_contain(file, bag):
    ans = 0
    for b in file:
        if is_bag1_in_bag2(bag, b[0]):
            ans += 1
    return ans


def count_bags_inside(file, bag):
    ans = 0
    for b in bags[bag]:
        if b[0] > 0:
            count = count_bags_inside(file, b[1])
            ans += b[0] * count + b[0]
    return ans


print(how_many_bags_contain(f, 'shiny gold'))
print(count_bags_inside(f, 'shiny gold'))

file.close()
