import math

# tf = int([x.strip() for x in open('2015/inputs/input-00.txt').readlines()][0])
f = int([x.strip() for x in open('2015/inputs/input-20.txt').readlines()][0])


def part1(f):
    house_i = 1
    while True:
        summ = 0
        for i in range(1, int(math.sqrt(house_i))+1):
            if house_i % i == 0:
                if house_i / i == i:
                    summ += i
                else:
                    summ += i + house_i / i
        if summ * 10 >= f:
            return house_i
        house_i += 1


def part2(f):
    house_i = 1
    elfs = [0]
    while True:
        elfs.append(50)
        summ = 0
        for i in range(1, int(math.sqrt(house_i))+1):
            if house_i % i == 0:
                if house_i / i == i:
                    if elfs[i] > 0:
                        summ += i
                        elfs[i] -= 1
                else:
                    if elfs[i] > 0:
                        summ += i
                        elfs[i] -= 1
                    if elfs[int(house_i / i)] > 0:
                        summ += house_i / i
                        elfs[int(house_i / i)] -= 1
                    
        if summ * 11 >= f:
            return house_i
        house_i += 1


# both might take a moment! (up to ~20-30 seconds)
print(f'part 1:\n{ part1(f) }')
print(f'part 2:\n{ part2(f) }')
