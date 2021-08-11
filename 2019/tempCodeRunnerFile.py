def findMassRec(m):
    m = int(m) // 3 - 2
    if m > 0:
        return m + findMassRec(m)
    return 0