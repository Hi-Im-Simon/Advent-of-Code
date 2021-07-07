file = open('2020/inputs/input-16.txt')
f = [x.strip() for x in file.readlines()]


def find_error_tickets(file, code = 0):
    avaNums, ans, tab1, tab3 = set(), 0, [], []
    file = [x.split(' ') for x in file]
    sector = 0
    for line in file:
        if line == ['']: 
            sector += 1
            continue
        if sector == 0:
            if len(line) == 4:
                tab1.append([line[0][:-1]] + [line[1]] + [line[-1]])
            elif len(line) == 5:
                tab1.append([line[0] + ' ' + line[1][:-1]] + [line[2]] + [line[-1]])
            for field in line:
                if '-' in field:
                    a, b = field.split('-')
                    a, b = int(a), int(b)
                    for i in range(a, b + 1):
                        avaNums.add(i)
        elif sector == 1:
            if 'your' in line:
                continue
            tab2 = [int(x) for x in line[0].split(',')]
        elif sector == 2:
            if 'nearby' in line:
                continue
            line = [int(x) for x in line[0].split(',')]
            for i in range(len(line)):
                if line[i] not in avaNums:
                    ans += line[i]
                    line[i] = 'x'
            tab3.append(line)
    if code:
        return tab1, tab2, tab3
    return ans


def solve(file):
    tab1, tab2, tab3 = find_error_tickets(file, 1)
    belongs = {}
    for x in range(len(tab3[0])):
        for code in range(len(tab1)):
            a, b = [int(x) for x in tab1[code][1].split('-')]
            c, d = [int(x) for x in tab1[code][2].split('-')]
            
            for y in range(len(tab3)):
                if tab3[y][x] == 'x' or a <= tab3[y][x] <= b or c <= tab3[y][x] <= d:
                    continue
                else:
                    break
            else:
                if tab1[code][0] in belongs:
                    belongs[tab1[code][0]] += [x]
                else:
                    belongs[tab1[code][0]] = [x]
    final = {}
    for _ in range(len(belongs)):
        m = len(belongs) + 1
        for el in belongs:
            if len(belongs[el]) < m:
                m = len(belongs[el])
                minEle = el
        val = belongs[minEle][0]
        final[minEle] = val
        del belongs[minEle]
        for el in belongs:
            belongs[el].remove(val)
    ans = 1
    for key in final:
        if 'departure' in key:
            ans *= tab2[final[key]]
    return ans


print(find_error_tickets(f))
print(solve(f))

file.close()
