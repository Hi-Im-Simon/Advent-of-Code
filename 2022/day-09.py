tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-09.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.rstrip().split() for x in f]
    data = [(d[0], int(d[1])) for d in data]
    return data


def move_snake(H, T, direc, is_real_head=False):
    # move head if it's the read head
    if is_real_head:
        if direc == 'U':
            H[1] += 1
        if direc == 'R':
            H[0] += 1
        if direc == 'D':
            H[1] -= 1
        if direc == 'L':
            H[0] -= 1

    # adjust tail placement
    w, h = (H[0] - T[0]), (H[1] - T[1])
    if abs(w) <= 1 and abs(h) <= 1:
        return H, T

    if w > 0:
        T[0] += 1
    elif w < 0:
        T[0] -= 1
    if h > 0:
        T[1] += 1
    elif h < 0:
        T[1] -= 1
    return H, T


def part1(f):
    data = prep_input(f)
    # head x y : tail x y
    H, T = [0, 0], [0, 0]
    visited = set([(0, 0)])
    
    # for each direction given
    for line in data:
        direc = line[0]
        for _ in range(line[1]):
            H, T = move_snake(H, T, direc, True)
            visited.add(tuple(T))
    return len(visited)


def part2(f):
    data = prep_input(f)
    # head x y : tail x y
    S = [[0, 0] for _ in range(10)]
    visited = set([(0, 0)])

    # for each direction given
    for line in data:
        direc = line[0]
        for _ in range(line[1]):
            # each move starts here
            S[0], S[1] = move_snake(S[0].copy(), S[1].copy(), direc, True)
            for i in range(1, len(S)-1):
                S[i], S[i+1] = move_snake(S[i].copy(), S[i+1].copy(), direc)
                
            visited.add(tuple(S[-1]))
    return len(visited)


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
