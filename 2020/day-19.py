file = open('2020/inputs/input-00.txt')
f = [x.strip() for x in file.readlines()]
rules, msgs = {}, []
i = 0
while f[i] != '':
    t = f[i].split(': ')
    t[1] = t[1].strip('"').split()
    rules[t[0]] = t[1]
    i += 1
while i < len(f) - 1:
    i += 1
    msgs.append(f[i])


def getMsgs(rules, msgs, rule = '0'):
    words = []
    if rule in ['a', 'b']:
        return rule
    for r in rules[rule]:
        if r != '|':
            words2 = getMsgs(rules, msgs, r)
            for w in words2:
                pass

    if '|' in rules[rule]:
        pass
    else:
        pass
    return t


print(rules, msgs)
print(getMsgs(rules, msgs))

file.close()
