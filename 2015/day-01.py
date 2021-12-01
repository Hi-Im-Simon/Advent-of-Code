f = open('2015/inputs/input-01.txt').read()

floor = 0
basement = -1

for i, char in enumerate(f):
    if char == ')':
        floor -= 1
    else:
        floor += 1
    if basement < 0 and floor == -1:
        basement = i + 1
        
print('part 1:\n' + str(floor))
print('part 2:\n' + str(basement))
