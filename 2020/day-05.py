file = open('2020/inputs/input-05.txt')
f = [[x[:7], x[7:].strip()] for x in file.readlines()]


def decode(code):
    ans = []
    a, b = 0, 127
    for c in code[0]:
        if c == 'F':
            b = (a + b) // 2
        else:
            a = (a + b + 1) // 2
    ans.append(a)

    a, b = 0, 7
    for c in code[1]:
        if c == 'L':
            b = (a + b) // 2
        else:
            a = (a + b + 1) // 2
    ans.append(a)
    return ans


def highest_seat(file):
    ans = 0
    for seat in file:
        t = decode(seat)
        t = t[0] * 8 + t[1]
        if t > ans:
            ans = t
    return ans


def find_your_seat(file):
    seatIds = []
    for seat in file:
        t = decode(seat)
        t = t[0] * 8 + t[1]
        seatIds.append(t)
    
    for i in range(highest_seat(file)):
        if i not in seatIds and i - 1 in seatIds and i + 1 in seatIds:
            return i


print(highest_seat(f))
print(find_your_seat(f))

file.close()
