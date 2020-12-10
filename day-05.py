def find_seat_id(i):
    row, col = int(file[i][0], 2), int(file[i][1], 2)
    return row * 8 + col

def ch1(f):
    ans = 0
    for i in range(len(f)):
        seat_id = find_seat_id(i)
        ans = max(ans, seat_id)
    print(ans)


def ch2(f):
    seats = []
    for i in range(len(f)):
        seats.append(find_seat_id(i))
    seats = sorted(seats)
    [print(x) for x in range(seats[0], seats[-1]+1) if x not in seats]




file = open('c:/Code/Advent of Code/2020/inputs/input-05.txt').readlines()
file = [[file[i][:7].replace('F', '0').replace('B', '1'), file[i][7:-1].replace('L', '0').replace('R', '1')] for i in range(len(file))]

ch1(file)
ch2(file)