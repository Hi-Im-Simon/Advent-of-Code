file = open('2020/inputs/input-00.txt')
tiles, tile = [], {}
for line in file:
    if line[0] == 'T':
        cur = int(line.split()[1].strip(':'))
        tiles.append(cur)
        tile[cur] = []
    else:
        if line != '\n':
            tile[cur].append(line.strip())


def rotateRight(tile):
    tile2 = [[''] * len(tile) for _ in range(len(tile[0]))]
    for row in range(len(tile)):
        for col in range(len(tile[0])):
            tile2[col][row] = tile[row][col]
    return [''.join(x) for x in tile2]


for t in tile[tiles[0]]:
    print(t)
print('\n')
for t in rotateRight(tile[tiles[0]]):
    print(t)

file.close()
