tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-04.txt').readlines()]


def prep_input(f):
    nums = [int(x) for x in f[0].split(',')]
    boards = []
    i = 0
    for y in range(2, len(f)):
        if f[y] == '':
            i += 1
        else:
            if len(boards) > i:
                boards[i].append([int(x) for x in f[y].split()])
            else:
                boards.append([[int(x) for x in f[y].split()]])
    return nums, boards


def is_bingo(board, x, y):
    if sum([1 if x == 'x' else 0 for x in board[y]]) == len(board[0]):
        return True
    elif sum([1 if y[x] == 'x' else 0 for y in board]) == len(board):
        return True
    return False


def bingo(f, pos='first'):
    nums, boards = prep_input(f)
    for num in nums:
        for board in boards.copy():
            for y, row in enumerate(board):
                if num in row:
                    x = row.index(num)
                    may_be_winner = row[x]
                    row[x] = 'x'
                    if is_bingo(board, x, y):
                        if pos == 'last':
                            if len(boards) > 1:
                                boards.remove(board)
                            else:
                                return sum([sum([x if x != 'x' else 0 for x in y]) for y in board]) * may_be_winner
                        else:
                            return sum([sum([x if x != 'x' else 0 for x in y]) for y in board]) * may_be_winner


print('part 1:\n' + str(bingo(f)))
print('part 2:\n' + str(bingo(f, 'last')))
