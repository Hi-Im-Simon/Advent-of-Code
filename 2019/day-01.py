file = open('2019/inputs/input-01.txt')
f = [x.strip() for x in file]


def findMass(file):
    ans = 0
    for i in file:
        ans += int(i) // 3 - 2
    return ans


def findMassRec(m):
    m = int(m) // 3 - 2
    if m > 0:
        return m + findMassRec(m)
    return 0


def findMass2(file):
    ans = 0
    for i in file:
        ans += findMassRec(i)
    return ans


print(findMass(f))
print(findMass2(f))

file.close()
