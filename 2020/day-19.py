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


def getMsgs(rules, msgs, rule = '0', word = ''):
    print(rule, word)
    if rule in ['a', 'b']:
        word += rule
        return word
    elif '|' in rules[rule]:
        a, b = rules[rule][0:2]
        word += getMsgs(rules, msgs, a)
        word += getMsgs(rules, msgs, b)
    else:
        for m in rules[rule]:
            if m != '|':
                getMsgs(rules, msgs, m)


print(rules, msgs)
print(getMsgs(rules, msgs))

file.close()
